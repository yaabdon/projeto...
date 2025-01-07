import json
from packages.models.episodio import Episodio
from packages.models.cena import Cena
from packages.models.dialogo import Dialogo
from packages.models.escolha import Escolha
from shapes.viewers.decorando_terminal import DecorandoTerminal
from assets.sounds.audio import Audio

def carregar_episodios(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)
    return dados['episodios']

def iniciar_episodio(episodio):
    print(f"\033[32mIniciando o Episódio {episodio['numero']}: {episodio['nome']}!\n\033[0m")
    Audio.tocar_som("assets/sounds/efeito_som.wav")
    cenas = []
    for cena_data in episodio["cenas"]: #criação de objetos armazenados em cenas
        dialogos = [Dialogo(d["personagem"], d["mensagem"], d.get("condicao")) for d in cena_data["dialogos"]]
        escolhas = [
            Escolha(
                e["descricao"], 
                e["proxima_cena"], 
                e.get("condicao"),
                e.get("pontuacao", 0) #tem que adicionar o 0
                ) 
                for e in cena_data["escolhas"]
            ]
        cena = Cena(cena_data["descricao"], dialogos, escolhas)
        cenas.append(cena)


    cena_atual = cenas[0]
    escolha_anterior = None

    
    Audio.tocar_musica("assets/sounds/musica_fundo.mp3")
    while cena_atual:

        cena_atual.exibir_descricao()
        cena_atual.exibir_dialogos(escolha_anterior)
        cena_atual.exibir_escolhas()

        try:
            numero_da_escolha = int(input("\033[32mEscolha uma opção:\n\033[0m"))
        except ValueError:
            print("\033[31mEscolha inválida. Tente novamente.\033[0m")
            continue

        if numero_da_escolha < 1 or numero_da_escolha > len(cena_atual.escolhas):
            print("\033[31mEscolha inválida. Tente novamente.\033[0m")
            continue

        DecorandoTerminal.limpar_terminal()
        escolha = cena_atual.escolhas[numero_da_escolha - 1]
        proxima_cena = escolha.proxima_cena
        if proxima_cena is not None and 0 <= proxima_cena < len(cenas):
            cena_atual = cenas[proxima_cena]
            escolha_anterior = numero_da_escolha  # Atualiza a escolha anterior
        else:
            print("\033[31mParabéns! Você chegou ao final do episódio!.\n\033[0m")
            Audio.parar_musica()
            break 


""""
Arquivo mais complexo de todo o jogo


Não é necessária essa função, pois eu crio os episódios todos pelo próprio arquivo JSON,
manualmente consigo acompanhar a história como se escrevesse um livro, mas futuramente, talvez
seja mais fácil ter uma função que receba os dados do terminal e complete no arquivo JSON por conta
própria...

def criar_episodio(episodio_data):
    return episodio"""