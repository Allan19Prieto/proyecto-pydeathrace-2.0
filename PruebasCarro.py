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
        self.vidas = 100

        #Para mover un rectangulo
        self.rectangulo = 100
        self.x = 950
        self.y = 150


        width = 1365
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.window_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

        self.car = Car(30, 5)

        self.pista1 = Image("img", "Pista-1.jpg", (width, height), self.screen, self.window_rect)
        self.pista2 = Image("img", "Pista2.jpg", (width, height), self.screen, self.window_rect)
        self.pista3 = Image("img", "Pista3.jpg", (width+10, height+10), self.screen, self.window_rect)
        self.carro = Image("img", "car12.png", (67, 37), self.screen, self.window_rect)
        self.vpi = self.pista1

        self.fps = 30

        self.punto_text = Text(self.screen, self.window_rect, "game_font", 40, white, "Vidas: "+ str(self.car.vidas), darkred)

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "img/car12.png")
        car_image = pygame.image.load(image_path)

        ppu = 32
        clock = pygame.time.Clock()

        while not self.exit:
            #time_passed = clock.tick(self.fps)
            #time_passed_seconds = time_passed / 1000.0
            dt = self.clock.get_time() / 1000.0


            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()
            mousex , mousey = pygame.mouse.get_pos()
            #self.rect = image_path.get_rect()

            if pressed[pygame.K_UP]:
                self.car.acelera(dt)

            elif pressed[pygame.K_DOWN]:
                self.car.reversa(dt)

            elif pressed[pygame.K_SPACE]:
                self.car.precionaFreno(dt)
            else:
                self.car.noprecionaFreno(dt)

            self.car.acceleration = max(- self.car.max_acceleration, min(self.car.acceleration, self.car.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                self.car.derecha(dt)
            elif pressed[pygame.K_LEFT]:
                self.car.izquierda(dt)
            else:
                self.car.steering = 0
            self.car.steering = max(-self.car.max_steering, min(self.car.steering, self.car.max_steering))

            # Para averiguar el color
            if self.screen.get_at((int(self.car.position.x) * 31, int(self.car.position.y) * 31)) == (color_fuera_pista):
                self.vidas -= 1
                self.car.perderVida(1)

            if self.vidas <= 50:
                self.vpi = self.pista2


            # Logic
            self.car.update(dt)

            # Drawing
            self.screen.fill((0, 0, 0))
            self.vpi.place()
            self.carro.place()
            #print(self.carro.rect)
            self.punto_text.place(True, (600, -280))

            #************************Rectangulo******************************
            pygame.draw.rect(self.screen, white, [self.x, self.y, 50, 50], 0)
            #self.carro.place(True, (self.x, self.y))

            if self.y == 150:
                self.x -= 5
            if self.x == 170:
                self.y += 5
            if self.y == 500:
                self.x += 5
            if self.x == 1150:
                self.y -= 5

            print("Rectangulo: ", self.x, self.y)



            rotated = pygame.transform.rotate(car_image, self.car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, self.car.position * ppu - (rect.width / 2, rect.height / 2))

            print(mousex, mousey)
            print("Carro:", self.car.position)

            print("Color:" , self.screen.get_at((mousex, mousey)))

            #print(self.rect.x)
            #if self.screen.get_at((mousex, mousey)) == (white):
             #   print("Esta en color blanco")
            #else:
             #   print("Esta en color negro")

            print(self.vidas)

            pygame.display.flip()
            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()