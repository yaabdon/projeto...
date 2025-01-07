from shapes.viewers.decorando_terminal import DecorandoTerminal

class Tutorial:
    def __init__(self):
        self.decorando = DecorandoTerminal()
        

    def exibir_tutorial(self):
        self.decorando.limpar_terminal()
        self.decorando.exibir_titulo("Tutorial")
        print("\033[35mBem-vindo ao tutorial do jogo!\n\033[0m")
        

        texto_tutorial = (
             "Após o início do episódio escolhido, você encontrará uma ou mais opções. "
        "Escolha suas opções com sabedoria para progredir e talvez encontrar as respostas que procura."
        )
        texto_formatado = self.decorando.criar_paragrafo(texto_tutorial)
        print(f"\033[35m{texto_formatado}\033[0m\n")