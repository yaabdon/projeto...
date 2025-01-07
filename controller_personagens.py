import json

def carregar_personagens(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)["personagens"]
    except FileNotFoundError:
        print("\033[31mErro: Arquivo de personagens não encontrado.\033[0m")
        return []