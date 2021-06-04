import pygame
from pygame.locals import *
import time
import random


class Chocolate:
    #wymiary czekolady to 20x20
    def __init__(self, board):
        self.board = board
        self.image = pygame.image.load('images/chocolate.PNG').convert()
        self.x = 60
        self.y = 60

    def draw(self):
        self.board.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def change_place(self):
        self.x = random.randint(1, 24)*20
        self.y = random.randint(1, 19)*20

class Bomb:
    #wymiary bomby to 20x20
    def __init__(self, board):
        self.board = board
        self.image = pygame.image.load('images/bomb.PNG').convert()


    def draw(self):
        self.board.blit(self.image, (120, 100))
        self.board.blit(self.image, (360, 100))
        self.board.blit(self.image, (120, 260))
        self.board.blit(self.image, (360, 260))
        self.board.blit(self.image, (240, 180))
        pygame.display.flip()



class Snake:
    # wymiary głowy węża to 20x20
    def __init__(self, board, size):
        self.board = board
        self.image = pygame.image.load('images/square.PNG').convert()
        self.direction = "right"

        self.size = size
        self.x = [20]*size
        self.y = [20]*size

    def draw(self):
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

    def out_of_x_left(self):
        self.x[0] = 500

    def out_of_x_right(self):
        self.x[0] = -20

    def out_of_y_up(self):
        self.y[0] = 400

    def out_of_y_down(self):
        self.y[0] = -20



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake and Chocolate")
        pygame.mixer.init()
        self.music()
        self.surface = pygame.display.set_mode((500, 400))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.chocolate = Chocolate(self.surface)
        self.chocolate.draw()
        self.bomb = Bomb(self.surface)
        self.bomb.draw()

    def collision_finder(self, a1, b1, a2, b2):
        if a1 >= a2 and a1 < a2 + 20:
            if b1 >= b2 and b1 < b2 + 20:
                return True
        return False

    def sound(self, sound):
        sound_v = pygame.mixer.Sound(f"{sound}.mp3")
        pygame.mixer.Sound.play(sound_v)

    def music(self):
        pygame.mixer.music.load("MUSIC/beach.mp3")
        pygame.mixer.music.play(-1)

    def background(self):
        bgr = pygame.image.load("images/backgr.png")
        self.surface.blit(bgr, (0, 0))

    def play(self):
        self.background()
        self.snake.creep()
        self.chocolate.draw()
        self.bomb.draw()
        self.score()
        pygame.display.flip()

        #poza planszą

        if self.snake.x[0] == -20 and self.snake.direction == "left":
            self.snake.out_of_x_left()
        if self.snake.x[0] == 500 and self.snake.direction == "right":
            self.snake.out_of_x_right()
        if self.snake.y[0] == -20 and self.snake.direction == "up":
            self.snake.out_of_y_up()
        if self.snake.y[0] == 400 and self.snake.direction == "down":
            self.snake.out_of_y_down()

        pygame.display.flip()
        #zbieranie punktów
        if self.collision_finder(self.snake.x[0], self.snake.y[0], self.chocolate.x, self.chocolate.y):
            self.sound("MUSIC/haps")
            self.snake.bigger()
            self.chocolate.change_place()
            for i in range(self.snake.size):
                if self.chocolate.x == self.snake.x[i] and self.chocolate.y == self.snake.y[i]:
                    self.chocolate.change_place()
                if self.chocolate.x == 120 and self.chocolate.y == 100:
                    self.chocolate.change_place()
                if self.chocolate.x == 360 and self.chocolate.y == 100:
                    self.chocolate.change_place()
                if self.chocolate.x == 240 and self.chocolate.y == 180:
                    self.chocolate.change_place()
                if self.chocolate.x == 120 and self.chocolate.y == 260:
                    self.chocolate.change_place()
                if self.chocolate.x == 360 and self.chocolate.y == 260:
                    self.chocolate.change_place()


        #koniec gry
        for i in range(1, self.snake.size):
            if self.collision_finder(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.sound("MUSIC/death")
                self.top_scores()
                raise

        if self.collision_finder(self.snake.x[0], self.snake.y[0], 120, 100):
            self.sound("MUSIC/death")
            self.top_scores()
            raise
        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 360, 100):
            self.sound("MUSIC/death")
            self.top_scores()
            raise
        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 240, 180):
            self.sound("MUSIC/death")
            self.top_scores()
            raise
        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 120, 260):
            self.sound("MUSIC/death")
            self.top_scores()
            raise
        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 360, 260):
            self.sound("MUSIC/death")
            self.top_scores()
            raise


    def score(self):
        font = pygame.font.SysFont('Helvetica', 22)
        result = font.render(f"Score: {self.snake.size-1}", True, (75, 0, 130))
        self.surface.blit(result, (400, 5))

    def top_scores(self):
        f = open("top_scores.txt", "a")
        f.write(str(self.snake.size-1) + "\n")
        f.close()
        f = open("top_scores.txt", "r")
        lines = f.readlines()
        f.close()
        top = []
        for i in lines:
            top.append(i[:-1])
        return top[-5:]


    def the_end(self):
        self.background()
        font = pygame.font.SysFont('Helvetica', 25)
        message = font.render(f"You've lost, your final score is: {self.snake.size-1}", True, (255, 255, 0))
        self.surface.blit(message, (100, 150))
        message2 = font.render(f"Click 'ENTER' to play again", True, (255, 255, 0))
        self.surface.blit(message2, (100, 200))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def restart(self):
        self.snake = Snake(self.surface, 1)
        self.chocolate = Chocolate(self.surface)


    def go(self):
        stop = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        stop = not stop
                    if not stop:
                        if event.key == K_UP or event.key == K_w:
                            if 500 > self.snake.x[0] > -20 and 400 > self.snake.y[0] > -20:
                                self.snake.move_up()

                        if event.key == K_DOWN or event.key == K_s:
                            if 500 > self.snake.x[0] > -20 and 400 > self.snake.y[0] > -20:
                                self.snake.move_down()

                        if event.key == K_LEFT or event.key == K_a:
                            if 500 > self.snake.x[0] > -20 and 400 > self.snake.y[0] > -20:
                                self.snake.move_left()

                        if event.key == K_RIGHT or event.key == K_d:
                            if 500 > self.snake.x[0] > -20 and 400 > self.snake.y[0] > -20:
                                self.snake.move_right()
                        else:
                            pass

            try:
                if not stop:
                    self.play()
            except:
                self.the_end()
                stop = True
                self.restart()
            time.sleep(0.1)






if __name__ == "__main__":
    game = Game()
    game.go()



