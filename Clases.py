
import pygame
import funciones
import os
import pygame as pg

from pygame.locals import *

#Mixer para los sonidos
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
#sonidos para el click
sound_volume = 2
click1 = pygame.mixer.Sound(os.path.join("sounds", "click1.wav"))
click1.set_volume(sound_volume)

#Para las cajas de Texto
darkred = (139, 0, 0)
crimson = (220, 20, 60)

#pg.init()
#screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = darkred
COLOR_ACTIVE = crimson
FONT = pygame.font.Font(None, 29)

#La clase para controlar el mouse y el cursor
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
            #click1.play()
        return cursor

    def coordenadas_cursor(self):
        """ Captura cordenadas del mouse """
        #print(pygame.mouse.get_pos())
        return pygame.mouse.get_pos()


    def coordenadas_ponteiro(self):
        """ Establece las cordenadas del puntero del mouse"""

        x, y = self.coordenadas_cursor()
        x -= self.imagem_cursor().get_width() - 5
        return x, y

    def altera_cursor(self):
        """ Muestra la imagen del mouse en estado normal """
        self.pantalla.blit(self.imagem_cursor(), self.coordenadas_ponteiro())

#Clase para que la imagen se vea del tamaño de la pantalla
class Image():
    def __init__(self, file: str, name: str, wh: tuple, pantalla, ventana):
        self.image = pygame.image.load(os.path.join(file, name))
        self.image = pygame.transform.scale(self.image, wh)
        self.rect = self.image.get_rect()
        self.brightness = 0
        self.pantalla = pantalla
        self.ventana =  ventana

    #Funcion para colocar las imagenes en un lugar espesifico de la pantalla
    def place(self, center: bool = False, xy: tuple = (0, 0)):
        if center:
            self.rect.center = self.ventana.center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

        self.pantalla.blit(self.image, self.rect)

class Text():
    def __init__(self, pantalla, ventana, font: str, size: int, color: tuple, text: str, background: tuple = None):
        self.pantalla = pantalla
        self.ventana = ventana
        self.size = size
        self.font = pygame.font.Font(os.path.join("fonts", f"{font}.ttf"), self.size)
        self.color = color
        self.text = text
        self.background = background
        self.image = self.font.render(self.text, False, self.color, self.background)
        self.rect = self.image.get_rect()

    #Funcion para colocar el texto en un lugar especifico de la pantalla
    def place(self, center: bool = False, xy: tuple = (0, 0)):
        if center:
            self.rect.center = self.ventana.center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

        self.pantalla.blit(self.image, self.rect)

    def render(self):
        self.image = self.font.render(self.text, True, self.color, self.background)
        self.rect = self.image.get_rect()

#Creamos la clase para las cajas de texto
class CajaText():

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    #Cuando se precione el cuandro
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Si se hace clic en el cuadro
            if self.rect.collidepoint(event.pos):
                # cuando esta activo
                self.active = not self.active
            else:
                self.active = False
            # cambia el color del cuandro caundo este inactivo.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # toma el texto.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # dependiendo de lo largo del texto hace el cuadro mas largo
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen, ventana, center: bool = False, xy: tuple = (0, 0)):
        if center:
            self.rect.center = ventana.center
            self.rect.x += xy[0]
            self.rect.y += xy[1]
        else:
            self.rect.x = xy[0]
            self.rect.y = xy[1]

        # Pone el texto.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        #  Pone el rectangulo.
        pg.draw.rect(screen, self.color, self.rect, 2)