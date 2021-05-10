import pygame
from pygame.locals import *


def first_snake():

    surface.blit(fs, (x, y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((600, 600))
    surface.fill((245, 170, 66))

    fs = pygame.image.load('gituuu.PNG').convert()
    x = 200
    y = 200
    surface.blit(fs, (x, y))

    pygame.display.flip()

    surface.blit(fs, (x, y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == K_UP or event.key == K_w:
                    y -= 20
                    first_snake()
                if event.key == K_DOWN or event.key == K_s:
                    y += 20
                    first_snake()
                if event.key == K_LEFT or event.key == K_a:
                    x -= 20
                    first_snake()
                if event.key == K_RIGHT or event.key == K_d:
                    x += 20
                    first_snake()
                else:
                    pass

first_snake()
