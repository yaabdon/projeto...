import pygame

pygame.init()
pygame.mixer.init()
audio_disponivel = True

class Audio:
    @staticmethod
    def tocar_som(caminho_arquivo):
        if audio_disponivel:
            som = pygame.mixer.Sound(caminho_arquivo)
            som.play()
        else:
            print("Áudio não disponível para tocar som.")

    @staticmethod
    def tocar_musica(caminho_arquivo):
        if audio_disponivel:
            pygame.mixer.music.load(caminho_arquivo)
            pygame.mixer.music.play(-1)  # -1 para loop infinito
        else:
            print("Áudio não disponível para tocar música.")

    @staticmethod
    def parar_musica():
        if audio_disponivel:
            pygame.mixer.music.stop()
        else:
            print("Áudio não disponível para parar música.")

