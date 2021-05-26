from Clases import *
import pygame
import os
from pygame.locals import *
from pygame.sprite import Sprite
from vector import Vector
from sys import exit
from math import *
import funciones
import random
from pygame.locals import *
from pygame.sprite import Sprite

def main(pantalla, num_pista, num_jugadores, Carro1, Carro2 = None, jugador1 = None, jugador2 = None):

    musicas = {1: "sounds/Wild Rift - LOL.mp3", 2: "sounds/Main Theme - ARK.mp3", 3: "sounds/Piercing Light  - LOL.mp3"}
    num_musica = random.randint(1, 3)
    pygame.mixer.pre_init(44100, -16, 2, 1024 * 4)
    ancho = 1361
    alto = 716
    window_rect = pantalla.get_rect()
    fps = 30

    #Colores
    blanco = (255, 255, 255, 255)
    negro = (0, 0, 0, 255)
    amarillo = (255, 240, 1, 255)
    rojo = (254, 0, 0, 255)
    meta = (237, 238, 240, 255)
    darkred = (139, 0, 0)

    #Funcion para escribir en la pantalla los objetos
    def escribe_en_pantalla(texto, color, tamanho, posicion):
        fuente = pygame.font.Font(None, tamanho)
        pantalla.blit(fuente.render(texto,  3, color), posicion)

    #Funcion para mapear la tecla que ha sido precionada
    def tecla(tecla, player):
        tecla_map = {'acelera': [K_UP, K_w], 'freno': [K_DOWN, K_s],\
                     'izquierda': [K_LEFT, K_a], 'derecha': [K_RIGHT, K_d]}
        if player == 1:
            return tecla_map[tecla][0]
        return tecla_map[tecla][1]

    #Esta clase nos permitira ver los datos del jugador en la pantalla
    class Display():
        def __init__(self, player):
            self.tamano_letra = 25
            self.numero_vueltas = 0

            if player == 1:
                self.name = jugador1
                self.carro_player = carro1
                self.posicion_nombre = (10, 5)
                self.posicion_velocidad = (10, 65)
                self.posicion_vueltas = (10, 85)
                self.posicion_vidas = (10, 45)
                self.posicion_puntos = (10, 105)
            else:
                self.name = jugador2
                self.carro_player = carro2
                self.posicion_nombre = (1200, 5)
                self.posicion_velocidad = (1200, 65)
                self.posicion_vueltas = (1200, 85)
                self.posicion_vidas = (1200, 45)
                self.posicion_puntos = (1200, 105)

        #Par amostrar la informacion que tendra el jugador
        def muestra_display(self):
            vida = 'Vida: ' + str(self.carro_player.life)
            velocidade = 'Velocidade: ' + str(self.carro_player.velocidad_carro // 5)
            voltas = 'Vueltas: ' + str(self.carro_player.vueltas)
            puntos = 'Puntos: ' + str(self.carro_player.puntos)

            #Esto se mostrara en la pantalla
            escribe_en_pantalla(self.name, darkred, self.tamano_letra, self.posicion_nombre)
            escribe_en_pantalla(vida, darkred, self.tamano_letra, self.posicion_vidas)
            escribe_en_pantalla(velocidade, darkred, self.tamano_letra, self.posicion_velocidad)
            escribe_en_pantalla(voltas, darkred, self.tamano_letra, self.posicion_vueltas)
            escribe_en_pantalla(puntos, darkred, self.tamano_letra, self.posicion_puntos)

    class Pista():
        def __init__(self, pista):
            #Variables para la clase
            self.snInicio = pygame.mixer.Sound('sounds/go.wav')
            self.snInicio.set_volume(0.2)
            self.imgpista = funciones.cargar_imagem('pista' + str(pista) + '.jpg')
            self.imgpista_colores = funciones.cargar_imagem('pista-' + str(pista) + '.jpg')
            self.num_vueltas = 1

            # Con respecto a la posicion qeu tengra el carro al iniciar la pista, y el angulo de rotacion
            self.tiempopo_enpantalla = 0
            self.largo = False
            self.tamano_letras = 200
            if num_pista == 1:
                self.posicion1 = Vector(850, 200)
                self.posicion2 = Vector(700, 210)
                self.rotacion_pantalla = 180.
            elif num_pista == 2:
                self.posicion1 = Vector(500, 630)
                self.posicion2 = Vector(350, 640)
                self.rotacion_pantalla = 180.
            elif num_pista == 3:
                self.posicion1 = Vector(700, 50)
                self.posicion2 = Vector(550, 60)
                self.rotacion_pantalla = 180.

        #Cuenta el tiempo de la apartida
        def tiempo_espera(self, tf, ti, numero):
            if tf > self.tiempopo_enpantalla >= ti:
                escribe_en_pantalla(numero, darkred, self.tamano_letras, (600, 250))

        #Comienza a contar antes de iniciar el juego
        def comienzo(self):
            if self.tiempopo_enpantalla < fps * 10:
                self.tiempopo_enpantalla += 1

            for i in range(1, 6):
                self.tiempo_espera(fps * i + fps, fps * i, "%d" % (6 - i))

            if fps * 7 > self.tiempopo_enpantalla >= fps * 6:
                self.snInicio.play()
                escribe_en_pantalla('GO!', darkred, self.tamano_letras, (580, 260))
                self.largo = True

        #Se cargan las imagenes de los colores
        def pistas_colores(self):
            pantalla.blit(self.imgpista_colores, (0, 0))

        #Se carga la imagen de las pistas con los obtaculos
        def pista_diseño(self):
            pantalla.blit(self.imgpista, (0, 0))

    #Nuestra clasa carro
    class Carro(Sprite):
        def __init__(self, player, num, *grupos):
            Sprite.__init__(self, *grupos)

            # Teclas que se usaran para que el carro se mueva
            self.acelerar, self.freno = tecla('acelera', player), tecla('freno', player)
            self.izquirda, self.derecha = tecla('izquierda', player), tecla('derecha', player)

            # La imagenes del carro que se selecciono
            self.imgscar = funciones.cargar_imagem(f"car{num}.png", 1)
            self.imgcar = self.imgscar

            # Variablels necesarias para el carro
            self.velocidad_carro = 0
            self.velocidad_max = 150.
            self.rotacion = pista.rotacion_pantalla
            self.velocidad_rotacao = 90.  # graus por segundo

            # la posicion inicial del carro seleccionado
            if player == 1:
                self.posicion = pista.posicion1
            else:
                self.posicion = pista.posicion2
            self.pos_antes_batida = self.posicion.copy()

            # Para saber el numero de vueltas que llevamos
            self.vueltas = 0

            self.cronometro = pygame.time.Clock()

            # Vida
            self.life = 200
            self.sonido_explosion = pygame.mixer.Sound('sounds/explode.wav')
            self.imgexplosion = funciones.cargar_imagem('explosion.png', 1, [(x, 0, 50, 50) for x in range(0, 400, 50)])
            self.imgexplota = self.imgexplosion[0]
            self.explocion = False
            self.conta_tempo_morte = fps * 5
            self.puntos = 0

            #Sonidos
            self.acelerasn = pygame.mixer.Sound('sounds/aceleracion_1.wav')

            # retangulo del  carro seleccionado
            self.rect = Rect(self.posicion.x - self.imgcar.get_width() / 2,
                             self.posicion.y - self.imgcar.get_height() / 2, \
                             self.imgcar.get_width(), self.imgcar.get_height())


            self.sombatida = pygame.mixer.Sound('sounds/warning.wav')
            self.sombatida.set_volume(0.2)
            self.sopasameta = pygame.mixer.Sound('sounds/go.wav')
            self.sopasameta.set_volume(0.2)

        def imgexplosion_carro(self):
            #Cambiamos la imagen del carro por la de la explosion
            self.imgcar = self.imgscar
            if self.life <= 0:
                self.imgcar = self.imgexplota

        #Detecta las colociones del auto y las pistas
        def colision(self):
            x, y = tuple(self.posicion)

            if x <= 10:
                x = 10
            elif x >= ancho - 10:
                x = ancho - 10

            if y <= 10:
                y = 10
            elif y >= alto - 10:
                y = alto - 10

            #Identificamos los colores de la pantalla y podemos saber donde estan los ostaculos
            if pista.imgpista_colores.get_at((int(self.posicion.x), int(self.posicion.y))) == rojo:
                self.sombatida.play()
                x += 2
            elif pista.imgpista_colores.get_at((int(self.posicion.x), int(self.posicion.y))) == amarillo:
                self.perde_life(5)
            if pista.imgpista_colores.get_at((int(self.posicion.x), int(self.posicion.y))) in [rojo, meta]:
                self.perder_velocidad(50, -25)
                self.perde_life(10)

            self.posicion = Vector(x, y)

        def acelera(self, pressed_key):
            #Para acelerar el carro
            if [pressed_key[self.acelerar], pressed_key[self.freno]] == [0, 0] or self.explocion:
                if self.velocidad_carro > 0:
                    self.velocidad_carro -= 5
                elif self.velocidad_carro < 0:
                    self.velocidad_carro += 5

            if pista.largo and not self.explocion:
                if pressed_key[self.acelerar]:
                    if self.velocidad_carro < 1000:
                        self.velocidad_carro += 20

                if pressed_key[self.freno]:
                    if 0 < self.velocidad_carro <= 1000:
                        self.velocidad_carro -= 20
                    elif -200 <= self.velocidad_carro <= 0:
                        self.velocidad_carro -= 10

        def perde_life(self, dano):
            #El jugador pierde vidas cuando resive algun naño
            if self.life > 0 and self.conta_tempo_morte == fps * 5:
                self.life -= dano

        def morre(self, grupo):
            #Con el efecto de explocion el carro desaparece
            if self.life <= 0 or fps * 2 >= self.conta_tempo_morte >= 0:
                grupo.remove(self)

                if fps * 5 >= self.conta_tempo_morte >= (fps * 5) - 5:
                    self.imgexplota = self.imgexplosion[0]
                    self.sonido_explosion.play()

                elif (fps * 5) - 5 >= self.conta_tempo_morte >= (fps * 5) - 10:
                    self.imgexplota = self.imgexplosion[1]

                elif (fps * 5) - 10 >= self.conta_tempo_morte >= (fps * 5) - 15:
                    self.imgexplota = self.imgexplosion[2]

                elif (fps * 5) - 15 >= self.conta_tempo_morte >= (fps * 5) - 20:
                    self.imgexplota = self.imgexplosion[3]

                elif (fps * 5) - 20 >= self.conta_tempo_morte >= (fps * 5) - 25:
                    self.imgexplota = self.imgexplosion[4]

                elif (fps * 5) - 25 >= self.conta_tempo_morte >= (fps * 5) - 30:
                    self.imgexplota = self.imgexplosion[5]

                elif (fps * 5) - 30 >= self.conta_tempo_morte >= (fps * 5) - 35:
                    self.imgexplota = self.imgexplosion[6]
                    self.velocidad_carro = 0

                if self.life <= 0:
                    self.explocion = True

                if self.conta_tempo_morte > 0:
                    self.conta_tempo_morte -= 1

                if self.conta_tempo_morte <= fps * 2:
                    self.add(grupo)
                    self.life = 200
                    self.explocion = False
                    if self.conta_tempo_morte <= 0:
                        self.conta_tempo_morte = fps * 5

        def perder_velocidad(self, limite, limite_re):
            #Regula la velocidad del jugador
            if self.velocidad_carro > limite:
                self.velocidad_carro-= 50
            elif -600 < self.velocidad_carro < limite_re:
                self.velocidad_carro+= 35


        def rotacion_carro(self, pressed_key):
            #Par ael movimiento del carro
            self.direcao_rotacao = 0.

            if self.velocidad_carro != 0:
                if self.velocidad_carro < 0:
                    if pressed_key[self.izquirda]:
                        self.direcao_rotacao = +1
                    elif pressed_key[self.derecha]:
                        self.direcao_rotacao = -1
                else:
                    if pressed_key[self.izquirda]:
                        self.direcao_rotacao = -1
                    elif pressed_key[self.derecha]:
                        self.direcao_rotacao = +1

        # Guarda la posicion en la que se encuantra el carro al morir
        def atualiza_rect(self):
             self.rect = Rect(self.posicion.x - self.imgcar.get_width() / 2, self.posicion.y - \
                                self.imgcar.get_height() / 2, self.imgcar.get_width(), self.imgcar.get_height())

        def completa_volta(self, pista):
             # Verifica un avuelta
            if pista.imgpista_colores.get_at((int(self.posicion.x), int(self.posicion.y))) == meta:

                self.vueltas += 1
                # Esta sera la de los puntos
                self.puntos += 10
                self.sopasameta.play()
                if self.vueltas == pista.num_vueltas:
                    return True

        def rotaciona_imgcarro(self):
            """ rotaciona a imagem do carro de acordo com a ação realizadaa pelo usuário """
            self.imgcar = pygame.transform.rotate(self.imgcar, self.rotacion)
            self.w, self.h = self.imgcar.get_size()
            desenha_carro = Vector(self.posicion.x - self.w/2, self.posicion.y - self.h/2)
            pantalla.blit(self.imgcar, desenha_carro)

        def movimenta(self, time_passed_seconds):
            #Movimiento normal de carro
            self.direcao_movimento = +(self.velocidad_carro/1000.)
            self.rotacion += self.direcao_rotacao * self.velocidad_rotacao * time_passed_seconds
            if self.rotacion >= 360:
               self.rotacion = self.rotacion - 360
            elif self.rotacion < 0:
               self.rotacion = 360 + self.rotacion
            heading_x = cos(self.rotacion*pi/180.0)
            heading_y = sin(self.rotacion*pi/180.0)
            heading = Vector(heading_x, heading_y)
            heading *= self.direcao_movimento
            self.posicion += heading * self.velocidad_max * time_passed_seconds

        #Determina cuando el carro choca con algun obstaculo
        def testa_batida(self, outro, grupo):
            self.atualiza_rect()
            outro.atualiza_rect()

            x, y = tuple(self.posicion)
            x1, y1 = tuple(self.pos_antes_batida)
            if outro in pygame.sprite.spritecollide(self, grupo, False):
                self.sombatida.play()
                x, y = x1, y1
                if (45 <= self.rotacion <= 135 and 45 <= outro.rotacao <= 135) or \
                        (225 < self.rotacion < 315 and 225 < outro.rotacao < 315) or \
                        (135 < self.rotacion <= 225 and 135 < outro.rotacao <= 225) or \
                        ((315 < self.rotacion < 360 or 0 < self.rotacion < 45) and \
                         (315 < outro.rotacao < 360 or 0 < outro.rotacao < 45)):

                    outro.velocidade_carro += self.velocidad_carro / 3
                    outro.velocidade_carro -= outro.velocidade_carro % 10
                    self.velocidad_carro -= self.velocidad_carro / 2
                    self.velocidad_carro -= self.velocidad_carro % 10

                elif (225 < self.rotacion < 315 and 45 <= outro.rotacao <= 135) or \
                        (45 <= self.rotacion <= 135 and 225 < outro.rotacao < 315) or \
                        (135 < self.rotacion <= 225 and (315 < outro.rotacao < 360 or \
                                                        0 < outro.rotacao < 45)) or ((315 < self.rotacion < 360 \
                                                                                      or 0 < self.rotacion < 45) and 135 < outro.rotacao <= 225):

                    outro.velocidade_carro -= self.velocidad_carro / 3
                    outro.velocidade_carro -= outro.velocidade_carro % 10
                    self.velocidad_carro -= self.velocidad_carro / 2
                    self.velocidad_carro -= self.velocidad_carro % 10

                elif ((self.velocidad_carro > 0 and 45 < self.rotacion < 135) or \
                      (self.velocidad_carro < 0 and 225 < self.rotacion < 315)) and \
                        (135 < outro.rotacao <= 225 or (315 < outro.rotacao < 360 or 0 < outro.rotacao < 45)):

                    self.velocidad = self.velocidad_carro / 4
                    outro.posicao.x += 2

                elif ((self.velocidad_carro < 0 and 45 < self.rotacion < 135) or \
                      (self.velocidad_carro > 0 and 225 < self.rotacion < 315)) and \
                        (135 < outro.rotacao <= 225 or (315 < outro.rotacao < 360 or 0 < outro.rotacao < 45)):

                    self.velocidad = self.velocidad_carro / 4
                    outro.posicao.x -= 2

                elif ((135 < self.rotacion < 225 and self.velocidad_carro > 0) or \
                      ((315 < self.rotacion < 360 or 0 < self.rotacion < 45) and \
                       self.velocidad_carro < 0)) and (45 <= outro.rotacao <= 135 or 225 < outro.rotacao < 315):

                    self.velocidad = self.velocidad_carro / 4
                    outro.posicao.y -= 2

                elif ((315 < self.rotacion < 360 or 0 < self.rotacion < 45) and \
                      self.velocidad_carro > 0 or (135 < self.rotacion < 225 and \
                                                    self.velocidad_carro < 0)) and (
                        45 <= outro.rotacao <= 135 or 225 < outro.rotacao < 315):

                    self.velocidad = self.velocidad_carro / 4
                    outro.posicao.y += 2

                elif self.rect.collidepoint(outro.posicion):
                    self.perde_life(200)

                self.perde_life(2)
            else:
                self.pos_antes_batida = self.posicion
            self.posicion = Vector(x, y)

        #LLamamos a todas las funciones que han sigo creadas, y se introsuce la variable para saber a cual grupo pertenece
        def Acciones(self, grupo):
            self.colision()
            self.imgexplosion_carro()
            self.acelera(pressed_key)
            self.rotacion_carro(pressed_key)
            self.rotaciona_imgcarro()
            self.movimenta(time_passed_seconds)
            self.morre(grupo)

    pygame.init()

    pygame.mixer.music.load(musicas[num_musica])
    pygame.mixer.music.play(-2)

    pista = Pista(num_pista)
    carro1 = Carro(1, Carro1)
    pantalla1 = Display(1)
    pantalla_jugador1 = pygame.sprite.GroupSingle(carro1)
    if num_jugadores > 1:
        carro2 = Carro(2, Carro2)
        pantalla2 = Display(2)
        pantalla_jugador2 = pygame.sprite.GroupSingle(carro2)

    clock = pygame.time.Clock()

    sairmenu = False

    while True:

        time_passed = clock.tick(fps)
        time_passed_seconds = time_passed / 1000.0

        pantalla1.muestra_display()
        if num_jugadores > 1:
            pantalla2.muestra_display()

        pygame.display.update()

        #Parte logica
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

        #Par acambiar de pista cada vez qeu se cumple con los 200 puntos
        carro1.completa_volta(pista)
        if num_jugadores == 1:
            if num_pista == 1 and carro1.puntos > 200:
                main(pantalla, 2, num_jugadores, Carro1, None, jugador1, jugador2)
            elif num_pista == 2 and carro1.puntos > 200:
                main(pantalla, 3, num_jugadores, Carro1, None, jugador1, jugador2)
        elif num_jugadores == 2:
            if num_pista == 1 and carro1.puntos > 200 and carro2.puntos > 200:
                main(pantalla, 2, num_jugadores, Carro1, None, jugador1, jugador2)
            elif num_pista == 2 and carro1.puntos > 200 and carro2.puntos > 200:
                main(pantalla, 3, num_jugadores, Carro1, None, jugador1, jugador2)

        pressed_key = pygame.key.get_pressed()

        #Ver las pistas
        pista.pistas_colores()
        pista.pista_diseño()

        carro1.Acciones(pantalla_jugador1)

        #aqui mostramos los datos del sugundo jugador
        if num_jugadores > 1:
            carro2.Acciones(pantalla_jugador2)

            # si los carros chocan entonces se activara esta funcion
            carro1.testa_batida(carro2, pantalla_jugador1)
            carro2.testa_batida(carro1, pantalla_jugador2)

        pista.comienzo()
        pygame.display.flip()
