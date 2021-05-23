import pygame
from pygame.locals import *
import time
import random


class Chocolate:
    #wymiary czekolady to 20x20
    def __init__(self, board):
        self.board = board
        self.image = pygame.image.load('chocolate.PNG').convert()
        self.x = 60
        self.y = 60

    def draw(self):
        self.board.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def change_place(self):
        self.x = random.randint(1, 24)*20
        self.y = random.randint(1, 19)*20


class Snake:
    # wymiary głowy węża to 20x20
    def __init__(self, board, size):
        self.board = board
        self.image = pygame.image.load('square.PNG').convert()
        self.direction = "right"

        self.size = size
        self.x = [20]*size
        self.y = [20]*size

    def draw(self):
        self.board.fill((245, 170, 66))
        for i in range(self.size):
            self.board.blit(self.image, (self.x[i], self.y[i]))
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

        for i in range(self.size-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= 20
        if self.direction == "down":
            self.y[0] += 20
        if self.direction == "left":
            self.x[0] -= 20
        if self.direction == "right":
            self.x[0] += 20
        self.draw()

    def bigger(self):
       self.size += 1
       self.x.append(-1)
       self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 400))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.chocolate = Chocolate(self.surface)
        self.chocolate.draw()

    def play(self):
        self.snake.creep()
        self.chocolate.draw()
        self.score()
        pygame.display.flip()
        if self.collision_finder(self.snake.x[0], self.snake.y[0], self.chocolate.x, self.chocolate.y):
            self.snake.bigger()
            self.chocolate.change_place()

    def score(self):
        font = pygame.font.SysFont('Helvetica', 22)
        result = font.render(f"Score: {self.snake.size-1}", True, (0, 0, 205))
        self.surface.blit(result, (420, 5))

    def collision_finder(self, a1, b1, a2, b2):
        if a1 >= a2 and a1 < a2 + 20:
            if b1 >= b2 and b1 < b2 + 20:
                return True
        return False

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
            self.play()
            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.go()

