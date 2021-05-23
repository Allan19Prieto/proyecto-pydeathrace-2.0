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

def main(pantalla, num_pista, num_jugadores, carro1, carro2 = None, jugador1 = None, jugador2 = None):

    #musicas = {1: "sounds/final.ogg", 2: "sounds/lose.wav", 3: "sounds/ready.wav"}
    #num_musica = random.randint(1, 3)
    pygame.mixer.pre_init(44100, -16, 2, 1024 * 4)

    ancho = 1361
    alto = 716
    #pantalla = pygame.display.set_mode((ancho, alto))
    window_rect = pantalla.get_rect()
    #region Datos para el cronometro
    #fuente = pygame.font.SysFont("Arial", 20, True, False)
    #info = fuente.render("Este va a ser el cronometro", 0, (255,255,255))
    #endragion
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

    class Display():
        #Las variables que se utilizaran durante el juego
        def __init__(self, player):
            self.tamano_letra = 25
            self.numero_vueltas = 0

            if player == 1:
                self.name = jugador1
                self.carro_player = carrop1
                self.posicion_nombre = (5, 5)
                self.posicion_velocidad = (5, 65)
                self.posicion_vueltas = (5, 85)
                self.posicion_vidas = (5, 45)
                self.posicion_puntos = (5, 105)

            else:
                self.name = jugador2
                #self.carro_player = carrop2
                self.posicion_nombre = (5, 625)
                self.posicion_velocidad = (5, 685)
                self.posicion_vueltas = (5, 705)
                self.posicion_vidas = (5, 665)
                self.posicion_puntos = (5, 725)


        #Par amostrar la informacion que tendra el jugador
        def exibe_display(self):
            vida = 'Vida: ' + str(self.carro_player.life)
            velocidade = 'Velocidade: ' + str(self.carro_player.velocidade_carro / 5)
            voltas = 'Vueltas: ' + str(0+1) + '/' + str(self.numero_vueltas)
            puntos = 'Puntos: ' + str(0+1) +  '/' + str(self.carro_player.puntos)


            escribe_en_pantalla(self.name, darkred, self.tamano_letra, self.posicion_nombre)
            escribe_en_pantalla(vida, darkred, self.tamano_letra, self.posicion_vidas)
            escribe_en_pantalla(velocidade, darkred, self.tamano_letra, self.posicion_velocidad)
            escribe_en_pantalla(voltas, darkred, self.tamano_letra, self.posicion_vueltas)
            escribe_en_pantalla(puntos, darkred, self.tamano_letra, self.posicion_puntos)

    class Pista():
        def __init__(self, pista):
            #Variables para la clase
            self.imgpista = funciones.cargar_imagem('pista' + str(pista) + '.jpg')
            self.imgpista_colores = funciones.cargar_imagem('pista-' + str(pista) + '.jpg')
            self.num_voltas = 1

            # largada
            self.tempo_largada = 0
            self.largada = False
            self.tamano_letras = 200
            if num_pista == 1:
                self.posicaop1 = Vector(850, 200)
                self.posicaop2 = Vector(830, 200)
                self.rotacao = 180.
            elif num_pista == 2:
                self.posicaop1 = Vector(800, 630)
                self.posicaop2 = Vector(7850, 670)
                self.rotacao = 180.
            elif num_pista == 3:
                self.posicaop1 = Vector(900, 50)
                self.posicaop2 = Vector(885, 50)
                self.rotacao = 180.

        def conta_tempo_largada(self, tf, ti, numero):
            """ o nome já diz tudo """
            if tf > self.tempo_largada >= ti:
                escribe_en_pantalla(numero, darkred, self.tamano_letras, (500, 334))

        def larga(self):
            """ exibe na tela a mensagem de largada e permite a movimentação dos carros (self.largada) """
            if self.tempo_largada < fps * 10:
                self.tempo_largada += 1

            for i in range(1, 6):
                self.conta_tempo_largada(fps * i + fps, fps * i, "%d" % (6 - i))

            if fps * 7 > self.tempo_largada >= fps * 6:
                escribe_en_pantalla('GO!', darkred, self.tamano_letras, (500, 334))
                self.largada = True

        #Se cargan las imagenes de los colores
        def pistas_colores(self):
            pantalla.blit(self.imgpista_colores, (0, 0))

        def carrega_pista(self):
            """ carrega a imagem da pista escolhida pelo usuário que fica em cima da imagem do mapa de cores """
            pantalla.blit(self.imgpista, (0, 0))

    class Carro(Sprite):
        def __init__(self, player, cor, *grupos):
            """ variáveis padrão de inicialização da classe """
            Sprite.__init__(self, *grupos)

            # teclas
            self.acelerador, self.freio = tecla('acelera', player), tecla('freno', player)
            self.esquerda, self.direita = tecla('izquierda', player), tecla('derecha', player)

            # cor do carro
            self.imgscar = funciones.cargar_imagem(f"car{cor}.png",1)
            self.imgcar = self.imgscar

            # velocidade/deslocamento/acelera
            self.velocidade_carro = 0
            self.velocidade_max = 200.
            self.rotacao = pista.rotacao
            self.velocidade_rotacao = 90.  # graus por segundo

            # posicao inicial dos carros na pista e antes de uma batida
            if player == 1:
                self.posicao = pista.posicaop1
            else:
                self.posicao = pista.posicaop2
            self.pos_antes_batida = self.posicao.copy()

            # conta voltas
            self.checks = 0
            self.voltas = 0
            self.melhor_volta = "-"
            self.ultima_volta = "-"
            self.cronometro = pygame.time.Clock()

            # life
            self.life = 100
            self.somexplosao = pygame.mixer.Sound('sounds/explode.wav')
            self.imgsexplosao = funciones.cargar_imagem('explosion.png', 1, [(x, 0, 50, 50) for x in range(0, 400, 50)])
            self.imgexplosao = self.imgsexplosao[0]
            self.explode = False
            self.conta_tempo_morte = fps * 5
            self.puntos = 0

            #Sonidos
            self.acelerasn = pygame.mixer.Sound('sounds/aceleracion_1.wav')

            # retangulo do sprite
            self.rect = Rect(self.posicao.x - self.imgcar.get_width() / 2,
                             self.posicao.y - self.imgcar.get_height() / 2, \
                             self.imgcar.get_width(), self.imgcar.get_height())


            self.sombatida = pygame.mixer.Sound('sounds/warning.wav')
            self.sombatida.set_volume(0.2)

        def muda_textura(self, pressed_key):
            #Usamos la imagen del carro
            self.imgcar = self.imgscar

            if self.life <= 0:
                self.imgcar = self.imgexplosao

        def colide(self):
            """ detecta a colisão do carro com os extremos da tela e com os obstáculos da pista """
            x, y = tuple(self.posicao)

            if x <= 10:
                x = 10
            elif x >= ancho - 10:
                x = ancho - 10

            if y <= 10:
                y = 10
            elif y >= alto - 10:
                y = alto - 10

            if pista.imgpista_colores.get_at((int(self.posicao.x), int(self.posicao.y))) == amarillo:
                self.sombatida.play()
                y -= 2
            elif pista.imgpista_colores.get_at((int(self.posicao.x), int(self.posicao.y))) == rojo:
                self.sombatida.play()
                y += 2
            elif pista.imgpista_colores.get_at((int(self.posicao.x), int(self.posicao.y))) == rojo:
                self.sombatida.play()
                x -= 2
            elif pista.imgpista_colores.get_at((int(self.posicao.x), int(self.posicao.y))) == amarillo:
                self.sombatida.play()
                x += 2

            if pista.imgpista_colores.get_at((int(self.posicao.x), int(self.posicao.y))) in [amarillo, rojo]:
                self.perde_velocidade(50, -25)
                self.perde_life(10)

            self.posicao = Vector(x, y)

        def acelera(self, pressed_key):
            #Para acelerar el carro
            if [pressed_key[self.acelerador], pressed_key[self.freio]] == [0, 0] or self.explode:
                if self.velocidade_carro > 0:
                    self.velocidade_carro -= 5
                elif self.velocidade_carro < 0:
                    self.acelerasn.play()
                    self.velocidade_carro += 5

            if pista.largada and not self.explode:
                if pressed_key[self.acelerador]:
                    if self.velocidade_carro < 1000:
                        self.velocidade_carro += 20

                if pressed_key[self.freio]:
                    if 0 < self.velocidade_carro <= 1000:
                        self.velocidade_carro -= 20
                    elif -200 <= self.velocidade_carro <= 0:
                        self.velocidade_carro -= 10

        def perde_life(self, dano):
            #El jugador pierde vidas
            if self.life > 0 and self.conta_tempo_morte == fps * 5:
                self.life -= dano

        def morre(self, grupo):
            #Con el efecto de explocion el carro desaparece
            if self.life <= 0 or fps * 2 >= self.conta_tempo_morte >= 0:
                grupo.remove(self)

                if fps * 5 >= self.conta_tempo_morte >= (fps * 5) - 5:
                    self.imgexplosao = self.imgsexplosao[0]
                    self.somexplosao.play()

                elif (fps * 5) - 5 >= self.conta_tempo_morte >= (fps * 5) - 10:
                    self.imgexplosao = self.imgsexplosao[1]

                elif (fps * 5) - 10 >= self.conta_tempo_morte >= (fps * 5) - 15:
                    self.imgexplosao = self.imgsexplosao[2]

                elif (fps * 5) - 15 >= self.conta_tempo_morte >= (fps * 5) - 20:
                    self.imgexplosao = self.imgsexplosao[3]

                elif (fps * 5) - 20 >= self.conta_tempo_morte >= (fps * 5) - 25:
                    self.imgexplosao = self.imgsexplosao[4]

                elif (fps * 5) - 25 >= self.conta_tempo_morte >= (fps * 5) - 30:
                    self.imgexplosao = self.imgsexplosao[5]

                elif (fps * 5) - 30 >= self.conta_tempo_morte >= (fps * 5) - 35:
                    self.imgexplosao = self.imgsexplosao[6]
                    self.velocidade_carro = 0

                if self.life <= 0:
                    self.explode = True

                if self.conta_tempo_morte > 0:
                    self.conta_tempo_morte -= 1

                if self.conta_tempo_morte <= fps * 2:
                    self.add(grupo)
                    self.life = 500
                    self.explode = False
                    if self.conta_tempo_morte <= 0:
                        self.conta_tempo_morte = fps * 5

        def perde_velocidade(self, limite, limite_re):
            #Regula la velocidad del jugador
            if self.velocidade_carro > limite:
                self.velocidade_carro-= 50
            elif -600 < self.velocidade_carro < limite_re:
                self.velocidade_carro+= 35

        def rotaciona_carro(self, pressed_key):
            #Par ael movimiento del carro
            self.direcao_rotacao = 0.

            if self.velocidade_carro != 0:
                if self.velocidade_carro < 0:
                    if pressed_key[self.esquerda]:
                        self.direcao_rotacao = -1
                    elif pressed_key[self.direita]:
                        self.direcao_rotacao = +1
                else:
                    if pressed_key[self.esquerda]:
                        self.direcao_rotacao = +1
                    elif pressed_key[self.direita]:
                        self.direcao_rotacao = -1

        def rotaciona_imgcarro(self):
            """ rotaciona a imagem do carro de acordo com a ação realizadaa pelo usuário """
            self.imgcar = pygame.transform.rotate(self.imgcar, self.rotacao)
            self.w, self.h = self.imgcar.get_size()
            desenha_carro = Vector(self.posicao.x - self.w/2, self.posicao.y - self.h/2)
            pantalla.blit(self.imgcar, desenha_carro)

        def movimenta(self, time_passed_seconds):
            #Movimiento normal de carro
            self.direcao_movimento = +(self.velocidade_carro/1000.)
            self.rotacao += self.direcao_rotacao * self.velocidade_rotacao * time_passed_seconds
            if self.rotacao >= 360:
               self.rotacao = self.rotacao - 360
            elif self.rotacao < 0:
               self.rotacao = 360 + self.rotacao
            heading_x = sin(self.rotacao*pi/180.0)
            heading_y = cos(self.rotacao*pi/180.0)
            heading = Vector(heading_x, heading_y)
            heading *= self.direcao_movimento
            self.posicao += heading * self.velocidade_max * time_passed_seconds

        def atualiza_rect(self):
            """ atualiza a representação do carro (retângulo) de acordo com a sua posição atual """
            self.rect = Rect(self.posicao.x - self.imgcar.get_width()/2, self.posicao.y - \
                              self.imgcar.get_height()/2, self.imgcar.get_width(), self.imgcar.get_height())

        def completa_volta(self, pista):
            #Verifica un avuelta
            if pista.imgmapa_cores.get_at((int(self.posicao.x), int(self.posicao.y))) in [meta]:

                self.ultima_volta_mil = self.cronometro.tick(fps)
                self.ultima_volta = self.ultima_volta_mil / 1000.0

                if self.melhor_volta == "-":
                    self.melhor_volta = self.ultima_volta

                if self.ultima_volta < self.melhor_volta:
                    self.melhor_volta = self.ultima_volta

                self.voltas += 1
                self.checks = 0
                #Esta sera la de los puntos
                self.puntos += 10
                if self.voltas == pista.num_voltas:
                    return True

        def testa_batida(self, outro, grupo):
            """ verifica batidas entre os carros e produz o os efeitos de movimento de colisão """
            self.atualiza_rect()
            outro.atualiza_rect()

            x, y = tuple(self.posicao)
            x1, y1 = tuple(self.pos_antes_batida)
            if outro in pygame.sprite.spritecollide(self, grupo, False):
                self.sombatida.play()
                x, y = x1, y1
                if (45 <= self.rotacao <= 135 and 45 <= outro.rotacao <= 135) or \
                        (225 < self.rotacao < 315 and 225 < outro.rotacao < 315) or \
                        (135 < self.rotacao <= 225 and 135 < outro.rotacao <= 225) or \
                        ((315 < self.rotacao < 360 or 0 < self.rotacao < 45) and \
                         (315 < outro.rotacao < 360 or 0 < outro.rotacao < 45)):

                    outro.velocidade_carro += self.velocidade_carro / 3
                    outro.velocidade_carro -= outro.velocidade_carro % 10
                    self.velocidade_carro -= self.velocidade_carro / 2
                    self.velocidade_carro -= self.velocidade_carro % 10

                elif (225 < self.rotacao < 315 and 45 <= outro.rotacao <= 135) or \
                        (45 <= self.rotacao <= 135 and 225 < outro.rotacao < 315) or \
                        (135 < self.rotacao <= 225 and (315 < outro.rotacao < 360 or \
                                                        0 < outro.rotacao < 45)) or ((315 < self.rotacao < 360 \
                                                                                      or 0 < self.rotacao < 45) and 135 < outro.rotacao <= 225):

                    outro.velocidade_carro -= self.velocidade_carro / 3
                    outro.velocidade_carro -= outro.velocidade_carro % 10
                    self.velocidade_carro -= self.velocidade_carro / 2
                    self.velocidade_carro -= self.velocidade_carro % 10

                elif ((self.velocidade_carro > 0 and 45 < self.rotacao < 135) or \
                      (self.velocidade_carro < 0 and 225 < self.rotacao < 315)) and \
                        (135 < outro.rotacao <= 225 or (315 < outro.rotacao < 360 or 0 < outro.rotacao < 45)):

                    self.velocidade = self.velocidade_carro / 4
                    outro.posicao.x += 2

                elif ((self.velocidade_carro < 0 and 45 < self.rotacao < 135) or \
                      (self.velocidade_carro > 0 and 225 < self.rotacao < 315)) and \
                        (135 < outro.rotacao <= 225 or (315 < outro.rotacao < 360 or 0 < outro.rotacao < 45)):

                    self.velocidade = self.velocidade_carro / 4
                    outro.posicao.x -= 2

                elif ((135 < self.rotacao < 225 and self.velocidade_carro > 0) or \
                      ((315 < self.rotacao < 360 or 0 < self.rotacao < 45) and \
                       self.velocidade_carro < 0)) and (45 <= outro.rotacao <= 135 or 225 < outro.rotacao < 315):

                    self.velocidade = self.velocidade_carro / 4
                    outro.posicao.y -= 2

                elif ((315 < self.rotacao < 360 or 0 < self.rotacao < 45) and \
                      self.velocidade_carro > 0 or (135 < self.rotacao < 225 and \
                                                    self.velocidade_carro < 0)) and (
                        45 <= outro.rotacao <= 135 or 225 < outro.rotacao < 315):

                    self.velocidade = self.velocidade_carro / 4
                    outro.posicao.y += 2

                elif self.rect.collidepoint(outro.posicao):
                    self.perde_life(500)

                self.perde_life(5)

            else:
                self.pos_antes_batida = self.posicao

            self.posicao = Vector(x, y)

        def acoes(self, grupo):
            """ metoto responsável por atualizar todas as ações do carro """
            self.colide()
            self.muda_textura(pressed_key)
            self.acelera(pressed_key)
            self.rotaciona_carro(pressed_key)
            self.rotaciona_imgcarro()
            #self.pisa_brita()
            self.movimenta(time_passed_seconds)
            self.morre(grupo)



    #pista = Image("img", "Pista1.jpg", (ancho, alto), pantalla, window_rect)
    pygame.init()

    #pygame.mixer.music.load(musicas[num_musica])
    #pygame.mixer.music.play(-1)

    pista = Pista(num_pista)
    carrop1 = Carro(1, carro1)
    displayp1 = Display(1)
    grupo1 = pygame.sprite.GroupSingle(carrop1)

    clock = pygame.time.Clock()

    sairmenu = False

    while True:

        time_passed = clock.tick(fps)
        time_passed_seconds = time_passed / 1000.0

        displayp1.exibe_display()
        if num_jugadores > 1:
            num_jugadores.exibe_display()

        pygame.display.update()


        #Parte logica
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

        #region Datos para el cronometro
        #Parte de dibujo

        pressed_key = pygame.key.get_pressed()

        #Ver las pistas
        pista.pistas_colores()
        pista.carrega_pista()

        carrop1.acoes(grupo1)

        pista.larga()
        #pista.place()
        #pantalla.blit(info, (5, 5))
        #segundos = str(int(pygame.time.get_ticks()/1000))
        #minnutos = 0
        #contador = fuente.render(segundos,0,(155,155,230))
        #pantalla.blit(contador, (300, 5))
        #endregion


        pygame.display.flip()
