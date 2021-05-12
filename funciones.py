from pygame.image import load

import os
import pygame
from pygame.locals import *

#Crea un ruta a un imagen, que esté en assets/sprites
def load_sprite(name, with_alpha=True):
    #arquivo = os.path.join('img', arquivo)
    path = f"C:/Users/joset/PycharmProjects/proyecto-pydeathrace-2.0/img/{name}.jpg"
    #Carga la imagen usando load
    loaded_sprite = load(path)

    #Convierte la imagena un formato que se adapte mejor a la pantalla
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def cargar_imagem(arquivo, transparencia=None, imagens=None):

    arquivo = os.path.join('img', arquivo)
    image = pygame.image.load(arquivo)

    if imagens is None:
        if transparencia == 1:
            return image.convert_alpha()

        return image.convert()
    else:
        imgs = []
        for img_area in imagens:
            img = pygame.Surface(Rect(img_area).size).convert()
            img.blit(image, (0, 0), img_area)
            if transparencia == 1:
                colorkey = img.get_at((0, 0))
                img.set_colorkey(colorkey, RLEACCEL)
            imgs.append(img)
        return imgs

