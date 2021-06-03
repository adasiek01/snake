from pygame_widgets import Button
from easy import *
from medium import *
from hard import *



def main_menu():
    def instructions():
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

            X = 500
            Y = 400

            pygame.display.set_caption('Instruction')

            font = pygame.font.Font('arial.ttf', 30)

            text1 = font.render("Use 'w' or 'up arrow' to go up", False, red)
            text2 = font.render("Use 's' or 'down arrow' to go down", False, red)
            text3 = font.render("Use 'a' or 'left arrow' to go left", False, red)
            text4 = font.render("Use 'd' or 'right arrow' to go right", False, red)
            text5 = font.render("Use 'Enter' to pause the game", False, red)

            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()

            textRect1.center = (X // 2, Y // 8.5)
            textRect2.center = (X // 2, Y // 4)
            textRect3.center = (X // 2, Y // 2.5)
            textRect4.center = (X // 2, Y // 1.8)
            textRect5.center = (X // 2, Y // 1.4)


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


    def new_menu():
        pygame.init()
        gui_2 = pygame.display.set_mode((500, 400))

        easy_button = Button(
            gui_2, 200, 70, 100, 50, text='Easy', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=e_function)

        medium_button = Button(
            gui_2, 175, 160, 150, 50, text='Medium', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=m_function)

        hard_button = Button(
            gui_2, 200, 250, 100, 50, text='Hard', textColour=(153, 0, 51), radius=40,
            fontSize=50,
            inactiveColour=(255, 223, 128),
            pressedColour=(51, 204, 51),
            onClick=h_function)

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





