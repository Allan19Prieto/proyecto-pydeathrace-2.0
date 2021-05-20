from Clases import *
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

def main(pantalla):

    ancho = 1361
    alto = 716
    #pantalla = pygame.display.set_mode((ancho, alto))
    window_rect = pantalla.get_rect()

    pista = Image("img", "Pista1.jpg", (ancho, alto), pantalla, window_rect)



    while True:


        #Parte logica
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()


        #Parte de dibujo
        pantalla.fill((0, 0, 0))
        pista.place()

        pygame.display.flip()
        pygame.display.update()
