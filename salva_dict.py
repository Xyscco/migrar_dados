import json

def salvar_dicionario_como_arquivo_python(arquivo_json, arquivo_python):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    with open(arquivo_python, 'w') as file:
        file.write("dados = ")
        file.write(json.dumps(dados, indent=4, ensure_ascii=False))

def main():
    arquivo_json = 'config.json'
    arquivo_python = 'dados_migracao.py'
    
    salvar_dicionario_como_arquivo_python(arquivo_json, arquivo_python)
    print(f"Dados foram salvos em {arquivo_python}.")

if __name__ == "__main__":
    main()