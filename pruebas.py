import funciones

import pygame
import ctypes
import os
import sys
from pygame.locals import *
import tkinter

#Mixer para los sonidos
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pantalla = pygame.display.set_mode((ancho-30,alto-55))
window_rect = pantalla.get_rect()

pygame.display.set_caption("Example")

fps = pygame.time.Clock()



# colors
white = (255, 255, 255)
black = (0, 0, 0)

# sonidos para el click
sound_volume = 1
click1 = pygame.mixer.Sound(os.path.join("sounds", "click1.wav"))
click1.set_volume(sound_volume)

#Clase para crear ul cursos
class Mouse():

    def __init__(self):
        """ Constructor """
        pygame.mouse.set_visible(0)
        self.imgens_cursor = funciones.cargar_imagem('cursor.png', 1, [(0, y, 40, 43) \
                                                                      for y in [0, 43]])
    def imagem_cursor(self):
        """ Cambia la imagen cuando hago click """
        cursor = self.imgens_cursor[0]

        if event.type == MOUSEBUTTONDOWN:
            #Se usa la imagen que esta en la posicion 1 del arreglo
            cursor = self.imgens_cursor[1]
            #Par aque suene al hacer Click
            click1.play()
        return cursor

    def coordenadas_cursor(self):
        """ Captura cordenadas del mouse """
        return pygame.mouse.get_pos()

    def coordenadas_ponteiro(self):
        """ Exatablece las cordenadas del puntero del mouse"""

        x, y = self.coordenadas_cursor()
        x -= self.imagem_cursor().get_width() - 5
        return x, y

    def altera_cursor(self):
        """ Muestra la imagen del mouse en estado normal """
        pantalla.blit(self.imagem_cursor(), self.coordenadas_ponteiro())

class Image:
    def __init__(self, name: str, wh: tuple):
        self.image = pygame.image.load(os.path.join("img", name))
        self.image = pygame.transform.scale(self.image, wh)
        self.rect = self.image.get_rect()
        self.brightness = 0

    def place(self, center: bool = False, xy: tuple = (0, 0)):
        if center:
            self.rect.center = window_rect.center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

        pantalla.blit(self.image, self.rect)


#Fondo de pantalla
main_background = Image("main.jpg", (ancho, alto))

mouse = Mouse()
# game loop
while True:

    # events
    for event in pygame.event.get():  # quit event
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


    fps.tick(60)
    pantalla.fill(black)
    main_background.place()


    # mouse
    mouse.altera_cursor()

    # update screen
    pygame.display.update()
