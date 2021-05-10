from pygame.image import load

import os
import pygame

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


