import pygame, sys
from button import Button
from questions import CATEGORIES, Question 

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jeopardy! by Group F")

BG = pygame.image.load("assets/Background.png")
PLAY_BG = pygame.image.load("assets/Player BG.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Fredoka.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#6d0707", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 500), 
                            text_input="QUIT", font=get_font(75), base_color="#6d0707", hovering_color="White")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    
    while True:
        SCREEN.blit(PLAY_BG, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_PLAYER1 = Button(image=pygame.image.load("assets/Player Button.png"), pos=(320, 530), 
                            text_input="1 PLAYER", font=get_font(30), base_color="White", hovering_color="Green")
        PLAY_PLAYER1.change_color(PLAY_MOUSE_POS)
        PLAY_PLAYER1.update(SCREEN)

        PLAY__PLAYER2 = Button(image=pygame.image.load("assets/Player Button.png"), pos=(640, 530), 
                            text_input="2 PLAYERS", font=get_font(30), base_color="White", hovering_color="Green")
        PLAY__PLAYER2.change_color(PLAY_MOUSE_POS)
        PLAY__PLAYER2.update(SCREEN)

        PLAY_PLAYER3 = Button(image=pygame.image.load("assets/Player Button.png"), pos=(960, 530), 
                            text_input="3 PLAYERS", font=get_font(30), base_color="White", hovering_color="Green")
        PLAY_PLAYER3.change_color(PLAY_MOUSE_POS)
        PLAY_PLAYER3.update(SCREEN)
    
        PLAY_BACK_BUTTON = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        PLAY_BACK_BUTTON.change_color(PLAY_MOUSE_POS)
        PLAY_BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK_BUTTON.check_for_input(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_PLAYER1.check_for_input(PLAY_MOUSE_POS):
                    names = name_input(1)
                    print(names)

                if PLAY__PLAYER2.check_for_input(PLAY_MOUSE_POS):
                    names = name_input(2)
                    print(names)

                if PLAY_PLAYER3.check_for_input(PLAY_MOUSE_POS):
                    names = name_input(3)
                    print(names)

        pygame.display.update()

def name_input(num_players):
    names = ["" for _ in range(num_players)]
    active_index = 0
    input_font = get_font(50)

    while True:
        SCREEN.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        title = get_font(50).render(f"Enter names for {num_players} player(s)", True, "White")
        title_rect = title.get_rect(center=(640, 100))
        SCREEN.blit(title, title_rect)

        # Draw name boxes
        for i in range(num_players):
            color = "green" if i == active_index else "white"
            text_surface = input_font.render(names[i] or f"Player {i+1}", True, color)
            rect = text_surface.get_rect(center=(640, 200 + i*100))
            pygame.draw.rect(SCREEN, (50, 50, 50), rect.inflate(300, 20))  # background box
            SCREEN.blit(text_surface, rect)

        # "Done" button appears when all names are typed
        done_btn = Button(image=None, pos=(640, 600),
                          text_input="DONE", font=get_font(45),
                          base_color="White", hovering_color="Green")
        done_btn.change_color(mouse_pos)
        done_btn.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:   # move to next player
                    if active_index < num_players - 1:
                        active_index += 1
                    else:
                        return names  # finished typing
                elif event.key == pygame.K_BACKSPACE:
                    names[active_index] = names[active_index][:-1]
                else:
                    names[active_index] += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if done_btn.check_for_input(mouse_pos) and all(names):
                    return names
    
        pygame.display.update()

def game_grid(names):
    categories = list(CATEGORIES.keys())
    point_values = sorted(list(set(p for cat in CATEGORIES for p in CATEGORIES[cat])))
    question_buttons = []
    button_width = 200
    button_height = 80
    x_spacing = (1280 - len(categories) * button_width) / (len(categories) + 1)
    y_spacing = (720 - (len(point_values) + 1) * button_height) / (len(point_values) + 1)
    for i, category in enumerate(categories):
        for j, points in enumerate(point_values):
            if points in CATEGORIES[category]:
                x = x_spacing + i * (button_width + x_spacing)
                y = 100 + y_spacing + j * (button_height + y_spacing)
                question_obj = CATEGORIES[category][points]
                if question_obj.answered:
                    base_color = "grey"
                    hovering_color = "grey"
                    text_input = ""
                else:
                    base_color = "#6d0707"
                    hovering_color = "White"
                    text_input = str(points)
                button = Button(
                    image=pygame.image.load("assets/Play Rect.png"),
                    pos=(x, y),
                    text_input=text_input,
                    font=get_font(40),
                    base_color=base_color,
                    hovering_color=hovering_color
                )
                question_buttons.append({"button": button, "question_obj": question_obj})
    while True:
        SCREEN.blit(PLAY_BG, (0, 0))
        GAME_GRID_MOUSE_POS = pygame.mouse.get_pos()
        for i, category in enumerate(categories):
            text = get_font(25).render(category, True, "White")
            text_rect = text.get_rect(center=(x_spacing + i * (button_width + x_spacing), 70))
            SCREEN.blit(text, text_rect)
        for item in question_buttons:
            if not item["question_obj"].answered:
                item["button"].change_color(GAME_GRID_MOUSE_POS)
            item["button"].update(SCREEN)
        BACK_BUTTON = Button(image=None, pos=(640, 650), text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")
        BACK_BUTTON.change_color(GAME_GRID_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.check_for_input(GAME_GRID_MOUSE_POS):
                    play()
                for item in question_buttons:
                    if not item["question_obj"].answered and item["button"].check_for_input(GAME_GRID_MOUSE_POS):
                        show_question(item["question_obj"])
                        return game_grid(names)
        pygame.display.update()

def show_question(question_obj):
    question = question_obj.question
    answer = question_obj.answer
    user_input = ""
    input_active = True
    input_box = pygame.Rect(490, 450, 300, 50)
    input_font = get_font(30)
    while True:
        SCREEN.fill((0, 0, 0))
        question_surface = get_font(30).render(question, True, "White")
        question_rect = question_surface.get_rect(center=(640, 300))
        SCREEN.blit(question_surface, question_rect)
        pygame.draw.rect(SCREEN, "white" if input_active else "grey", input_box, 2)
        text_surface = input_font.render(user_input, True, "White")
        SCREEN.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        submit_button = Button(image=None, pos=(640, 550), text_input="SUBMIT", font=get_font(40), base_color="White", hovering_color="Green")
        submit_button.change_color(pygame.mouse.get_pos())
        submit_button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                if submit_button.check_for_input(pygame.mouse.get_pos()):
                    if question_obj.check_answer(user_input):
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct answer was: {answer}")
                    return
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    if question_obj.check_answer(user_input):
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct answer was: {answer}")
                    return
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
        pygame.display.update()

main_menu()

