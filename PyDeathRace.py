from Clases import *
from funciones import load_sprite
import pygame
import ctypes
import os

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
celeste = (0, 255, 255)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

class pydeathrace:
    def __init__(self):
        self._init_pygame()

        #Nos permite obtener el tamaño de la pantalla completa
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.pantalla = pygame.display.set_mode((ancho,alto))

        #Añadimos el fondo de pantalla
        self.background = load_sprite("main", False)

        #Nombre y icono
        pygame.display.set_caption("PyDeathRace 2.0")
        pygame.display.set_icon(pygame.image.load(os.path.join("img/icon.png")))


        # tocar musica inicial
        #pygame.mixer.music.load("sounds/menu.wav")
        #pygame.mixer.music.play(-1)


    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.pantalla.fill(black)

        #Con esta linea podemos ver la imagen
        self.pantalla.blit(self.background, (450, 200))

        #Así se dibuja un rectangulo
        #self.rectangulo = pygame.draw.rect(self.pantalla, (255,255,255), [160, 50, 160, 40])


        pygame.display.flip()