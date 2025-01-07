import pygame
import os

# Configurar backend de áudio para "dummy" no caso de ambientes sem áudio
os.environ["SDL_AUDIODRIVER"] = "dummy"

try:
    pygame.init()
    pygame.mixer.init()
    audio_disponivel = True
except pygame.error as e:
    print(f"Áudio desativado: {e}")
    audio_disponivel = False

class Audio:
    @staticmethod
    def tocar_som(caminho_arquivo):
        if audio_disponivel:
            try:
                som = pygame.mixer.Sound(caminho_arquivo)
                som.play()
            except pygame.error as e:
                print(f"Erro ao tocar som: {e}")
        else:
            print("Áudio não disponível para tocar som.")

    @staticmethod
    def tocar_musica(caminho_arquivo):
        if audio_disponivel:
            try:
                pygame.mixer.music.load(caminho_arquivo)
                pygame.mixer.music.play(-1)  # -1 para loop infinito
            except pygame.error as e:
                print(f"Erro ao tocar música: {e}")
        else:
            print("Áudio não disponível para tocar música.")

    @staticmethod
    def parar_musica():
        if audio_disponivel:
            try:
                pygame.mixer.music.stop()
            except pygame.error as e:
                print(f"Erro ao parar música: {e}")
        else:
            print("Áudio não disponível para parar música.")
