import os
import time
from dbfread import DBF
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
# from sqlalchemy.sql import insert
from tqdm import tqdm

def dbf_to_sqlalchemy_records(dbf, field_names):
    # Prepara registros para inserção
    for record in dbf:
        yield {field: record.get(field.upper(), None) for field in field_names}

def dbf_to_postgresql_create_sql(dbf_file_path, table_name):
    table = DBF(dbf_file_path, load=False, ignore_missing_memofile=True)
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
    field_mappings = {
        'C': 'VARCHAR',
        'N': 'NUMERIC',
        'F': 'REAL',
        'D': 'DATE',
        'L': 'BOOLEAN',
        'M': 'TEXT'
    }

    # Armazenar todos os nomes de campo
    field_names = {}

    for field in table.fields:
        field_type = field.type
        original_field_name = field.name.lower()
        
        # Se o nome já existir, incrementa o sufixo
        field_name = original_field_name
        count = 1
        while field_name in field_names:
            field_name = f"{original_field_name}_{count}"
            count += 1

        # Armazena o nome final no dicionário para prevenir outros duplicados
        field_names[field_name] = None

        if field_type == 'C':
            sql_type = f"VARCHAR({field.length})"
        else:
            sql_type = field_mappings.get(field_type, 'TEXT')

        sql += f"{field_name} {sql_type},\n"

    sql = sql.rstrip(",\n") + "\n);"
    return sql

def create_tables_from_dbfs(dbf_directory, database_url):
    # Cria a engine de conexão com o banco de dados
    engine = create_engine(database_url)

    try:
        # Itera sobre cada arquivo DBF na pasta
        for filename in os.listdir(dbf_directory):
            if filename.endswith('.DBF') or filename.endswith('.dbf'):
                dbf_file_path = os.path.join(dbf_directory, filename)
                table_name = os.path.splitext(filename)[0].lower()  # Nome da tabela baseado no nome do arquivo

                # Gerar o SQL de criação de tabela
                create_table_sql = dbf_to_postgresql_create_sql(dbf_file_path, table_name)

                # Executa o SQL de criação da tabela
                with engine.connect() as connection:
                    connection.execute(create_table_sql)
                    print(f"Tabela '{table_name}' criada com sucesso.")
    except SQLAlchemyError as e:
        print(f"Erro ao executar SQL: {e}")

def migrate_dbf_to_postgresql(dbf_directory, database_url, batch_size=3000):
    # Cria a engine e metadata do SQLAlchemy
    engine = create_engine(database_url)
    metadata = MetaData(bind=engine)

    try:
        dbf_files = [f for f in os.listdir(dbf_directory) if f.endswith('.DBF') or f.endswith('.dbf')]

        for filename in tqdm(dbf_files, desc="Arquivos DBF processados"):
            dbf_file_path = os.path.join(dbf_directory, filename)
            table_name = os.path.splitext(filename)[0].lower()
            
            with engine.connect() as connection:
                table = Table(table_name, metadata, autoload_with=engine)
                
                dbf = DBF(dbf_file_path, ignore_missing_memofile=True, encoding='latin1')
                field_names = [col.name for col in table.columns]

                # Lista de registros para inserção em lotes
                records = list(dbf_to_sqlalchemy_records(dbf, field_names))

                # Inserção em lotes
                for i in tqdm(range(0, len(records), batch_size), desc=f"Migrando dados de {filename}"):
                    batch = records[i:i + batch_size]
                    try:
                        connection.execute(table.insert(), batch)
                    except (IntegrityError, OperationalError) as e:
                        print(f"Erro ao inserir lote de registros na '{table_name}': {e}")
                        continue

            print(f"Dados de '{filename}' migrados com sucesso para a tabela '{table_name}'.")

    except SQLAlchemyError as e:
        print(f"Erro ao migrar dados para {table_name}: {e}")

# Defina o diretório contendo os arquivos DBF e a URL do banco de dados
dbf_directory = './dbf'
database_url = 'postgresql://postgres:syncode123@127.0.0.1:5432/conv_601_RUY_SILVA_SANTANA_LTDA'

# Marca o tempo de início
start_time = time.time()
# Execute a função para processar os arquivos DBF
create_tables_from_dbfs(dbf_directory, database_url)
migrate_dbf_to_postgresql(dbf_directory, database_url)
end_time = time.time()
total_time_seconds = end_time - start_time
total_time_minutes = total_time_seconds / 60  # Converte segundos para minutos
print(f"Tempo total de execução: {total_time_minutes:.2f} minutos")
