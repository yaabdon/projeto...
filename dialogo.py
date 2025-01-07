class Dialogo:
    def __init__(self, personagem, mensagem, condicao=None):
        self.personagem = personagem
        self.mensagem = mensagem
        self.condicao = condicao

    def str(self):
        return f"{self.personagem}: {self.mensagem}"