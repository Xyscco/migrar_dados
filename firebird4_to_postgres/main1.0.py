import fdb
import psycopg2
from psycopg2 import extras
from tqdm import tqdm
import collections
import concurrent.futures
import chardet
import logging

# Configuração básica de logging
logging.basicConfig(filename='data_migration.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def map_data_type(field_type, field_sub_type, field_length):
    if field_type == 7:
        return 'SMALLINT'
    elif field_type == 8:
        return 'INTEGER'
    elif field_type == 9:
        return 'BYTEA'
    elif field_type == 10:
        return 'REAL'
    elif field_type == 11:
        return 'DOUBLE PRECISION'
    elif field_type == 12:
        return 'DATE'
    elif field_type == 13:
        return 'TIME'
    elif field_type == 14:
        if field_length == 0:
            return 'CHAR'
        else:
            return f'CHAR({field_length})'
    elif field_type == 16:
        if field_sub_type == 1:
            return f'NUMERIC'
        else:
            return 'BIGINT'
    elif field_type == 27:
        return 'DOUBLE PRECISION'
    elif field_type == 35:
        return 'TIMESTAMP'
    elif field_type == 37:
        return f'VARCHAR({field_length})'
    elif field_type == 261:
        if field_sub_type == 0:
            return 'BYTEA'
    return 'TEXT'

def fetch_blob_as_text(blob_field):
    if blob_field is not None:
        content = blob_field.read()
        detected = chardet.detect(content)
        return content.decode(detected['encoding'] or 'windows-1252', errors='ignore')
    return None

def robust_decode(value):
    """Tenta decodificar de diferentes maneiras, detectando automaticamente."""
    if isinstance(value, bytes):
        detected = chardet.detect(value)
        print(f"Detected encoding: {detected['encoding']}")
        try:
            return value.decode(detected['encoding'] or 'windows-1252', errors='replace')
        except UnicodeDecodeError:
            return value.decode('utf-8', 'replace')
    if isinstance(value, str):
        return value
    return str(value)

# def process_and_insert_data(rows, insert_sql, pg_cursor):
#     batch = []
#     for row in rows:
#         processed_row = [robust_decode(value) for value in row]
#         converted_row = [(fetch_blob_as_text(value) if isinstance(value, fdb.BlobReader) else value) for value in processed_row]
#         batch.append(converted_row)

#     if batch:
#         extras.execute_values(pg_cursor, insert_sql, batch, template=None, page_size=3000)

def process_and_insert_data(rows, insert_sql, pg_cursor):
    batch = []
    for row in rows:
        processed_row = [
            fetch_blob_as_text(value) if isinstance(value, fdb.BlobReader) else robust_decode(value)
            for value in row
        ]
        batch.append(processed_row)
    if batch:
        extras.execute_values(pg_cursor, insert_sql, batch, template=None, page_size=1000)

# Conectar ao banco de dados Firebird
fb_conn = fdb.connect(
    host='localhost', port=3051, database='D:\\Syncode\\projetos-Python\\migrar-dados\\firebird4_to_postgres\\bancos\CADASTRO.FDB',
    user='SYSDBA', password='masterkey'
)
fb_cursor = fb_conn.cursor()

# Consultar a estrutura das tabelas do Firebird
fb_cursor.execute("""
    SELECT rf.RDB$RELATION_NAME,
           rf.RDB$FIELD_NAME,
           f.RDB$FIELD_TYPE,
           f.RDB$FIELD_SUB_TYPE,
           f.RDB$FIELD_LENGTH,
           rf.RDB$NULL_FLAG
    FROM RDB$RELATION_FIELDS rf
    JOIN RDB$FIELDS f ON rf.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME
    WHERE rf.RDB$RELATION_NAME NOT LIKE 'RDB$%' and rf.RDB$RELATION_NAME NOT LIKE 'MON$%'
    ORDER BY rf.RDB$RELATION_NAME, rf.RDB$FIELD_POSITION
""")
tables_metadata = fb_cursor.fetchall()

tables_dict = collections.defaultdict(list)
columns_dict = collections.defaultdict(list)
for table, column, field_type, field_sub_type, field_length, null_flag in tables_metadata:
    postgres_data_type = map_data_type(field_type, field_sub_type, field_length)
    tables_dict[table.strip()].append(
        f"{column.strip()} {postgres_data_type} {'NOT NULL' if null_flag else ''}"
    )
    columns_dict[table.strip()].append(column.strip())

# Conectar ao banco de dados PostgreSQL
pg_conn = psycopg2.connect(
    dbname='migradorfb4',
    user='postgres',
    password='syncode123',
    host='localhost'
)
pg_cursor = pg_conn.cursor()

for table_name, columns in tqdm(tables_dict.items(), desc="Criando tabelas"):
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n  " + ",\n  ".join(columns) + "\n);"
    try:
        pg_cursor.execute(create_table_sql)
    except Exception as e:
        print(f"Erro ao criar tabela {table_name}: {e}")
    pg_conn.commit()

for table_name, column_list in tqdm(columns_dict.items(), desc="Inserindo dados"):
    try:
        columns = ", ".join(column_list)
        fb_query = f"SELECT {columns} FROM {table_name}"
        fb_cursor.execute(fb_query)
        
        rows = fb_cursor.fetchall()
        insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES %s"

        # Processar usando threads para performance
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            # Dividir a lista de linhas em blocos (chunk)
            for i in range(0, len(rows), 3000):
                executor.submit(process_and_insert_data, rows[i:i + 3000], insert_sql, pg_cursor)

    except fdb.fbcore.DatabaseError as e:
        print(f"Erro ao operar nas colunas de {table_name}: {e}")
    except Exception as e:
        print(f"Erro ao inserir dados na tabela {table_name}: {e}")
    pg_conn.commit()

# Fechar conexões
fb_conn.close()
pg_conn.close()