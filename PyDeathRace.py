
from Clases import *
import pygame
import ctypes
import os

# Colores
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
celeste = (0, 255, 255)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
aqua = (127, 255, 212)
darksalmon = (233, 150, 122)
cyan = (0, 255, 255)
darkslategray = (47, 79, 79)
darkkahaki = (189, 183, 107)
darkorange = (255, 140, 0)
darkred = (139, 0, 0)
crimson = (220, 20, 60)

class pydeathrace:
    def __init__(self):
        self._init_pygame()

        # Nos permite obtener el tamaño de la pantalla completa
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        #self.ancho, self.alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.ancho = 1361
        self.alto = 716
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto ))
        self.window_rect = self.pantalla.get_rect()


        # Para que el juego se ejecute siempre en unas FPS establecidas
        self.clock = pygame.time.Clock()

        #Variable para el menu
        self.menu = "menu"

        #Nombre de usuarios
        self.nombre_usuario = "#"

        #Ejemplo para los puntos
        self.puntos = 0
        #self.p = puntos

        #Botones
        self.btn_atras = Image("button", "Atras.png", (90, 56), self.pantalla, self.window_rect)
        self.btn_guardar = Image("button", "Guardar.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_indicaciones = Image("button", "Indicaciones.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_info = Image("button", "Info.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_jugar = Image("button", "Jugar.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_menu = Image("button", "Menu.png", (290, 225), self.pantalla, self.window_rect)
        self.btn_nombre = Image("button", "Nombre.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_pausa = Image("button", "Pausa.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_play = Image("button", "Play.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_puntaje = Image("button", "Puntaje.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_salir = Image("button", "Salir.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_terminar = Image("button", "Terminar.png", (180, 115), self.pantalla, self.window_rect)

        self.btn_iformacion = Image("img", "Informacion.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_cuadroinfo = Image("img", "CuadroInfo.png", (580, 515), self.pantalla, self.window_rect)


        # Fondo pantalla
        self.f_inicio = Image("img", "FondoPrincipal.png", (self.ancho, self.alto), self.pantalla, self.window_rect)

        #Pistas
        #self.p_pista1 = Image("img", "Pista1-png.png", (self.ancho, self.alto), self.pantalla, self.window_rect)
        #self.p_pista2 = Image("img", "Pista2.png", (self.ancho, self.alto), self.pantalla, self.window_rect)
        #self.p_pista3 = Image("img", "Pista3.png", (self.ancho, self.alto), self.pantalla, self.window_rect)

        # Sound
        #self.s_battlefield = pygame.mixer.Sound(os.path.join("sounds", "Battlefield.mp3"))
        self.s_click = pygame.mixer.Sound(os.path.join("sounds", "click.wav"))
        self.s_click1 = pygame.mixer.Sound(os.path.join("sounds", "click1.wav"))
        self.s_click2 = pygame.mixer.Sound(os.path.join("sounds", "click2.wav"))
        self.s_click3 = pygame.mixer.Sound(os.path.join("sounds", "click3.wav"))
        self.s_explode = pygame.mixer.Sound(os.path.join("sounds", "explode.wav"))
        #self.s_final = pygame.mixer.Sound(os.path.join("sounds", "final.ogg"))
        self.s_go = pygame.mixer.Sound(os.path.join("sounds", "go.wav"))
        self.s_lose = pygame.mixer.Sound(os.path.join("sounds", "lose.wav"))
        self.s_race = pygame.mixer.Sound(os.path.join("sounds", "race.wav"))
        self.s_ready = pygame.mixer.Sound(os.path.join("sounds", "ready.wav"))
        self.s_tiro = pygame.mixer.Sound(os.path.join("sounds", "tiro.wav"))
        self.s_warning = pygame.mixer.Sound(os.path.join("sounds", "warning.wav"))
        self.s_win = pygame.mixer.Sound(os.path.join("sounds", "win.wav"))
        self.s_winrace = pygame.mixer.Sound(os.path.join("sounds", "winrace.wav"))

        # Texto
        self.usuario_nomnre = Text(self.pantalla, self.window_rect, "game_font",30, crimson, " Usuario: " + self.nombre_usuario)
        self.inicio_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, " PyDeathRace ", crimson)
        self.title_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, "Menu Principal", cyan)
        self.play_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, " ¿Que desea hacer? ", crimson)
        self.info_tex = Text(self.pantalla, self.window_rect, "game_font", 60, white, " Info ", darkslategray)
        self.indica_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, " indicaciones ", darkred)
        self.titulo_nombre_text = Text(self.pantalla, self.window_rect, "game_font", 50, white, " Ingrese su nombre de usuario, por favor ", darkred)

        self.input_box1 = CajaText(100, 100, 140, 32)
        self.done = False

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

            self.input_box1.handle_event(self.event)
            self.input_box1.update()
            self.nombre_usuario = self.input_box1.text
            #self.nombre2 = str(self.input_box1.text)

            # Aqui Añadiremos la logica que va a tener el juego
            if self.event.type == pygame.MOUSEBUTTONDOWN:

                #Evento del boton Play
                if self.btn_play.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "menu":
                    self.s_click2.play()
                    self.menu = "play"

                #Evento del boton info
                if self.btn_info.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "menu":
                    self.s_click2.play()
                    self.puntos += 1
                    self.menu = "info"

                #Evento del boton indicaciones
                if self.btn_indicaciones.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "menu":
                    self.s_click2.play()
                    self.menu = "indica"

                #***********************************************************************************************************
                #Eventos dentro del menu principal
                #Nombre
                if self.btn_nombre.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "play":
                    self.s_click2.play()
                    self.menu = "nombre"

                #Puntos
                if self.btn_puntaje.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "play":
                    self.s_click2.play()
                    self.menu = "puntaje"


                #evento del boton salir
                if self.btn_salir.rect.collidepoint(self.mouse1.coordenadas_cursor()):
                    quit()

                #evento boton atras
                if self.btn_atras.rect.collidepoint(self.mouse1.coordenadas_cursor()):
                    if self.menu == "play" or self.menu == "info" or self.menu == "indica":
                        self.s_click3.play()
                        self.menu = "menu"
                    elif self.menu == "nombre" or self.menu == "puntaje":
                        #self.nombre_usuario = self.input_box1.text
                        self.s_click3.play()
                        self.menu = "play"

    # Par amanejar la logica del juego
    def _process_game_logic(self):
        #Se llama el Mouse
        self.mouse1 = Mouse(self.pantalla, self.event)

    # Para dibujar en la pantalla por fotogramas y qeu esta se actualice cada sierto tiempo
    def _draw(self):
        self.pantalla.fill(black)

        #Vista de la pantalla de inicio
        if self.menu == "menu":
            self.f_inicio.place()
            self.inicio_text.place(True, (0, -310))
            self.btn_play.place(True, (0, -125))
            self.btn_info.place(True, (0, 55))
            self.btn_indicaciones.place(True, (0, 240))

        #Vista de la pantalla de menu
        elif self.menu == "play":
            self.f_inicio.place()
            #self.play_text.place(True, (0, -280))
            self.btn_menu.place(True, (0, -240))
            self.usuario_nomnre.place(True, (480, -320))
            self.btn_nombre.place(True, (-275, -50))
            self.btn_puntaje.place(True, (-275, 150))
            self.btn_jugar.place(True, (275, -50))
            self.btn_salir.place(True, (275, 150))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantala de informacion
        elif self.menu == "info":
            self.f_inicio.place()
            self.info_tex.place(True, (0, -390))
            #self.btn_iformacion.....
            self.btn_cuadroinfo.place(True, (25 , 0))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantalla de indicaciones
        elif self.menu == "indica":
            self.f_inicio.place()
            self.btn_indicaciones.place(True, (0, -290))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantalla nombre
        elif self.menu == "nombre":
            self.f_inicio.place()
            self.input_box1.draw(self.pantalla, self.window_rect, True, (0, 0))
            self.btn_nombre.place(True, (0, -290))
            self.titulo_nombre_text.place(True, (0, -150))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantalla puntaje
        elif self.menu == "puntaje":
            self.f_inicio.place()
            #self.indica_tex.place(True, (0, -200))
            self.btn_puntaje.place(True, (0, -290))
            self.btn_atras.place(True, (-590, -320))

        # Colocamos en mouse en la pantalla
        self.mouse1.altera_cursor()
        print(self.mouse_pos[0], self.mouse_pos[1])
        #print("Boton: ", self.btn_play.rect)

        print(self.menu)
        print(str(self.input_box1))

        # update screen
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(60)