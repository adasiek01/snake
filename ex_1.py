import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, board):
        self.board = board
        self.fs = pygame.image.load('gituuu.PNG').convert()
        self.x = 280
        self.y = 250
        self.direction = "up"

    def draw(self):
        self.board.fill((245, 170, 66))
        self.board.blit(self.fs, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def creep(self):
        if self.direction == "up":
            self.y -= 10
        if self.direction == "down":
            self.y += 10
        if self.direction == "left":
            self.x -= 10
        if self.direction == "right":
            self.x += 10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600, 600))
        self.surface.fill((245, 170, 66))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def go(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == K_UP or event.key == K_w:
                        self.snake.move_up()

                    if event.key == K_DOWN or event.key == K_s:
                        self.snake.move_down()

                    if event.key == K_LEFT or event.key == K_a:
                        self.snake.move_left()

                    if event.key == K_RIGHT or event.key == K_d:
                        self.snake.move_right()
                    else:
                        pass
            self.snake.creep()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.go()

