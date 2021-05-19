from Clases import *
import os
import pygame
from pygame.locals import*
import sys
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

from Objetos import Car

white = (255, 255, 255, 255)
color_fuera_pista = (231, 134, 81, 255)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Prueba Carro")
        width = 1365
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.window_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
        self.pista1 = Image("img", "Pista1.jpg", (width, height), self.screen, self.window_rect)
        self.pista2 = Image("img", "Pista2.jpg", (width, height), self.screen, self.window_rect)
        self.pista3 = Image("img", "Pista3.jpg", (width+10, height+10), self.screen, self.window_rect)
        self.carro = Image("img", "car12.png", (67, 37), self.screen, self.window_rect)
        self.vpi = self.pista1
        self.vidas = 100


    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "img/car12.png")
        car_image = pygame.image.load(image_path)
        car = Car(30, 5)
        ppu = 32
        #poi = car_image.get_rect()



        #pocar = car.get_rect()

        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()
            mousex , mousey = pygame.mouse.get_pos()
            #self.rect = image_path.get_rect()

            if pressed[pygame.K_UP]:
                car.acelera(dt)
            elif pressed[pygame.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:
                    car.acceleration -= 10 * dt

            elif pressed[pygame.K_SPACE]:
                if abs(car.velocity.x) > dt * car.brake_deceleration:
                    car.acceleration = -copysign(car.brake_deceleration, car.velocity.x)
                else:
                    car.acceleration = -car.velocity.x / dt
            else:
                if abs(car.velocity.x) > dt * car.free_deceleration:
                    car.acceleration = -copysign(car.free_deceleration, car.velocity.x)
                else:
                    if dt != 0:
                        car.acceleration = -car.velocity.x / dt
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                car.steering -= 120 * dt
            elif pressed[pygame.K_LEFT]:
                car.steering += 120 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))

            # Logic
            car.update(dt)

            # Drawing
            self.screen.fill((0, 0, 0))
            self.pista3.place()
            self.carro.place()
            #print(self.carro.rect)
            rotated = pygame.transform.rotate(car_image, car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, car.position * ppu - (rect.width / 2, rect.height / 2))
            pygame.display.flip()

            print(mousex, mousey)
            print("Carro:", car.position)

            print("Color:" , self.screen.get_at((mousex, mousey)))

            if self.screen.get_at((int(car.position.x)*31, int(car.position.y)*31)) == (color_fuera_pista):
                self.vidas -= 1

            if self.vidas <= 50:
                self.vpi = self.pista2


            #print(self.rect.x)
            #if self.screen.get_at((mousex, mousey)) == (white):
             #   print("Esta en color blanco")
            #else:
             #   print("Esta en color negro")
            print(self.vidas)


            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()