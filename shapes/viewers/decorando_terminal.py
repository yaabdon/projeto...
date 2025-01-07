import os

class DecorandoTerminal:

    @staticmethod
    def limpar_terminal():
        os.system('clear' if os.name == 'posix' else 'cls')
      
    def exibir_titulo(self, titulo):
        print(f"\n\033[35m\033[47m{'*' * 40}\n{titulo.center(40)}\n{'*' * 40}\033[0m\n")

    def exibir_texto(self, mensagem, cor='rosa', fundo='branco'):
        cores = {
            'rosa': '\033[35m',
            'vermelho': '\033[31m',
            'reset': '\033[0m', 
        }

        fundos = {
            'branco': '\033[47m',
            'preto': '\033[40m',
            'reset': '\033[0m', 
        }

        cor_escolhida = cores.get(cor, cores['reset'])  
        fundo_escolhido = fundos.get(fundo, fundos['reset'])  
        print(f"{cor_escolhida}{fundo_escolhido}{mensagem}\033[0m")  # \033[0m reseta a cor

    
    def exibir_espaco(self):
        print(" " * 40) #se usei essa função, já não me lembro ondeKKKK

    def press_enter(self):
        input("\nPressione Enter para continuar...") #função exclusiva da recepção do jogo

    def criar_paragrafo(self, texto, largura=40):
        import textwrap
        return "\n".join(textwrap.wrap(texto, largura))