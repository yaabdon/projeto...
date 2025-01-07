import pygame
pygame.init()
pygame.mixer.init()

class Audio:
    @staticmethod
    def tocar_som(caminho_arquivo):
        pygame.mixer.Sound(caminho_arquivo).play()

    @staticmethod
    def tocar_musica(caminho_arquivo):
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play(-1)  # -1 para loop infinito

    @staticmethod
    def parar_musica():
        pygame.mixer.music.stop()
