"""
NESSE CÓDIGO ORGANIZAMOS A ESTRUTURA DO EPISÓDIO A PARTIR DE:
CENA
ESCOLHAS
DIÁLGOS
"""

from packages.models.cena import Cena

class Episodio:
    def __init__(self, nome, numero, cenas, status="Iniciado"):
        self.nome = nome
        self.numero = numero
        self.cenas = cenas  

    def exibir_nome_e_numero_episodio(self):
        print(f"\n{self.nome}")
        print(f"Número do episódio: {self.numero}")

    def iniciar_episodio(self, controller):
        controller.iniciar_episodio(self)
        
