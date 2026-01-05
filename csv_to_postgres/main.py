import os
import time
import pandas as pd
import subprocess
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer, Float, Date, Boolean, Text, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import insert
from tqdm import tqdm
import numpy as np

log_file = 'migration_errors.log'

if os.path.exists(log_file):
    os.remove(log_file)

def csv_to_sqlalchemy_insert(table, df, field_names, batch_size=1):
    """
    Converte DataFrame em inserções SQLAlchemy com processamento em lotes
    """
    # Processa em lotes para melhor performance
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i+batch_size]
        records = []
        
        for _, row in batch.iterrows():
            # Prepara o dicionário para inserção, tratando valores NaN
            record_data = {}
            for field in field_names:
                value = row.get(field, None)
                # Converte NaN para None
                if pd.isna(value):
                    record_data[field] = None
                else:
                    record_data[field] = value
            records.append(record_data)
        
        # Retorna inserção em lote
        yield insert(table).values(records)

def infer_column_type(series, column_name):
    """
    Infere o tipo de coluna baseado nos dados da série pandas
    """
    # Remove valores nulos para análise
    non_null_series = series.dropna()

    # Comentado: sempre que for identificado como string, definir como TEXT
    # if 'barras' in column_name.lower() or 'princípio' in column_name.lower():
    #     with open(log_file, 'a') as f:
    #         f.write(f"{datetime.now()}: Devido ao nome a coluna {column_name} foi definida como TEXT\n")
    #     return Text()

    # if column_name == 'barras' or column_name == 'Barras':
    #     return String(255) 

    if 'ncm' in column_name.lower():
        return String(255) 

    # Para strings, determina o tamanho máximo
    if series.dtype == 'object':
        max_length = series.astype(str).str.len().max()
        if pd.isna(max_length):
            max_length = 255
        
        # Se muito longo, usa TEXT
        if max_length > 8000:
            return Text()
        else:
            return String(min(max_length + 50, 8000))  # Adiciona margem de segurança
    
    if len(non_null_series) == 0:
        return String(255)  # Default para colunas vazias
    
    # Tenta inferir tipo numérico
    if pd.api.types.is_numeric_dtype(series):
        # Verifica se são todos inteiros
        if pd.api.types.is_integer_dtype(series):
            return Integer()
        else:
            return Float()
    
    # Tenta inferir tipo booleano
    if pd.api.types.is_bool_dtype(series):
        return Boolean()
    
    # Tenta inferir tipo data
    if pd.api.types.is_datetime64_any_dtype(series):
        return Date()
    
    # Verifica se pode ser convertido para data
    if series.dtype == 'object':
        sample_values = non_null_series.head(100).astype(str)
        date_patterns = [
            '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d',
            '%d-%m-%Y', '%m-%d-%Y', '%Y%m%d'
        ]
        
        for pattern in date_patterns:
            try:
                pd.to_datetime(sample_values.head(10), format=pattern, errors='raise')
                return Date()
            except:
                continue
    
    # Default
    return String(255)

def clean_column_name(column_name):
    """
    Limpa e normaliza nomes de colunas para PostgreSQL
    """
    # Converte para string e remove espaços
    name = str(column_name).strip()
    
    # Remove acentos e caracteres especiais
    import unicodedata
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')
    
    # Converte para minúsculo
    name = name.lower()
    
    # Substitui espaços e caracteres especiais por underscore
    import re
    name = re.sub(r'[^a-z0-9_]', '_', name)
    
    # Remove underscores múltiplos
    name = re.sub(r'_+', '_', name)
    
    # Remove underscore no início e fim
    name = name.strip('_')
    
    # Se vazio ou começar com número, adiciona prefixo
    if not name or name[0].isdigit():
        name = f"col_{name}"
    
    return name

def csv_to_postgresql_create_sql(csv_file_path, table_name, delimiter=';', encoding='utf-8'):
    """
    Gera SQL de criação de tabela baseado na estrutura do CSV
    """
    try:
        # Lê uma amostra do CSV para inferir tipos
        df_sample = pd.read_csv(csv_file_path, delimiter=delimiter, encoding=encoding, nrows=1000)
        
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
        
        # Armazenar todos os nomes de campo para evitar duplicatas
        field_names = {}
        column_mapping = {}  # Para mapear nomes originais para nomes limpos
        
        for column in df_sample.columns:
            # Limpa o nome da coluna
            original_field_name = clean_column_name(column)
            
            # Se o nome já existir, incrementa o sufixo
            field_name = original_field_name
            count = 1
            while field_name in field_names:
                field_name = f"{original_field_name}_{count}"
                count += 1
            
            # Armazena o nome final no dicionário
            field_names[field_name] = None
            column_mapping[column] = field_name
            
            # Infere o tipo da coluna
            column_type = infer_column_type(df_sample[column], column)
            
            # Converte para SQL
            # Text deve ser testado antes de String, pois Text pode herdar de String
            if isinstance(column_type, Text):
                sql_type = "TEXT"
            elif isinstance(column_type, String):
                sql_type = f"TEXT"
            elif isinstance(column_type, Integer):
                sql_type = "INTEGER"
            elif isinstance(column_type, Float):
                sql_type = "REAL"
            elif isinstance(column_type, Date):
                sql_type = "DATE"
            elif isinstance(column_type, Boolean):
                sql_type = "BOOLEAN"
            else:
                sql_type = "VARCHAR(255)"
            
            sql += f"    {field_name} {sql_type},\n"
        
        sql = sql.rstrip(",\n") + "\n);"
        return sql, list(field_names.keys()), column_mapping
        
    except Exception as e:
        # print(f"Erro ao analisar CSV {csv_file_path}: {e}")
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now()}: {e}\n")
        return None, None, None

def create_tables_from_csvs(csv_directory, database_url, delimiter=',', encoding='utf-8'):
    """
    Cria tabelas no PostgreSQL baseadas nos arquivos CSV
    """
    engine = create_engine(database_url)
    table_mappings = {}  # Para armazenar mapeamento de colunas
    
    try:
        for filename in os.listdir(csv_directory):
            if filename.endswith('.csv') or filename.endswith('.CSV'):
                csv_file_path = os.path.join(csv_directory, filename)
                table_name = os.path.splitext(filename)[0].lower()
                
                print(f"Analisando estrutura de '{filename}'...")
                
                # Gerar o SQL de criação de tabela
                create_table_sql, field_names, column_mapping = csv_to_postgresql_create_sql(
                    csv_file_path, table_name, delimiter, encoding
                )
                
                if create_table_sql:
                    # Executa o SQL de criação da tabela dentro de uma transação
                    # engine.begin() abre conexão + transaction e commita ao sair do bloco
                    with engine.begin() as connection:
                        connection.execute(text(create_table_sql))
                        print(f"Tabela '{table_name}' criada com sucesso.")
                        
                        # Armazena o mapeamento para uso na migração
                        table_mappings[filename] = {
                            'field_names': field_names,
                            'column_mapping': column_mapping
                        }
                else:
                    print(f"Erro ao criar tabela para '{filename}'")
                    
    except SQLAlchemyError as e:
        # print(f"Erro ao executar SQL: {e}")
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now()}: {e}\n")
    except Exception as e:
        # print(f"Erro geral: {e}")
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now()}: {e}\n")
    
    return table_mappings

def migrate_csv_to_postgresql(csv_directory, database_url, table_mappings, delimiter=';', encoding='utf-8'):
    """
    Migra dados dos arquivos CSV para PostgreSQL
    """
    engine = create_engine(database_url)
    metadata = MetaData()
    
    try:
        for filename in os.listdir(csv_directory):
            if filename.endswith('.csv') or filename.endswith('.CSV'):
                csv_file_path = os.path.join(csv_directory, filename)
                table_name = os.path.splitext(filename)[0].lower()
                
                if filename not in table_mappings:
                    print(f"Mapeamento não encontrado para '{filename}', pulando...")
                    continue
                
                print(f"Migrando dados de '{filename}'...")
                
                with engine.connect() as connection:
                    # Abre uma transação que commita automaticamente:
                    # usa engine.begin() para garantir commit ao finalizar
                    with engine.begin() as connection_tx:
                        # Define a tabela com base em metadata já existente
                        table = Table(table_name, metadata, autoload_with=connection_tx)
                        
                        # Lê o arquivo CSV
                        try:
                            df = pd.read_csv(csv_file_path, delimiter=delimiter, encoding=encoding)
                            
                            # Aplica o mapeamento de colunas
                            column_mapping = table_mappings[filename]['column_mapping']
                            field_names = table_mappings[filename]['field_names']
                            
                            df = df.rename(columns=column_mapping)
                            
                            # Garante que todas as colunas esperadas existam
                            for field in field_names:
                                if field not in df.columns:
                                    df[field] = None
                            
                            # Remove colunas extras que não estão na tabela
                            df = df[field_names]
                            
                            # Trata valores de data se necessário
                            for col in df.columns:
                                if df[col].dtype == 'object':
                                    # Tenta detectar um formato entre padrões comuns e usar format explícito para evitar warnings
                                    try:
                                        sample = df[col].dropna().astype(str).head(100)
                                        if sample.empty:
                                            continue

                                        date_patterns = [
                                            '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d',
                                            '%d-%m-%Y', '%m-%d-%Y', '%Y%m%d'
                                        ]

                                        best_fmt = None
                                        best_count = 0
                                        for fmt in date_patterns:
                                            parsed = pd.to_datetime(sample, format=fmt, infer_datetime_format=False)
                                            count = parsed.notna().sum()
                                            if count > best_count:
                                                best_count = count
                                                best_fmt = fmt

                                        # Se encontramos um formato que parseou a maioria, usar format explícito (sem inferência)
                                        if best_fmt and best_count >= max(1, int(0.6 * len(sample))):
                                            df[col] = pd.to_datetime(df[col], format=best_fmt, infer_datetime_format=False)
                                        else:
                                            # Sem formato consistente: usar to_datetime sem inferência para evitar o UserWarning
                                            df[col] = pd.to_datetime(df[col], infer_datetime_format=False)
                                    except Exception:
                                        # Se tudo falhar, mantém a coluna original
                                        pass
                            
                            # Inserção de registros com barra de progresso
                            total_rows = len(df)
                            processed_rows = 0
                            
                            with tqdm(total=total_rows, desc=f"Migrando {filename}") as pbar:
                                for stmt in csv_to_sqlalchemy_insert(table, df, field_names):
                                    result = connection_tx.execute(stmt)
                                    batch_size = result.rowcount if result.rowcount is not None else 0
                                    processed_rows += batch_size
                                    pbar.update(batch_size)
                            
                            print(f"Dados de '{filename}' migrados com sucesso para a tabela '{table_name}' ({total_rows} registros).")
                            
                        except Exception as e:
                            with open(log_file, 'a') as f:
                                f.write(f"{datetime.now()}: Erro ao processar CSV '{filename}': {e}\n")
                            # print(f"Erro ao processar CSV '{filename}': {e}")
                        
    except SQLAlchemyError as e:
        # print(f"Erro ao migrar dados: {e}")
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now()}: {e}\n")
    except Exception as e:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now()}: {e}\n")

def parse_database_url(database_url):
    """
    Extrai informações da URL do banco de dados
    """
    # Formato: postgresql://user:password@host:port/database
    import re
    pattern = r'postgresql://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)'
    match = re.match(pattern, database_url)
    
    if match:
        return {
            'user': match.group(1),
            'password': match.group(2),
            'host': match.group(3),
            'port': match.group(4),
            'database': match.group(5)
        }
    else:
        raise ValueError("URL do banco de dados inválida")

def create_sql_backup(database_url, backup_directory='./backups'):

    try:
        subprocess.run(['pg_dump', '--version'], capture_output=True, text=True, check=True)
    except FileNotFoundError:
        print("❌ pg_dump não encontrado. Certifique-se de que o PostgreSQL está instalado e pg_dump está no PATH.")
        print("Para instalar: sudo apt install postgresql-client")
        return None
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao verificar pg_dump: {e.stderr}")
        return None

    try:
        # Cria diretório de backup se não existir
        os.makedirs(backup_directory, exist_ok=True)
        
        # Extrai informações da URL do banco
        db_info = parse_database_url(database_url)
        
        # Gera nome do arquivo de backup com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        database_name = db_info['database']
        backup_filename = f"{database_name}_backup_{timestamp}.sql"
        backup_path = os.path.join(backup_directory, backup_filename)
        
        # Monta comando pg_dump para formato SQL
        cmd = [
            'pg_dump',
            '-h', db_info['host'],
            '-p', db_info['port'],
            '-U', db_info['user'],
            '-d', db_info['database'],
            '-f', backup_path,
            '-v',  # Verbose
            '--no-password'  # Usa variável de ambiente para senha
        ]
        
        # Define variável de ambiente para senha
        env = os.environ.copy()
        env['PGPASSWORD'] = db_info['password']
        
        print("\n" + "="*60)
        print("🔄 INICIANDO BACKUP DO BANCO DE DADOS")
        print("="*60)
        print(f"📦 Banco: {database_name}")
        print(f"📄 Formato: SQL (.sql)")
        print(f"📂 Destino: {backup_path}")
        
        # Executa o comando
        result = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Verifica se o arquivo foi criado
        if os.path.isfile(backup_path):
            file_size = os.path.getsize(backup_path)
            file_size_mb = file_size / (1024 * 1024)
            
            print("\n" + "="*60)
            print("✅ BACKUP CRIADO COM SUCESSO")
            print("="*60)
            print(f"📁 Arquivo: {backup_path}")
            print(f"💾 Tamanho: {file_size_mb:.2f} MB")
            print(f"📍 Localização completa: {os.path.abspath(backup_path)}")
            
            print("\n" + "="*60)
            print("🔧 COMO RESTAURAR ESTE BACKUP")
            print("="*60)
            print(f"psql -h localhost -p 5432 -U postgres -d nome_do_banco -f '{backup_path}'")
            print("="*60)
            
            return backup_path
        else:
            raise Exception("Arquivo de backup não foi encontrado após execução")
        
    except subprocess.CalledProcessError as e:
        print("\n" + "="*60)
        print("❌ ERRO AO EXECUTAR PG_DUMP")
        print("="*60)
        print(f"Código de saída: {e.returncode}")
        print(f"Erro: {e.stderr}")
        return None
    except Exception as e:
        print(f"\n❌ Erro ao criar backup: {e}")
        return None

# Configurações
csv_directory = './csv'  # Altere para o diretório dos seus CSVs
database_name = input("Digite o nome do banco de dados PostgreSQL de destino: ")
database_url = f'postgresql://postgres:syncode123@localhost:5432/{database_name}'
backup_directory = './backups'  # Diretório para salvar backups

# Configurações opcionais para CSV
delimiter = ';'  # Pode ser ';' para CSVs brasileiros
encoding = 'latin1'  # Pode ser 'latin1' ou 'cp1252' se necessário

# Execução
if __name__ == "__main__":
    start_time = time.time()
    
    print("�� INICIANDO MIGRAÇÃO CSV PARA POSTGRESQL")
    print("="*60)
    
    print("\n📊 Criando tabelas...")
    table_mappings = create_tables_from_csvs(csv_directory, database_url, delimiter, encoding)
    
    print("\n📥 Migrando dados...")
    migrate_csv_to_postgresql(csv_directory, database_url, table_mappings, delimiter, encoding)
    
    migration_time = time.time()
    migration_duration = migration_time - start_time
    
    print(f"\n✅ Migração concluída em {migration_duration:.2f} segundos")
    
    # Criar backups
    successful_backups = create_sql_backup(database_url, backup_directory)

    successful_backups = []
    
    end_time = time.time()
    total_time = end_time - start_time
    backup_time = end_time - migration_time
    
    print("\n" + "="*60)
    print("📈 RELATÓRIO FINAL")
    print("="*60)
    print(f"⏱️  Tempo de migração: {migration_duration:.2f} segundos")
    print(f"⏱️  Tempo de backup: {backup_time:.2f} segundos")
    print(f"⏱️  Tempo total: {total_time:.2f} segundos")
    print(f"📦 Backups criados: {len(successful_backups)}")
    print("="*60)