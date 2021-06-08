import pygame
from pygame.locals import *
import time
import random
from pygame_widgets import Button


class Chocolate:
    """
    the class that creates chocolate object
    """
    def __init__(self, board):
        """
        the constructor takes board parameter
        :param board: board of the game
        """
        self.board = board
        self.image = pygame.image.load('images/chocolate.PNG').convert()
        self.x = 60
        self.y = 60

    def draw(self):
        """
        the method that draws the chocolate object
        """
        self.board.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def change_place(self):
        """
        the method that changes the place of the chocolate object
        """
        self.x = random.randint(1, 24)*20
        self.y = random.randint(1, 19)*20


class Bomb:
    """
    the class that creates the bomb object
    """
    def __init__(self, board):
        """
        the constructor takes board parameter, that is board of the game
        :param board:
        """
        self.board = board
        self.image = pygame.image.load('images/bomb.PNG').convert()

    def draw(self):
        """
        the method that draws the bomb object
        """
        self.board.blit(self.image, (120, 100))
        self.board.blit(self.image, (360, 100))
        self.board.blit(self.image, (120, 260))
        self.board.blit(self.image, (360, 260))
        self.board.blit(self.image, (240, 180))
        pygame.display.flip()


class Snake:
    """
    the class that creates the snake object
    """
    def __init__(self, board, size):
        """
        the constructor takes board parameter and size parameter
        :param board: is board of the game
        :param size: length of the snake
        """
        self.board = board
        self.image = pygame.image.load('images/square.PNG').convert()
        self.direction = "right"

        self.size = size
        self.x = [20]*size
        self.y = [20]*size

    def draw(self):
        """
        the method that draws the snake object
        """
        for i in range(self.size):
            self.board.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        """
        the method that makes snake go up
        """
        self.direction = "up"

    def move_down(self):
        """
        the method that makes snake go down
        """
        self.direction = "down"

    def move_left(self):
        """
        the method that makes snake go left
        """
        self.direction = "left"

    def move_right(self):
        """
        the method that makes snake go right
        """
        self.direction = "right"

    def creep(self):
        """
        the method that enables snake to move on the board
        """
        for i in range(self.size-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "up":
            self.y[0] -= 20
        elif self.direction == "down":
            self.y[0] += 20
        elif self.direction == "left":
            self.x[0] -= 20
        elif self.direction == "right":
            self.x[0] += 20
        self.draw()

    def bigger(self):
        """
        the method that enables snake to grow
        """
        self.size += 1
        self.x.append(-1)
        self.y.append(-1)

    def out_of_x_left(self):
        """
        the method that moves snake on the right site of the board
        """
        self.x[0] = 500

    def out_of_x_right(self):
        """
        the method that moves snake on the left site of the board
        """
        self.x[0] = -20

    def out_of_y_up(self):
        """
        the method that moves snake on the top site of the board
        """
        self.y[0] = 400

    def out_of_y_down(self):
        """
        the method that moves snake on the bottom site of the board
        """
        self.y[0] = -20


class Game:
    """
    the class that creates the gameplay
    """
    def __init__(self, mode):
        """
        the constructor that takes mode parameter
        :param mode: level of difficulty
        """
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
        self.mode = mode

    def collision_finder(self, a1, b1, a2, b2):
        """
        the method that checks if collision exists
        :param a1: first coordinate of the first object
        :param b1: second coordinate of the first object
        :param a2: first coordinate of the second object
        :param b2: second coordinate of the second object
        :return: boolean value
        """
        if a1 >= a2 and a1 < a2 + 20:
            if b1 >= b2 and b1 < b2 + 20:
                return True
        return False

    def sound(self, sound):
        """
        the method that turns on the sounds
        :param sound: sound in game
        """
        sound_v = pygame.mixer.Sound(f"{sound}.mp3")
        pygame.mixer.Sound.play(sound_v)

    def music(self):
        """
        the method that turns on the music
        """
        pygame.mixer.music.load("MUSIC/beach.mp3")
        pygame.mixer.music.play(-1)

    def background(self):
        """
        the method that turns on the background of the game
        """
        bgr = pygame.image.load("images/backgr.png")
        self.surface.blit(bgr, (0, 0))

    def play(self):
        """
        the method that checks game conditions
        """
        self.background()
        self.snake.creep()
        self.chocolate.draw()
        self.bomb.draw()
        self.score()
        pygame.display.flip()

        """change site"""
        if self.snake.x[0] == -20 and self.snake.direction == "left":
            self.snake.out_of_x_left()
        if self.snake.x[0] == 500 and self.snake.direction == "right":
            self.snake.out_of_x_right()
        if self.snake.y[0] == -20 and self.snake.direction == "up":
            self.snake.out_of_y_up()
        if self.snake.y[0] == 400 and self.snake.direction == "down":
            self.snake.out_of_y_down()
        pygame.display.flip()

        """points collecting"""
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

        """game is over"""
        for i in range(1, self.snake.size):
            if self.collision_finder(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.sound("MUSIC/death")
                self.save_scores()
                raise

        if self.collision_finder(self.snake.x[0], self.snake.y[0], 120, 100):
            self.sound("MUSIC/death")
            self.save_scores()
            raise

        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 360, 100):
            self.sound("MUSIC/death")
            self.save_scores()
            raise

        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 240, 180):
            self.sound("MUSIC/death")
            self.save_scores()
            raise

        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 120, 260):
            self.sound("MUSIC/death")
            self.save_scores()
            raise

        elif self.collision_finder(self.snake.x[0], self.snake.y[0], 360, 260):
            self.sound("MUSIC/death")
            self.save_scores()
            raise

    def score(self):
        """
        te method that counts and displays your game points
        """
        font = pygame.font.SysFont('Helvetica', 22)
        result = font.render(f"Score: {self.snake.size-1}", True, (75, 0, 130))
        self.surface.blit(result, (400, 5))

    def save_scores(self):
        """
        the method that saves scores of the game
        """
        mode = None
        if self.mode == 0.12:
            mode = "Easy"
        elif self.mode == 0.1:
            mode = "Medium"
        elif self.mode == 0.08:
            mode = "Hard"
        f = open("top_scores.txt", "a")
        f.write(str(self.snake.size - 1) + " " + mode + "\n")
        f.close()

    def the_end(self):
        """
        the method that displays a message after the game
        """
        self.background()
        font = pygame.font.SysFont('Helvetica', 35)
        message = font.render(f"You've lost, your final score is: {self.snake.size-1}", True, (0, 0, 0))
        self.surface.blit(message, (20, 100))
        message2 = font.render(f"Click 'ENTER' to play again", True, (255, 255, 0))
        self.surface.blit(message2, (50, 180))
        message3 = font.render(f"Click 'SPACE' to go to menu", True, (255, 255, 0))
        self.surface.blit(message3, (50, 250))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def restart(self):
        """
        the method that restarts the game
        """
        self.snake = Snake(self.surface, 1)
        self.chocolate = Chocolate(self.surface)

    def go(self):
        """
        the method that enables us to use computer buttons
        """
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
                    elif event.key == K_SPACE:
                        main_menu()
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
            time.sleep(self.mode)


def main(t):
    """
    the method that turns on the game
    :param t: velocity of the snake
    """
    game = Game(t)
    game.go()


def main_menu():
    """
    the function that creates the main menu
    """
    pygame.init()

    def leaderboard():
        """
        the method that takes 5 best scores
        :return: 5 best scores
        """
        f = open("top_scores.txt", "r")
        lines = f.readlines()
        f.close()
        top = []
        for line in lines:
            try:
                a, b = line.split()
                pair = (int(a), b)
                top.append(pair)
            except Exception:
                pass
        top_5 = sorted(top, key=lambda x: x[0], reverse=True)
        return top_5[:5]

    def top_s():
        """
        the method that creates the leaderboard screen
        """
        gui_5 = pygame.display.set_mode((500, 400))

        back_2_button = Button(
            gui_5, 30, 320, 100, 50, text='Back', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=main_menu)

        run = True
        while run:
            events = pygame.event.get()

            gui_5.fill((102, 204, 255))
            back_2_button.listen(events)
            quit_button.listen(events)

            red = (255, 0, 0)
            x = 500
            y = 400

            pygame.display.set_caption('Top scores')

            font = pygame.font.Font('arial.ttf', 25)

            element = 0

            roman = ["I", "II", "III", "IV", "V"]

            for s, i in zip(leaderboard(), roman):

                text = font.render(f"{i}: " + str(s[0]) + " " + str(s[1]), False, red)

                textRect = text.get_rect()

                textRect.center = (x // 2, y // 14 + element)

                element += 60

                gui_5.blit(text, textRect)

            back_2_button.draw()

            quit_button.draw()

            pygame.display.update()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

    def instructions():
        """
        the method that creates the instructions screen
        """
        gui_3 = pygame.display.set_mode((500, 400))

        back_2_button = Button(
            gui_3, 30, 320, 100, 50, text='Back', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=main_menu)

        run = True
        while run:
            events = pygame.event.get()

            gui_3.fill((102, 204, 255))
            back_2_button.listen(events)
            quit_button.listen(events)

            red = (255, 0, 0)
            x = 500
            y = 400

            pygame.display.set_caption('Instructions')

            font = pygame.font.Font('arial.ttf', 25)

            text0 = font.render("Don't hit the bombs and yourself,", False, red)
            text02 = font.render("eat as much Chocolate as you can!", False, red)
            text1 = font.render("Use 'w' or 'up arrow' to go up", False, red)
            text2 = font.render("Use 's' or 'down arrow' to go down", False, red)
            text3 = font.render("Use 'a' or 'left arrow' to go left", False, red)
            text4 = font.render("Use 'd' or 'right arrow' to go right", False, red)
            text5 = font.render("Use 'Enter' to pause the game", False, red)

            textRect0 = text0.get_rect()
            textRect02 = text02.get_rect()
            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()

            textRect0.center = (x // 2, y // 14)
            textRect02.center = (x // 2, y // 7)
            textRect1.center = (x // 2, y // 3.5)
            textRect2.center = (x // 2, y // 2.5)
            textRect3.center = (x // 2, y // 1.95)
            textRect4.center = (x // 2, y // 1.6)
            textRect5.center = (x // 2, y // 1.37)

            gui_3.blit(text0, textRect0)
            gui_3.blit(text02, textRect02)
            gui_3.blit(text1, textRect1)
            gui_3.blit(text2, textRect2)
            gui_3.blit(text3, textRect3)
            gui_3.blit(text4, textRect4)
            gui_3.blit(text5, textRect5)

            back_2_button.draw()

            quit_button.draw()

            pygame.display.update()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

    def author():
        """
        the method that creates the author screen
        """
        gui_4 = pygame.display.set_mode((500, 400))

        back_2_button = Button(
            gui_4, 30, 320, 100, 50, text='Back', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=main_menu)

        run = True
        while run:
            events = pygame.event.get()

            gui_4.fill((102, 204, 255))
            back_2_button.listen(events)
            quit_button.listen(events)

            red = (255, 0, 0)
            x = 500
            y = 400

            pygame.display.set_caption('Author')

            font = pygame.font.Font('arial.ttf', 30)

            text1 = font.render("Adam Kawałko", False, red)
            text2 = font.render("Applied Mathematics", False, red)
            text3 = font.render("I year", False, red)
            text4 = font.render("I like People", False, red)
            text5 = font.render("I like computer games", False, red)

            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()

            textRect1.center = (x // 2, y // 8.5)
            textRect2.center = (x // 2, y // 4)
            textRect3.center = (x // 2, y // 2.5)
            textRect4.center = (x // 2, y // 1.8)
            textRect5.center = (x // 2, y // 1.4)

            gui_4.blit(text1, textRect1)
            gui_4.blit(text2, textRect2)
            gui_4.blit(text3, textRect3)
            gui_4.blit(text4, textRect4)
            gui_4.blit(text5, textRect5)

            back_2_button.draw()

            quit_button.draw()

            pygame.display.update()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

    def new_menu():
        """
        the method that creates the level choice screen
        """
        pygame.init()
        gui_2 = pygame.display.set_mode((500, 400))

        easy_button = Button(
            gui_2, 200, 70, 100, 50, text='Easy', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=lambda: main(0.12))

        medium_button = Button(
            gui_2, 175, 160, 150, 50, text='Medium', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=lambda: main(0.1))

        hard_button = Button(
            gui_2, 200, 250, 100, 50, text='Hard', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=lambda: main(0.08))

        back_button = Button(
            gui_2, 30, 320, 100, 50, text='Back', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=main_menu)

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

            gui_2.fill((102, 204, 255))
            easy_button.listen(events)
            easy_button.draw()
            medium_button.listen(events)
            medium_button.draw()
            hard_button.listen(events)
            hard_button.draw()
            back_button.listen(events)
            back_button.draw()
            quit_button.listen(events)
            quit_button.draw()
            pygame.display.set_caption('Play')
            pygame.display.update()
    """
    Main menu
    """
    gui = pygame.display.set_mode((500, 400))

    play_button = Button(
        gui, 185, 80, 140, 80, text='Play', textColour=(153, 0, 51), radius=40,
        fontSize=80,
        inactiveColour=(255, 223, 128),
        pressedColour=(51, 204, 51),
        onClick=new_menu)

    quit_button = Button(
        gui, 370, 320, 100, 50, text='Quit', textColour=(153, 0, 51), radius=40,
        fontSize=50,
        inactiveColour=(255, 223, 128),
        pressedColour=(51, 204, 51),
        onClick=quit)

    instructions_button = Button(
        gui, 135, 250, 230, 50, text='Instructions', textColour=(153, 0, 51), radius=40,
        fontSize=50,
        inactiveColour=(255, 223, 128),
        pressedColour=(51, 204, 51),
        onClick=instructions)

    top_scores_button = Button(
        gui, 150, 180, 200, 50, text='Top scores', textColour=(153, 0, 51), radius=40,
        fontSize=50,
        inactiveColour=(255, 223, 128),
        pressedColour=(51, 204, 51),
        onClick=top_s)

    author_button = Button(
        gui, 190, 320, 140, 50, text='Author', textColour=(153, 0, 51), radius=40,
        fontSize=50,
        inactiveColour=(255, 223, 128),
        pressedColour=(51, 204, 51),
        onClick=author)

    run = True
    while run:
        events = pygame.event.get()

        gui.fill((102, 204, 255))
        play_button.listen(events)
        quit_button.listen(events)
        instructions_button.listen(events)
        author_button.listen(events)
        top_scores_button.listen(events)

        brown = (128, 32, 0)
        x = 500
        y = 400

        pygame.display.set_caption('Snake & chocolate')

        font = pygame.font.Font('arial.ttf', 40)

        text = font.render("SNAKE & CHOCOLATE", False, brown)

        textRect = text.get_rect()

        textRect.center = (x // 2, y // 12)

        gui.blit(text, textRect)

        play_button.draw()
        quit_button.draw()
        instructions_button.draw()
        author_button.draw()
        top_scores_button.draw()

        pygame.display.update()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()


main_menu()
