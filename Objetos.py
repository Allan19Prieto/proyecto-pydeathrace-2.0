from Clases import *
import os
import pygame
from pygame.locals import*
import sys
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

class Car():
    def __init__(self, x, y, angle = 0.0, length=4, max_steering=100, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 11
        self.brake_deceleration = 10
        self.free_deceleration = 30

        self.acceleration = 0.0
        self.steering = 0.0

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

