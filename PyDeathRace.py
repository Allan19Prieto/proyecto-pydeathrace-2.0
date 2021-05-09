import pygame
#Hola
class pydeathrace:
    def __init__(self):
        self._init_pygame()
        self.pantalla = pygame.display.set_mode((800,600))


    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_UP
            ):
                quit()

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.pantalla.fill((0, 0, 255))
        self.rectangulo = pygame.draw.rect(self.pantalla, (255,255,255), [160, 50, 160, 40])
        pygame.display.flip()
