import pygame, sys
from button import Button

# The Question class and CATEGORIES data are now part of main.py
class Question:
    """
    Represents a single trivia question with its correct answer and point value.
    """
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points
        self.answered = False

    def check_answer(self, player_answer):
        self.answered = True
        return player_answer.strip().lower() == self.answer.strip().lower()

    def __str__(self):
        return f"{self.question} ({self.points} pts)"

CATEGORIES = {
    "FACULTY": {
        100: Question("Who is the current Chancellor of the UPOU?", "Joane V. Serrano, PhD.", 100),
        200: Question("Who is the Vice Chancellor for Academic Affairs?", "Aurora V. Lacaste, PhD.", 200),
        300: Question("Who is the University Registrar?", "Blancaflor P. Arada", 300),
        400: Question("Who is the current Dean for the Faculty of Information and Communication Studies?", "Assoc. Prof. Roberto B. Figueroa Jr.", 400),
        500: Question("Who is the Program Chair for Bachelor of Arts in Multimedia Studies?", "Dr. Benigno B. Agapito, Jr.", 500),
    },
    "FACILITIES": {
        100: Question("How many facilities are within the UPOU Campus in Los Banos, Laguna?", "6", 100),
        200: Question("This facility room could be used for a catered dining or a socialization gathering.", "Academic Residences Cafeteria", 200),
        300: Question("This facility can be used for large conferences and has 100-200 seating capacity.", "Centennial Center for Digital Learning (CCDL)", 300),
        400: Question("A room within the campus perfect for intimate gatherings, live streaming or podcasting as it only caters to 25-30 pax.", "Sandbox", 400),
        500: Question("A room that has the oblation and can be used for roundtable meetings.", "Oblation Hall", 500),
    },
    "UPOU HISTORY": {
        100: Question("In what year was the University of the Philippines Open University (UPOU) established?", "1995", 100),
        200: Question("UPOU is the _____ constituent university of the UP System.", "5th", 200),
        300: Question("What was the first program offered by UPOU when it was founded?", "Diploma in Distance Education", 300),
        400: Question("Where is the physical campus of UPOU located?", "Los Baños, Laguna", 400),
        500: Question("What iconic UP symbol can also be found at the UPOU campus in Los Baños?", "The Oblation", 500),
    },
    "UPOU ONLINE LEARNING TOOLS": {
        100: Question("What is the official online learning platform used by UPOU students?", "MyPortal (based on Moodle)", 100),
        200: Question("What is the official online library service of UPOU?", "UPOU Digital Library", 200),
        300: Question("Which student organization serves as the official student council of UPOU?", "UPOU Student Council (UPOU SC)", 300),
        400: Question("What is the name of the UPOU’s open access journal?", "IJDE (International Journal on Open and Distance e-Learning)", 400),
        500: Question("Which platform does UPOU use for live webcasting of academic events and lectures?", "UPOU Networks", 500),
    },
}


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



main_menu()
