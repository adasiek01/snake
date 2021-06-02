from pygame_widgets import Button
from function_ok import *
import pygame_menu


def main_menu():
    def instructions():
        pygame.init()
        gui_3 = pygame.display.set_mode((500, 400))
        inst = pygame.image.load("inst.png")
        gui_3.blit(inst, inst.get_rect())
        pygame.display.flip()

        back_2_button = Button(
            gui_3, 30, 320, 100, 50, text='Back', textColour=(153, 0, 51), radius=40,
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

            gui_3.fill((102, 204, 255))
            back_2_button.listen(events)
            back_2_button.draw()

    def new_menu():
        pygame.init()
        gui_2 = pygame.display.set_mode((500, 400))

        easy_button = Button(
            gui_2, 200, 70, 100, 50, text='Easy', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=function)

        medium_button = Button(
            gui_2, 175, 160, 150, 50, text='Medium', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=function)

        hard_button = Button(
            gui_2, 200, 250, 100, 50, text='Hard', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=function)

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
            pygame.display.update()

    pygame.init()
    gui = pygame.display.set_mode((500, 400))

    play_button = Button(
        gui, 200, 120, 100, 50, text='Play', textColour=(153, 0, 51), radius=40,
        fontSize=50,
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
        gui, 135, 220, 230, 50, text='Instructions', textColour=(153, 0, 51), radius=40,
        fontSize=50,
        inactiveColour=(255, 223, 128),
        pressedColour=(51, 204, 51),
        onClick=instructions)

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        gui.fill((102, 204, 255))
        play_button.listen(events)
        play_button.draw()
        quit_button.listen(events)
        quit_button.draw()
        instructions_button.listen(events)
        instructions_button.draw()
        pygame.display.update()





main_menu()





