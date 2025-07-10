import fdb
import json
from dados_migracao import dados

config = dados

def conectar_ao_banco(arquivo_banco, usuario = 'SYSDBA', senha = 'masterkey'):
    return fdb.connect(dsn=arquivo_banco, user=usuario, password=senha, fb_library_name='./fbclient.dll')

def obter_campos_tabela(cursor, nome_tabela):
    cursor.execute(f"SELECT RDB$FIELD_NAME FROM RDB$RELATION_FIELDS WHERE RDB$RELATION_NAME='{nome_tabela}'")
    campos = [campo[0].strip() for campo in cursor.fetchall()]
    return campos

def migrar_dados(config, conexao_origem, conexao_destino):
    cursor_origem = conexao_origem.cursor()
    cursor_destino = conexao_destino.cursor()

    for tabela in config:
        nome_tabela = tabela['NomeTabela']
        where_sql = tabela['WhereSQL']
        generator = tabela['Generator']
        generator_field = tabela['GeneratorField']
        campos_formatados = tabela['CamposFormatados']

        # Obtenha todos os campos da tabela
        campos_tabela = obter_campos_tabela(cursor_origem, nome_tabela)
        
        # Aplicar formatação aos campos
        campos_select = []
        for campo in campos_tabela:
            # Verifica se o campo precisa de formatação personalizada
            formatado = next((formato[campo] for formato in campos_formatados if campo in formato), campo)
            campos_select.append(f"{formatado} AS {campo}")
        
        query = f"SELECT {', '.join(campos_select)} FROM {nome_tabela} WHERE {where_sql}"
        print(query)
        # cursor_origem.execute(query)
        
        # for row in cursor_origem:
        #     campos = ', '.join(row.keys())
        #     valores = ', '.join([f"'{str(valor)}'" for valor in row])
            
        #     insert_query = f"INSERT INTO {nome_tabela} ({campos}) VALUES ({valores})"
        #     cursor_destino.execute(insert_query)
        
        # # Opcional: atualizar gerador
        # generator_query = f"SELECT GEN_ID({generator}, 1) FROM RDB$DATABASE"
        # cursor_destino.execute(generator_query)
        
    conexao_destino.commit()


def main():
    conexao_origem = conectar_ao_banco('origem.fdb')
    conexao_destino = conectar_ao_banco('destino.fdb')
    
    try:
        migrar_dados(config, conexao_origem, conexao_destino)
        
    finally:
        conexao_origem.close()
        conexao_destino.close()

# if __name__ == "__main__":
main()