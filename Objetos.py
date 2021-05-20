from Clases import *
import os
import pygame
from pygame.locals import*
import sys
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

class Car():
    def __init__(self, x, y, angle = 0, length=4, max_steering=100, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 11
        self.brake_deceleration = 10
        self.free_deceleration = 30

        self.acceleration = 0
        self.steering = 0

        #Vidas
        self.vidas = 100

        self.mure = pygame.mixer.Sound("sounds/explode.wav")
        #self.conta_tempo_morte = fps * 5

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt

    def perderVida(self, dan):
        if self.vidas >= 0:
            self.vidas -= dan

    #El carro va para adelante
    def acelera(self, dt):
        if self.velocity.x < 0:
            self.acceleration = self.brake_deceleration
        else:
            self.acceleration += 15 * dt

    #El carro va para atras
    def reversa(self, dt):
        if self.velocity.x > 0:
            self.acceleration = - self.brake_deceleration
        else:
            self.acceleration -= 10 * dt

    #Carro se mueve a la derecha
    def derecha(self, dt):
        self.steering -= 120 * dt

    #Carro se mueve a la izquirda
    def izquierda(self, dt):
        self.steering += 120 * dt

    def precionaFreno(self, dt):
        if abs(self.velocity.x) > dt * self.brake_deceleration:
            self.acceleration = - copysign(self.brake_deceleration, self.velocity.x)
        else:
            self.acceleration = - self.velocity.x / dt

    def noprecionaFreno(self, dt):
        if abs(self.velocity.x) > dt * self.free_deceleration:
            self.acceleration = -copysign(self.free_deceleration, self.velocity.x)
        else:
            if dt != 0:
                self.acceleration = - self.velocity.x / dt

'''
    class Pista():
        def __init__(self, pista):
            """ variáveis padrão de inicialização da classe """
            self.imgpista = funciones.carrega_imagem('pista' + str(pista) + '.png')
            self.imgmapa_cores = funciones.carrega_imagem('pista_mapa' + str(pista) + '.png')
            #self.num_voltas = num_voltas

            # largada
            self.tempo_largada = 0
            self.largada = False
            self.tamanho_fonte = 100
            if num_pista == 1:
                self.posicaop1 = Vector(565, 135)
                self.posicaop2 = Vector(465, 165)
                self.rotacao = 90.
            elif num_pista == 2:
                self.posicaop1 = Vector(565, 630)
                self.posicaop2 = Vector(465, 670)
                self.rotacao = 90.

            # arvores
            self.arvores = funcoes.carrega_imagem('pista_arvores' + str(pista) + '.png', 1)

        def conta_tempo_largada(self, tf, ti, numero):
            """ o nome já diz tudo """
            if tf > self.tempo_largada >= ti:
                escreve_tela(numero, branco, self.tamanho_fonte, (500, 334))

        def larga(self):
            """ exibe na tela a mensagem de largada e permite a movimentação dos carros (self.largada) """
            if self.tempo_largada < fps * 10:
                self.tempo_largada += 1

            for i in range(1, 6):
                self.conta_tempo_largada(fps * i + fps, fps * i, "%d" % (6 - i))

            if fps * 7 > self.tempo_largada >= fps * 6:
                escreve_tela('ROCK AND ROLL!!!', branco, self.tamanho_fonte, (200, 334))
                self.largada = True

        def carrega_mapa_cores(self):
            """ carrega o mapa de cores da pista responsável pelo controle de colisões de obstáculos """
            screen.blit(self.imgmapa_cores, (0, 0))

        def carrega_pista(self):
            """ carrega a imagem da pista escolhida pelo usuário que fica em cima da imagem do mapa de cores """
            screen.blit(self.imgpista, (0, 0))

        def mostra_arvores(self):
            """ carrega a imagem das árvores """
            screen.blit(self.arvores, (0, 0)) '''
