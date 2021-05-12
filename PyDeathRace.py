from Clases import *
from funciones import load_sprite
import pygame
import ctypes
import os
import tkinter

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
        self.ancho, self.alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.pantalla = pygame.display.set_mode((self.ancho-5,self.alto-52))

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
        #pygame.draw.rect(self.pantalla, green, [150, 50, 400, 400], 0)

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
                #Para el evento del ratón al darle colick
               # if event.type == pygame.MOUSEBUTTONUP:
               #     if event.button != 1:
                #        continue
                #press = True

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.pantalla.fill(black)

        #Con esta linea podemos ver la imagen
        self.pantalla.blit(self.background, (450, 200))

        #Así se dibuja un rectangulo
        #self.rectangulo = pygame.draw.rect(self.pantalla, (255,255,255), [160, 50, 160, 40])
        #alto= 800
        #ancho = 1500
        x= 0
        y= 0
        #dependiendo del numero final se le quita el fondo (0) y solo bordes (1)
        #pygame.draw.rect(self.pantalla, green, [x, y, self.ancho, self.alto], 0)
        pygame.draw.rect(self.pantalla, white, [660, 430, 200, 100], 0)
        pygame.draw.rect(self.pantalla, white, [300, 175, 200, 100], 0)
        pygame.draw.rect(self.pantalla, white, [660, 175, 200, 100], 0)
        pygame.draw.rect(self.pantalla, white, [1020, 175, 200, 100], 0)
        pygame.draw.rect(self.pantalla, white, [300, 430, 200, 100], 0)
        pygame.draw.rect(self.pantalla, white, [1020, 430, 200, 100], 0)
        pygame.display.flip()