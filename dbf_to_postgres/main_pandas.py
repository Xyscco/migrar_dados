import os
import time
import pandas as pd
from dbfread import DBF
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from tqdm import tqdm

def get_unique_column_names(dbf_table):
    """
    Cria uma lista de nomes de colunas únicos e em minúsculo,
    adicionando um sufixo numérico para nomes duplicados.
    """
    new_names = []
    name_counts = {}
    
    for field in dbf_table.fields:
        col_name = field.name.lower()
        
        if col_name in name_counts:
            name_counts[col_name] += 1
            new_name = f"{col_name}_{name_counts[col_name] - 1}"
        else:
            name_counts[col_name] = 1
            new_name = col_name
        
        while new_name in new_names:
            name_counts[col_name] += 1
            new_name = f"{col_name}_{name_counts[col_name] - 1}"

        new_names.append(new_name)
        
    return new_names

def migrate_dbf_to_postgresql_with_pandas(dbf_directory, database_url):
    """
    Lê arquivos DBF, os carrega em DataFrames do Pandas e os insere no PostgreSQL.
    Cria a tabela mesmo que o arquivo DBF esteja vazio.
    """
    try:
        engine = create_engine(database_url)
        dbf_files = [f for f in os.listdir(dbf_directory) if f.lower().endswith('.dbf')]

        for filename in tqdm(dbf_files, desc="Migrando arquivos DBF"):
            dbf_file_path = os.path.join(dbf_directory, filename)
            table_name = os.path.splitext(filename)[0].lower()

            try:
                dbf_table = DBF(dbf_file_path, ignore_missing_memofile=True, encoding='latin1')
                
                # --- LÓGICA CORRIGIDA PARA EVITAR VALORES NULL ---

                # 1. Crie o DataFrame a partir do DBF. Neste ponto, as colunas estarão em MAIÚSCULO.
                df = pd.DataFrame(iter(dbf_table))

                # Pega a lista de nomes de colunas já tratados (minúsculos e únicos)
                final_column_names = get_unique_column_names(dbf_table)

                # 2. Verifique se o DataFrame tem dados para renomear as colunas.
                if not df.empty:
                    # Se há dados, renomeie as colunas existentes.
                    df.columns = final_column_names
                else:
                    # Se estiver vazio, crie um novo DataFrame vazio, mas com as colunas corretas.
                    # Isso garante que a tabela seja criada com a estrutura certa no banco.
                    df = pd.DataFrame(columns=final_column_names)

                # 3. Execute o to_sql.
                df.to_sql(
                    table_name,
                    con=engine,
                    if_exists='replace',
                    index=False,
                    chunksize=10000
                )

                if len(df) == 0:
                    print(f"Arquivo '{filename}' vazio. Tabela '{table_name}' criada com sucesso (sem dados).")
                else:
                    print(f"Dados de '{filename}' ({len(df)} linhas) migrados com sucesso para a tabela '{table_name}'.")

            except Exception as e:
                print(f"Erro ao processar o arquivo '{filename}': {e}")

    except SQLAlchemyError as e:
        print(f"Erro de conexão com o banco de dados: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Bloco de Execução ---
if __name__ == "__main__":
    dbf_directory = './dbf'
    database_url = 'postgresql://postgres:syncode123@localhost:5432/conv_601_RUY_SILVA_SANTANA_LTDA'

    print("Iniciando a migração de dados com Pandas...")
    start_time = time.time()
    
    migrate_dbf_to_postgresql_with_pandas(dbf_directory, database_url)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("\nMigração concluída.")
    print(f"Tempo total de execução: {total_time:.2f} segundos")