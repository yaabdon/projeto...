import os
from shapes.viewers.decorando_terminal import DecorandoTerminal
from packages.models.usuario import Usuario
from packages.controllers.menu import Menu
from packages.controllers.controller_episodio import carregar_episodios
from assets.sounds.audio import Audio

def main():
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    caminho_episodios = os.path.join(caminho_base, "packages", "data", "episodios", "episodios.json")
    caminho_personagens = os.path.join(caminho_base, "packages", "data", "personagens", "personagens.json")

    decorando = DecorandoTerminal()
    decorando.limpar_terminal()
    decorando.exibir_titulo("Iniciando o Jogo!")
    decorando.press_enter()
    decorando.limpar_terminal()

    decorando.exibir_titulo("Login")
    escolha = input("Deseja (1) Criar uma conta ou (2) Fazer login?\nEscolha entre 1 ou 2: ")
    decorando.press_enter()
    decorando.limpar_terminal()

    if escolha == '1':
        decorando.exibir_titulo("Criando Sua Conta")
        usuario_logado = Usuario.criar_conta()
    elif escolha == '2':
        decorando.exibir_titulo("Realizando Login")
        usuario_logado = Usuario.login()
    else:
        print("Opção inválida. O jogo será encerrado.")
        return

    # Checa se o login ou a criação de conta foi bem-sucedida
    if not usuario_logado:
        print("Ocorreu um erro ao iniciar o usuário. O jogo será encerrado.")
        return

    # Mensagem de boas-vindas
    decorando.exibir_titulo("Iniciando a Aventura...")
    decorando.exibir_texto(
        f"\nBem-vindo ao Contos em Branco, {usuario_logado.nome_usuario}!",
        cor='rosa', fundo='branco'
    )
    decorando.press_enter()

    # Carrega os episódios e personagens
    episodios = carregar_episodios(caminho_episodios)

    # Inicializa o Menu com o usuário logado
    menu = Menu(episodios=caminho_episodios, personagens=caminho_personagens, usuario=usuario_logado)
    menu.escolher_menu()  # Chama o menu principal


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()

"""
AQUI É O ÚNICO ARQUIVO COM EXPLICAÇÃO ANTES DO CÓDIGO, OUTROS
ARQUIVOS .PY TEM A EXPLICAÇÃO DA IMPLEMENTAÇÃO E GUIA, ALÉM DE
SUGESTÕES FUTURAS PARA EXECUÇÃO E EVOLUÇÃO 
"""
