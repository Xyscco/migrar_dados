import fdb
import psycopg2
import unicodedata

from fdb import fbcore
from psycopg2 import sql
from tqdm import tqdm
import logging

logging.basicConfig(filename='migration_errors.log', level=logging.ERROR)

def connect_firebird(host, database, user, password, port = 3051, charset = 'WIN1252'):
    """Conecta ao banco de dados Firebird."""
    try:
        connection = fdb.connect(
            host=host, port=port, database=database,
            user=user, password=password, charset=charset
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao Firebird: {e}")
        return None

def connect_postgres(host, database, user, password):
    """Conecta ao banco de dados PostgreSQL."""
    try:
        connection = psycopg2.connect(
            host=host, database=database,
            user=user, password=password,
            client_encoding='WIN1252'
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

def get_firebird_tables(fb_conn):
    """Obtém a estrutura das tabelas do Firebird."""
    cursor = fb_conn.cursor()
    cursor.execute("""
        SELECT TRIM(rdb$relation_name)
        FROM rdb$relations
        WHERE rdb$view_blr IS NULL
        AND (rdb$system_flag IS NULL OR rdb$system_flag = 0)
        ORDER BY rdb$relation_name
    """)
    tables = [row[0].strip() for row in cursor.fetchall()]
    
    table_structures = {}
    for table in tables:
        cursor.execute(f"""
            SELECT 
                TRIM(rf.RDB$FIELD_NAME),
                f.RDB$FIELD_TYPE,
                f.RDB$FIELD_SUB_TYPE,
                f.RDB$FIELD_LENGTH
            FROM RDB$RELATION_FIELDS rf
            JOIN RDB$FIELDS f ON rf.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME
            WHERE rf.RDB$RELATION_NAME = '{table}'
            ORDER BY rf.RDB$RELATION_NAME, rf.RDB$FIELD_POSITION 
        """)
        fields = [(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
        table_structures[table] = fields
    
    return table_structures

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

def create_postgres_tables(pg_conn, table_structures):
    """Cria tabelas no PostgreSQL baseadas na estrutura do Firebird."""
    cursor = pg_conn.cursor()
    for table, fields in tqdm(table_structures.items(), desc="Criando tabelas"):
        columns = []
        for field, field_type, field_sub_type, field_length in fields:
            # Mapeamento simples de tipos Firebird para PostgreSQL
            pg_type = map_data_type(field_type, field_sub_type, field_length)
            
            columns.append(f"{field} {pg_type}")
        
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(columns)})"
        cursor.execute(create_table_query)
    
    pg_conn.commit()


def safe_decode(value, encodings=['WIN1252', 'ISO8859_1', 'UTF8']):
    if isinstance(value, str):
        return value
    for encoding in encodings:
        try:
            return value.decode(encoding)
        except UnicodeDecodeError:
            continue
    return value.decode('utf-8', errors='ignore')


def migrate_data(fb_conn, pg_conn, table_structures):
    fb_cursor = fb_conn.cursor()
    pg_cursor = pg_conn.cursor()
    
    for table, fields in tqdm(table_structures.items(), desc="Migrando tabelas"):
        fb_cursor.execute(f"SELECT * FROM {table}")
        columns = [field[0].lower() for field in fields]
        
        insert_query = sql.SQL("INSERT INTO {} ({}) VALUES {}").format(
            sql.Identifier(table.lower()),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join([sql.SQL('({})').format(sql.SQL(', ').join([sql.Placeholder()] * len(columns)))] * 3000)
        )
        
        batch = []
        total_inserted = 0
        
        while True:
            try:
                rows = fb_cursor.fetchmany(3000)
                if not rows:
                    break
                
                for row in rows:
                    processed_row = []
                    for value in row:
                        if value is None:
                            processed_row.append(None)
                        elif isinstance(value, bytes):
                            processed_row.append(safe_decode(value))
                        elif isinstance(value, str):
                            processed_row.append(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii'))
                        else:
                            processed_row.append(value)
                    
                    batch.extend(processed_row)
                
                if len(batch) >= 3000 * len(columns):
                    try:
                        pg_cursor.execute(insert_query, batch)
                        pg_conn.commit()
                        total_inserted += len(batch) // len(columns)
                        batch = []
                    except psycopg2.Error as e:
                        print(f"Erro ao inserir lote na tabela {table}: {e}")
                        pg_conn.rollback()
                        batch = []
            
            except Exception as e:
                logging.error(f"Erro ao processar dados da tabela {table}: {insert_query}")
                print(f"Erro ao processar dados da tabela {table}: {e}")
                continue
        
        # Inserir registros restantes
        if batch:
            remaining_count = len(batch) // len(columns)
            remaining_query = sql.SQL("INSERT INTO {} ({}) VALUES {}").format(
                sql.Identifier(table.lower()),
                sql.SQL(', ').join(map(sql.Identifier, columns)),
                sql.SQL(', ').join([sql.SQL('({})').format(sql.SQL(', ').join([sql.Placeholder()] * len(columns)))] * remaining_count)
            )
            try:
                pg_cursor.execute(remaining_query, batch)
                pg_conn.commit()
                total_inserted += remaining_count
            except psycopg2.Error as e:
                print(f"Erro ao inserir lote final na tabela {table}: {e}")
                pg_conn.rollback()
        
        print(f"Total de registros inseridos em {table}: {total_inserted}")


def main():
    # Configurações de conexão
    fb_config = {
        "host": "localhost", "database": "D:\\Syncode\\projetos-Python\\migrar-dados\\firebird4_to_postgres\\bancos\CADASTRO.FDB",
        "user": "sysdba", "password": "masterkey"
    }
    pg_config = {
        "host": "localhost", "database": "migradorfb4",
        "user": "postgres", "password": "syncode123"
    }
    
    # Conectar aos bancos de dados
    fb_conn = connect_firebird(**fb_config)
    pg_conn = connect_postgres(**pg_config)
    
    if fb_conn and pg_conn:
        # Obter estrutura das tabelas do Firebird
        table_structures = get_firebird_tables(fb_conn)
        
        # Criar tabelas no PostgreSQL
        create_postgres_tables(pg_conn, table_structures)
        
        # Migrar dados
        migrate_data(fb_conn, pg_conn, table_structures)
        
        print("Migração concluída com sucesso!")
    else:
        print("Falha na conexão com os bancos de dados.")
    
    # Fechar conexões
    if fb_conn:
        fb_conn.close()
    if pg_conn:
        pg_conn.close()

if __name__ == "__main__":
    main()