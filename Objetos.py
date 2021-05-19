from Clases import *
import os
import pygame
from pygame.locals import*
import sys
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

class Car():
    def __init__(self, x, y,   angle = 0.0, length=4, max_steering=100, max_acceleration=5.0):
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

    def acelera(self, dt):
        if self.velocity.x < 0:
            self.acceleration = self.brake_deceleration
        else:
            self.acceleration += 15 * dt

