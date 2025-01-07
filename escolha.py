class Escolha:
    def __init__(self, descricao, proxima_cena, condicao=None, pontuacao=0):
        self.descricao = descricao
        self.proxima_cena = proxima_cena
        self.condicao = condicao
        self.pontuacao = pontuacao

    def __str__(self):
        return self.descricao

    def exibir_escolhas(self):
        if self.escolhas:
            print("\nEscolhas:")
            for i, escolha in enumerate(self.escolhas, 1):  # Usando '1' para começar de 1, para exibição no formato "1. ..."
                print(f"{i}. {escolha.descricao}")
        else:
            print("Sem escolhas disponíveis nesta cena.")

        print("\nEscolha uma opção (1, 2, 3...):")

    def realizar(self):
        print(f"\nVocê escolheu: {self.descricao}")
        return self.proxima_cena
