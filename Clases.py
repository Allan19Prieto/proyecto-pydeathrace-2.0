
import pygame
import funciones
import os

from pygame.locals import *

#Mixer para los sonidos
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
# sonidos para el click
sound_volume = 2
click1 = pygame.mixer.Sound(os.path.join("sounds", "click1.wav"))
click1.set_volume(sound_volume)

#La clase para controlar el mouase y el cursoss
class Mouse():
    def __init__(self, pantalla, event):
        """ Constructor """
        self.pantalla = pantalla
        self.event = event
        pygame.mouse.set_visible(0)
        self.imgens_cursor = funciones.cargar_imagem('cursor.png', 1, [(0, y, 40, 43) \
                                                                      for y in [0, 43]])
    def imagem_cursor(self):
        """ Cambia la imagen cuando hago click """
        cursor = self.imgens_cursor[0]

        if self.event.type == MOUSEBUTTONDOWN:
            #Se usa la imagen que esta en la posicion 1 del arreglo
            cursor = self.imgens_cursor[1]
            #Par aque suene al hacer Click
            click1.play()
        return cursor

    def coordenadas_cursor(self):
        """ Captura cordenadas del mouse """
        #print(pygame.mouse.get_pos())
        return pygame.mouse.get_pos()


    def coordenadas_ponteiro(self):
        """ Exatablece las cordenadas del puntero del mouse"""

        x, y = self.coordenadas_cursor()
        x -= self.imagem_cursor().get_width() - 5
        return x, y

    def altera_cursor(self):
        """ Muestra la imagen del mouse en estado normal """
        self.pantalla.blit(self.imagem_cursor(), self.coordenadas_ponteiro())

#Clase para que la imagen se vea del tamaño de la pantalla
class Image():
    def __init__(self, name: str, wh: tuple,pantalla, ventana):
        self.image = pygame.image.load(os.path.join("img", name))
        self.image = pygame.transform.scale(self.image, wh)
        self.rect = self.image.get_rect()
        self.brightness = 0
        self.pantalla = pantalla
        self.ventana =  ventana

    def place(self, center: bool = False, xy: tuple = (0, 0)):
        if center:
            self.rect.center = self.ventana.center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

        self.pantalla.blit(self.image, self.rect)
