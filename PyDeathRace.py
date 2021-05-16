
from Clases import *
import pygame
import ctypes
import os

#Colores
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
        #self.ancho, self.alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.ancho = 1361
        self.alto = 716
        self.pantalla = pygame.display.set_mode((self.ancho , self.alto ))
        self.window_rect = self.pantalla.get_rect()

        # Para que el juego se ejecute siempre en unas FPS establecidas
        self.clock = pygame.time.Clock()

        #Variable para el menu
        self.menu = "inicio"

        #Ejemplo para los puntos
        self.puntos = 0
        #self.p = puntos

        # Fondos de pantalla
        self.fondo_inicio = Image("img", "FondoPrincipal.png", (self.ancho+200, self.alto+200), self.pantalla, self.window_rect)
        self.fondo_menu = Image("img", "Fondo2.png", (self.ancho, self.alto), self.pantalla, self.window_rect)

        # Sound
        self.menu_musica = pygame.mixer.Sound(os.path.join("sounds", "Battlefield.mp3"))
        self.click2_sound = pygame.mixer.Sound(os.path.join("sounds", "click2.wav"))

        # Pantalla Inicio
        self.title_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, "Menu Principal", purple)
        self.play_button = Image("button", "Play.png", (180, 115), self.pantalla, self.window_rect)
        self.about_button = Image("button", "Info.png", (180, 115), self.pantalla, self.window_rect)




        # Fondo de pantalla que se colocara
        #self.imagen_inicio = self.fondo_inicio

        # tocar musica inicial
        #pygame.mixer.music.load("sounds/Battlefield.mp3")
        #pygame.mixer.music.play(1)

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
        self.mouse_pos = pygame.mouse.get_pos()
        self.mousex , self.mousey = pygame.mouse.get_pos()
        #self.mouse1 = Mouse(self.pantalla, self.event)
        # Texto de puntos
        self.texto_puntos = Text(self.pantalla, self.window_rect, "game_font", 60, green, str(self.puntos))

        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT or (
                    self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE
            ):
                quit()

            # Aqui Añadiremos la logica que va a tener el juego
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "inicio":
                    self.click2_sound.play()
                    self.puntos += 1
                    self.menu = "play"



    # Par amanejar la logica del juego
    def _process_game_logic(self):
        #Se llama el Mpuse
        self.mouse1 = Mouse(self.pantalla, self.event)




    # Par adibujar en la pantalla por fotogramas y qeu esta se actualice cada sierto tiempo
    def _draw(self):
        self.pantalla.fill(black)

        if self.menu == "inicio":
            self.fondo_inicio.place()
            self.title_text.place(True, (0, -200))
            self.texto_puntos.place(True, (500, -200))
            self.play_button.place(True, (0, -45))
            self.about_button.place(True, (0, 100))

        elif self.menu == "play":
            self.fondo_menu.place()
            self.texto_puntos.place(True, (500, -200))
            self.menu_musica.play()


        # Colocamos en mouse en la pantalla
        self.mouse1.altera_cursor()
        print(self.mouse_pos[0], self.mouse_pos[1])
        print("Boton: ", self.play_button.rect)

        # update screen
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)