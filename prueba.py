import pygame

pygame.init()

#tocar musica inicial
pygame.mixer.music.load("sounds/menu.wav")
pygame.mixer.music.play(-1)

# define as propriedades da janela do jogo
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Nerd N\' Roll Rancing 3000')

while True:


    # atualiza tela
    pygame.display.update()