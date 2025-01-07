import textwrap
from packages.models.dialogo import Dialogo
from packages.models.escolha import Escolha

class Cena:
    def __init__(self, descricao, dialogos=None, escolhas=None, status="Em progresso"):
        self.descricao = descricao
        self.dialogos = dialogos if dialogos else []
        self.escolhas = escolhas if escolhas else []
        self.status = status  # Status da cena (Iniciado, Em progresso, Concluído)

    def exibir_descricao(self):
        print(self.descricao)

    def exibir_dialogos(self, escolha_anterior=None):
        for dialogo in self.dialogos:
            if dialogo.condicao is None or dialogo.condicao == escolha_anterior:
                wrapped_text = textwrap.fill(f"{dialogo.personagem}: {dialogo.mensagem}", width=80)
                print(wrapped_text)
                print()  # Linha em branco após o diálogo

    def exibir_escolhas(self):
        if self.escolhas:
            print("\033[32m\nEscolhas:\033[0m")
            for i, escolha in enumerate(self.escolhas, 1):
                print(f"{i}. {escolha.descricao}")
                print("\n")
        else: 
            return False

    """def realizar_escolha(self, numero_da_escolha):
        if not self.escolhas:  # Se não houver escolhas
            if numero_da_escolha == 1:  # O jogador escolheu "Continuar"
                self.atualizar_status("Concluída")  # Atualiza o status da cena
                return True  
            else:
                print("Escolha inválida.")
                return None  # Caso uma escolha inválida seja feita
        elif 1 <= numero_da_escolha <= len(self.escolhas):
            escolha = self.escolhas[numero_da_escolha - 1]
            self.atualizar_status("Concluída")  # Marca a cena como concluída após a escolha
            print(f"Proxima cena após escolha: {escolha.proxima_cena}")
            return escolha.proxima_cena  # Retorna a próxima cena, que deve ser uma referência para o avanço
        else:
            print("Escolha inválida")
            return None"""

    """def atualizar_status(self, novo_status):
        self.status = novo_status"""