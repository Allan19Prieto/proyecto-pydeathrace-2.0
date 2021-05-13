
from Clases import *
from funciones import muestra_texto
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
# Parametros del puntaje
consolas = pygame.font.match_font("consolas")
puntuacion = 0
red = (255, 0, 0)

class pydeathrace:
    def __init__(self):
        self._init_pygame()

        # Nos permite obtener el tamaño de la pantalla completa
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        #self.ancho, self.alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.ancho = 1361
        self.alto = 716
        self.pantalla = pygame.display.set_mode((self.ancho , self.alto ))
        self.window_rect = self.pantalla.get_rect()

        # Vaviables para los fondos de pantalla
        self.fondo_inicio = Image("Fondo.png", (self.ancho, self.alto), self.pantalla, self.window_rect)

        # Fondo de pantalla que se colocara
        self.imagen_inicio = self.fondo_inicio

        self.title_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, "Menu Principal", purple)

        self.puntaje = muestra_texto(self.pantalla,consolas,str (puntuacion),red, 40, 700,50)


        # tocar musica inicial
        pygame.mixer.music.load("sounds/Battlefield.mp3")
        pygame.mixer.music.play(1)

    # Este es el bucle de nuestro juego
    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    # El init pygame es siempre necesario al inicio de un guego qcon pygame
    def _init_pygame(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.init()


        #Nombre y icono
        pygame.display.set_caption("PyDeathRace 2.0")
        pygame.display.set_icon(pygame.image.load(os.path.join("img/icon.png")))


    # Para manejar las entradas
    def _handle_input(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT or (
                    self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE
            ):
                quit()

            #Aqui Añadiremos la logica que va a tener el juego

    # Par amanejar la logica del juego
    def _process_game_logic(self):
        #Se llama el Mpuse
        self.mouse1 = Mouse(self.pantalla, self.event)



    # Par adibujar en la pantalla por fotogramas y qeu esta se actualice cada sierto tiempo
    def _draw(self):
        self.pantalla.fill(black)

        #Con esta linea podemos ver la imagen de fondo
        self.imagen_inicio.place()



        self.title_text.place(True, (25, -300))

        self.puntaje

        # Colocamos en mouse en la pantalla
        self.mouse1.altera_cursor()
        print(self.ancho, self.alto)


        # update screen
        pygame.display.update()
        pygame.display.flip()

