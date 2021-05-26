
#region Importadas
import csv

from Clases import *
import pygame
import ctypes
import os
import sys
import pickle
import Carrera
from datetime import date

import tkinter as tk
from tkinter import ttk
#endregion

#region Colores
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
#endregion

font = pygame.font.SysFont("comicsansms", 30)
nameActive = False
regionsActive = False
slategrey = (112, 128, 144)

class pydeathrace:
    def __init__(self):
        self._init_pygame()

        #región datos de pantalla y datos del sistema
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        #self.ancho, self.alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.ancho = 1361
        self.alto = 716
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto ))
        self.window_rect = self.pantalla.get_rect()

        #Variables para la fecha
        self.today = date.today()
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.smallfont = pygame.font.SysFont("comicsansms", 14)
        self.slategrey = (112, 128, 144)

        #Obtenemos la fecha del sistema
        self.todayText = "Fecha:  " + self.today.strftime("%A") + ", " + self.today.strftime(
            "%B") + " " + self.today.strftime("%d") + \
                         ", " + self.today.strftime("%Y")
        self.todayText = self.smallfont.render(self.todayText, True, darkred)
        #endregion

        # Para que el juego se ejecute siempre en unos FPS establecidas
        self.clock = pygame.time.Clock()

        #región Variables
        #Variable para el menú
        self.menu = "menu"
        self.jugadores = "uno"

        #Variables para la pantalla
        self.Carro1_seleccionado = 1
        self.Carro2_seleccionado = None
        self.Pista_seleccionada = 1
        self.Jugadores_seleccionados = 1

        #Nombre de usuarios
        self.nombre_usuario = ""
        self.nombre_usuario2 = ""
        self.nombre_usuario_1 = ""
        self.nombre_usuario_2 = None

        self.newUserName = ""
        self.userName = ""
        #endregion

        #región botones
        self.btn_atras = Image("button", "Atras.png", (90, 56), self.pantalla, self.window_rect)
        self.btn_guardar = Image("button", "Guardar.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_indicaciones = Image("button", "Indicaciones.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_info = Image("button", "Info.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_jugar = Image("button", "Jugar.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_jugar_pista = Image("button", "jugar.png",(100, 60), self.pantalla, self.window_rect)
        self.btn_menu = Image("button", "Menu.png", (290, 225), self.pantalla, self.window_rect)
        self.btn_nombre = Image("button", "Nombre.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_pausa = Image("button", "Pausa.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_play = Image("button", "Play.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_puntaje = Image("button", "Puntaje.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_salir = Image("button", "Salir.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_terminar = Image("button", "Terminar.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_menu_indicaciones = Image("img", "Indicacion1.png", (580, 515), self.pantalla, self.window_rect)


        self.btn_iformacion = Image("img", "Informacion.png", (180, 115), self.pantalla, self.window_rect)
        self.btn_cuadroinfo = Image("img", "CuadroInfo.png", (580, 515), self.pantalla, self.window_rect)

        #Botones de flechas
        self.btn_flecha_derecha = Image("button", "Seleccion.png", (50, 30), self.pantalla, self.window_rect)
        self.btn_flecha_izquierda = Image("button", "Atras.png", (50, 30), self.pantalla, self.window_rect)
        self.btn_flecha_derecha2 = Image("button", "Seleccion.png", (50, 30), self.pantalla, self.window_rect)
        self.btn_flecha_izquierda2 = Image("button", "Atras.png", (50, 30), self.pantalla, self.window_rect)
        self.btn_flecha_derecha3 = Image("button", "Seleccion.png", (50, 30), self.pantalla, self.window_rect)
        self.btn_flecha_izquierda3 = Image("button", "Atras.png", (50, 30), self.pantalla, self.window_rect)

        self.btn_multigugador = Image("img", "upgrade_hp.png", (70, 70), self.pantalla, self.window_rect)

        #Títulos
        self.btn_jugador1 = Image("img", "Jugador1.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_jugador2 = Image("img", "Jugador2.png", (230, 115), self.pantalla, self.window_rect)
        self.btn_icono_inicio = Image("img", "Icono.png", (300, 155), self.pantalla, self.window_rect)
        self.btn_pista_titulo = Image("img", "Pista.png", (230, 115), self.pantalla, self.window_rect)
        #endregion

        #RegiÓn Listas
        # Fondo pantalla
        self.f_inicio = Image("img", "FondoPrincipal.png", (self.ancho, self.alto), self.pantalla, self.window_rect)

        # Carros en una lista
        self.imagenes_carros = []
        for i in range(1, 16):
            self.imagenes_carros.append(Image("img", f"car{i}.png", (125, 65), self.pantalla, self.window_rect))
        self.contador_carros = 0

        # Carros2 en una lista
        self.imagenes_carros2 = []
        for i in range(1, 16):
            self.imagenes_carros2.append(Image("img", f"car{i}.png", (125, 65), self.pantalla, self.window_rect))
        self.contador_carros2 = 0

        #Pistas en una lista
        self.imagenes_pistas = []
        for i in range(1, 4):
            self.imagenes_pistas.append(Image("img", f"pista{i}.jpg", (200, 150), self.pantalla, self.window_rect))
        self.contador_pistas = 0
        #endregion

        #Region de sonido
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
        #endregion

        #Región texto
        self.inicio_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, " PyDeathRace ", crimson)
        self.title_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, "Menu Principal", cyan)
        self.play_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, " ¿Que desea hacer? ", crimson)
        self.info_tex = Text(self.pantalla, self.window_rect, "game_font", 60, white, " Info ", darkslategray)
        self.indica_text = Text(self.pantalla, self.window_rect, "game_font", 60, white, " indicaciones ", darkred)
        self.titulo_nombre_text = Text(self.pantalla, self.window_rect, "game_font", 50, white, " Ingrese su nombre de usuario, por favor ", darkred)
        #endregion

        self.puntuacionAlta = 0

        #Creamos una caja de texto con TKINTER
        #self.entry = ttk.Entry(self.pantalla)
        # Create the text box
        self.userNameSurface = font.render(self.newUserName, True, white)
        # Create the border around the text box with .Rect
        # left, top, width, height
        self.userNameBorder = pygame.Rect(((self.ancho - self.userNameSurface.get_width()) / 2) - 10, self.alto * .20,
                                          self.userNameSurface.get_width() + 10, 50)

        self.input_box1 = CajaText(100, 100, 140, 32)
        self.input_box2 = CajaText(100, 100, 140, 32)
        self.done = False

        #Región par a las pantallas en espera
        self.espera1_text = Text(self.pantalla, self.window_rect, "game_font", 35, white, "Cargando Sala...")
        self.espera2_text = Text(self.pantalla, self.window_rect, "game_font", 35, white, "Espere un momento...")
        self.tiempo_espera = 0
        #endregion

    # Función para guardar las puntuaciones de los jugadores
    def SaveScores(self, sc, hs, user):
        self.user = user
        self.sc = sc
        self.hs = hs
        self.lista = []
        with open("puntajesJugadores.csv", newline='') as File:
            reader = csv.reader(File)
            self.lista.append([self.user, self.hs, self.sc])
            for row in reader:
                if len(row) > 0:
                    if self.user != row[0]:
                        self.lista.append(row)
        writer = csv.writer(open('puntajesJugadores.csv', 'w'), delimiter=",")
        writer.writerows(self.lista)

    # Función para cargar el puntajes más altos de los jugadores
    def LoadScores(self, user):
        self.user = user
        with open("puntajesJugadores.csv", newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if len(row) > 0:
                    if self.user == row[0]:
                        self.puntuacionAlta = int(row[1])
                        self.puntos = int(row[2])
                        if 1 == 1:
                            self.puntos = 0
                        else:
                            self.puntos = int(row[2])
     # Clase para la nave defensora

    # Este es el bucle de nuestro juego
    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    # El init pygame es siempre necesario al inicio de un juego con pygame
    def _init_pygame(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.init()

        #Nombre e ícono
        pygame.display.set_caption("PyDeathRace 2.0")
        pygame.display.set_icon(pygame.image.load(os.path.join("img/icon.png")))

    # Para manejar las entradas
    def _handle_input(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mousex , self.mousey = pygame.mouse.get_pos()

        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT or (
                    self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE
            ):
                quit()

            #Para las cajas de texto
            self.input_box1.handle_event(self.event)
            self.input_box2.handle_event(self.event)
            self.nombre_usuario1 = self.input_box1.text
            self.nombre_usuario2 = self.input_box2.text

            # Aquí añadiremos la lógica que va a tener el juego
            if self.event.type == pygame.MOUSEBUTTONDOWN:

                #Evento del botón Play
                if self.btn_play.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "menu":
                    self.s_click2.play()
                    self.menu = "play"

                #Evento del botón info
                if self.btn_info.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "menu":
                    self.s_click2.play()
                    self.menu = "info"

                #Evento del botón indicaciones
                if self.btn_indicaciones.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "menu":
                    self.s_click2.play()
                    self.menu = "indica"

                #***********************************************************************************************************
                #Eventos dentro del menú principal
                #Nombre
                if self.btn_nombre.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click2.play()
                    self.menu = "nombre"

                #Puntos
                if self.btn_puntaje.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "play":
                    self.s_click2.play()
                    self.menu = "puntaje"

                #Eventos del botón jugar
                if self.btn_jugar.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "play":
                    self.s_click2.play()
                    #Carrera.main(self.pantalla)
                    self.menu = "seleccionar"

                #Eventos del botón que pasa a la pista
                if self.btn_jugar_pista.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click3.play()
                    #Carrera.main(self.pantalla)
                    self.menu = "CargandoJuego"

                #Eventos en la pantalla seleccionar
                if self.btn_flecha_derecha.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click.play()
                    if self.contador_carros == 14:
                        self.contador_carros = 0
                    else:
                        self.contador_carros += 1
                    self.Carro1_seleccionado = self.contador_carros + 1
                if self.btn_flecha_izquierda.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click.play()
                    if self.contador_carros  == 0:
                        self.contador_carros = 14
                    else:
                        self.contador_carros -= 1
                    self.Carro1_seleccionado = self.contador_carros + 1

                #Eventos para las pistas
                if self.btn_flecha_derecha2.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click.play()
                    if self.contador_pistas == 2:
                        self.contador_pistas = 0
                    else:
                        self.contador_pistas += 1
                    self.Pista_seleccionada = self.contador_pistas + 1
                if self.btn_flecha_izquierda2.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click.play()
                    if self.contador_pistas  == 0:
                        self.contador_pistas = 2
                    else:
                        self.contador_pistas -= 1
                    self.Pista_seleccionada = self.contador_pistas + 1

                # Eventos Para el segundo jugador
                if self.btn_flecha_derecha3.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click.play()
                    if self.contador_carros2 == 14:
                        self.contador_carros2 = 0
                    else:
                        self.contador_carros2 += 1
                    self.Carro2_seleccionado = self.contador_carros2 + 1
                if self.btn_flecha_izquierda3.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click.play()
                    if self.contador_carros2 == 0:
                        self.contador_carros2 = 14
                    else:
                        self.contador_carros2 -= 1
                    self.Carro2_seleccionado = self.contador_carros2 + 1

                #Botón para ingresar un jugador más a la partida
                if self.btn_multigugador.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "seleccionar":
                    self.s_click1.play()
                    #self.LoadScores("allan")
                    if self.jugadores == "uno":
                        self.jugadores = "dos"
                        self.Jugadores_seleccionados = 2
                    elif self.jugadores == "dos":
                        self.jugadores = "uno"
                        self.Jugadores_seleccionados = 1

                # Evento del botón salir
                if self.btn_salir.rect.collidepoint(self.mouse1.coordenadas_cursor()) and self.menu == "play":
                    quit()

                #Evento botón atrás
                if self.btn_atras.rect.collidepoint(self.mouse1.coordenadas_cursor()):
                    if self.menu == "play" or self.menu == "info" or self.menu == "indica":
                        self.s_click3.play()
                        self.menu = "menu"
                    elif self.menu == "puntaje" or self.menu == "seleccionar":
                        #self.nombre_usuario = self.input_box1.text
                        self.s_click3.play()
                        self.menu = "play"
                    elif self.menu == "nombre":
                        self.s_click3.play()
                        if self.nombre_usuario1 != "":
                            self.nombre_usuario_1 = self.nombre_usuario1
                        if self.nombre_usuario2 != "" and self.Jugadores_seleccionados == 2:
                            self.nombre_usuario_2 = self.nombre_usuario2
                        self.menu = "seleccionar"

                        #Guardar nombre de usuario
                        self.SaveScores(self.nombre_usuario_1, self.Carro1_seleccionado, self.Pista_seleccionada)



    # Para amanejar la lógica del juego
    def _process_game_logic(self):
    #Se llama el Mouse
        self.mouse1 = Mouse(self.pantalla, self.event)

    # Para dibujar en la pantalla por fotogramas y que esta se actualice cada cierto tiempo
    def _draw(self):
        self.pantalla.fill(black)

        #Vista de la pantalla de inicio
        if self.menu == "menu":
            self.f_inicio.place()
            self.pantalla.blit(self.todayText, (1130, 8))
            self.btn_icono_inicio.place(True, (0, -280))
            self.btn_play.place(True, (0, -125))
            self.btn_info.place(True, (0, 55))
            self.btn_indicaciones.place(True, (0, 240))

        #Vista de la pantalla de menú
        elif self.menu == "play":
            self.f_inicio.place()
            self.pantalla.blit(self.todayText, (1130, 8))
            self.btn_menu.place(True, (0, -240))
            self.btn_puntaje.place(True, (275, 0))
            self.btn_jugar.place(True, (-275, 0))
            self.btn_salir.place(True, (0, 200))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantala de información
        elif self.menu == "info":
            self.f_inicio.place()
            self.info_tex.place(True, (0, -390))
            self.btn_iformacion.place(True, (-5,-300))
            self.btn_cuadroinfo.place(True, (25 , 0))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantalla de indicaciones
        elif self.menu == "indica":
            self.f_inicio.place()
            self.btn_indicaciones.place(True, (0, -290))
            self.btn_menu_indicaciones.place(True, (25, 0))
            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantalla nombre
        elif self.menu == "nombre":
            self.f_inicio.place()
            self.btn_nombre1 = Image("button", "Nombre1.png", (230, 115), self.pantalla, self.window_rect)
            self.btn_nombre2 = Image("button", "Nombre2.png", (230, 115), self.pantalla, self.window_rect)
            self.input_box1.draw(self.pantalla, self.window_rect, True, (-400, 20))
            self.btn_nombre.place(True, (-0, -290))
            self.btn_nombre1.place(True, (-400, -130))
            if self.jugadores == "dos":
                self.input_box2.draw(self.pantalla, self.window_rect, True, (400, 20))
                self.btn_nombre2.place(True, (400, -130))

            self.btn_atras.place(True, (-590, -320))

        #Vista de la pantalla puntaje
        elif self.menu == "puntaje":
            self.f_inicio.place()
            self.btn_puntaje.place(True, (0, -290))
            self.btn_atras.place(True, (-590, -320))

        #Ventana para seleccionar las caracteristicas de la lista
        elif self.menu == "seleccionar":

            self.f_inicio.place()

            #Para ver los carros que se quieren jugar
            self.btn_flecha_derecha.place(xy=(390, 240))
            self.btn_flecha_izquierda.place(xy=(155, 240))
            self.imagenes_carros[self.contador_carros].place(xy=(245, 225))

            self.usuario_nombre = Text(self.pantalla, self.window_rect, "game_font", 30, crimson,
                                       " Usuario: " + self.nombre_usuario_1 + " / ")
            self.usuario_nombre.place(xy=(570, 225))

            self.btn_jugador1.place(xy=(200, 85))
            self.btn_nombre.place(xy=(570, 85))
            self.btn_pista_titulo.place(xy=(970, 85))

            #Para ver las pistas en la paantalla
            self.btn_flecha_derecha2.place(xy=(1210, 350))
            self.btn_flecha_izquierda2.place(xy=(900, 350))
            self.imagenes_pistas[self.contador_pistas].place(xy=(980, 305))

            self.btn_multigugador.place(True, (-450, 0))

            if self.jugadores == "dos":
                # Para ver los carros que se quieren jugar
                self.btn_jugador2.place(xy=(200, 450))
                self.btn_flecha_derecha3.place(xy=(390, 610))
                self.btn_flecha_izquierda3.place(xy=(155, 610))
                self.imagenes_carros2[self.contador_carros2].place(xy=(245, 595))

                self.usuario_nombre2 = Text(self.pantalla, self.window_rect, "game_font", 30, crimson,
                                           " Usuario: " + str(self.nombre_usuario_2))
                self.usuario_nombre2.place(xy=(570, 595))

            self.btn_atras.place(True, (-590, -320))
            self.btn_jugar_pista.place(True, (590, 320))

        #Patntallas Cargando el juego
        elif self.menu == "CargandoJuego":

            self.pantalla.fill(darkred)
            if self.tiempo_espera < 90:
                self.espera1_text.place(True)
                self.tiempo_espera += 1

            if self.tiempo_espera >= 90:
                self.espera2_text.place(True)
                self.tiempo_espera += 1

            if self.tiempo_espera == 170:
                #Pasamos a jugar en la pista
                Carrera.main(self.pantalla, self.Pista_seleccionada, self.Jugadores_seleccionados, self.Carro1_seleccionado, self.Carro2_seleccionado, self.nombre_usuario_1, self.nombre_usuario_2)
                self.menu = "menu"

        # Colocamos en mouse en la pantalla
        self.mouse1.altera_cursor()
        print(self.mouse_pos[0], self.mouse_pos[1])
        #print("Boton: ", self.btn_play.rect)

        #print(self.menu)
        #print(str(self.input_box1))
        print("Carro: ", self.Carro1_seleccionado)
        print("Carro2: ", self.Carro2_seleccionado)
        print("Pista: ", self.Pista_seleccionada)
        print("jugadores: ", self.Jugadores_seleccionados)
        print("Nombre: ", self.nombre_usuario_1)
        print("Nombre2: ", self.nombre_usuario_2)

        # update screen
        self.input_box1.update()
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
