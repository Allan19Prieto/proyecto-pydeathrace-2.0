
from Clases import *

import pygame
import ctypes
import os

#Algunos colores
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

        # Nos permite obtener el tamaño de la pantalla completa
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        self.ancho, self.alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.pantalla = pygame.display.set_mode((self.ancho - 5, self.alto - 52))
        self.window_rect = self.pantalla.get_rect()

        # Vaviables para los fondos de pantalla
        self.fondo_inicio = Image("Fondo.png", (self.ancho, self.alto), self.pantalla, self.window_rect)

        # Fondo de pantalla que se colocara
        self.imagen_inicio = self.fondo_inicio


        # tocar musica inicial
        pygame.mixer.music.load("sounds/Battlefield.mp3")
        pygame.mixer.music.play(1)

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        #Nombre y icono
        pygame.display.set_caption("PyDeathRace 2.0")
        pygame.display.set_icon(pygame.image.load(os.path.join("img/icon.png")))

        # Mixer para los sonidos
        #pygame.mixer.pre_init(44100, -16, 2, 2048)
        #pygame.mixer.init()

    def _handle_input(self):

        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT or (
                    self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE
            ):
                quit()


    def _process_game_logic(self):
        #Se llama el Mpuse
        self.mouse1 = Mouse(self.pantalla, self.event)

    def _draw(self):
        self.pantalla.fill(black)

        #Con esta linea podemos ver la imagen de fondo
        self.imagen_inicio.place()

        #Colocamos en mouse en la pantalla
        self.mouse1.altera_cursor()


        # update screen
        pygame.display.update()
        pygame.display.flip()

