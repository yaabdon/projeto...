from shapes.viewers.decorando_terminal import DecorandoTerminal
from packages.controllers.tutorial import Tutorial
from packages.controllers.controller_episodio import iniciar_episodio
from packages.controllers.controller_episodio import carregar_episodios
from packages.controllers.controller_personagens import carregar_personagens
from assets.sounds.audio import Audio

class Menu:
    def __init__(self, tutorial=Tutorial(), episodios='packages/data/episodios.json', personagens='packages/data/personagens.json', usuario=None):
        self.tutorial = tutorial
        self.personagens = carregar_personagens(personagens)
        self.episodios = carregar_episodios(episodios)
        self.decorando = DecorandoTerminal()
        self.usuario = usuario  # Atributo usuário agora contém o usuário logado

    def exibir_menu(self):
        self.decorando.limpar_terminal()
        self.decorando.exibir_titulo("Menu Principal")
        Audio.tocar_som("assets/sounds/efeito_som.wav")
        print("\033[35m1.\033[0m Tutorial")
        print("\033[36m2.\033[0m Episódios")
        print("\033[33m3.\033[0m Personagens")
        print("\033[31m4.\033[0m Sair")
        self.decorando.exibir_espaco()

    def escolher_menu(self):
        while True:
            self.exibir_menu()
            escolha = input("\033[37mEscolha uma opção (1-4): \033[0m")
            if escolha == '1':
                self.exibir_tutorial()
            elif escolha == '2':
                self.escolher_episodio()
            elif escolha == '3':
                self.exibir_personagens()
            elif escolha == '4':
                print("\033[31mSaindo do jogo. Até a próxima!\033[0m")
                return  # Sai do loop principal
            else:
                print("\033[33mOpção inválida. Tente novamente.\033[0m")

    def exibir_tutorial(self):
        self.tutorial.exibir_tutorial()
        self.retornar_menu()

    def exibir_personagens(self):
        self.decorando.limpar_terminal()
        self.decorando.exibir_titulo("Personagens")

        if self.personagens:
            for personagem in self.personagens:
                # Exibindo as informações dos personagens em amarelo
                print(f"\033[35mNome: {personagem['nome']}\033[0m")
                print(f"\033[35mDescrição: {personagem['descricao']}\033[0m")
                print(f"\033[35mIdade: {personagem['idade']}\033[0m")
                print("\033\n[97m********************\n\033[0m")
        else:
            print("\033[33mNenhum personagem encontrado.\033[0m")

        self.retornar_menu()

    def escolher_episodio(self):
        self.decorando.limpar_terminal()
        self.decorando.exibir_titulo("Escolher Episódio")

        for i, episodio in enumerate(self.episodios, 1):
            print(f"\033[36m{i}.\033[0m {episodio.get('nome', 'Episódio sem nome')} (Episódio {episodio.get('numero', 'N/A')})")
       
        try:
            escolha = int(input("\033[36mEscolha um episódio (1-{}): \033[0m".format(len(self.episodios))))
            if 1 <= escolha <= len(self.episodios):
                episodio_selecionado = self.episodios[escolha - 1]
                self.decorando.limpar_terminal()
                iniciar_episodio(episodio_selecionado)
            else:
                print("\033[33mOpção inválida. Tente novamente.\033[0m")
        except ValueError:
            print("\033[33mPor favor, insira um número válido.\033[0m")
        self.retornar_menu()

    def retornar_menu(self):
        input("\033[37mPressione qualquer tecla para retornar ao menu...\033[0m")
