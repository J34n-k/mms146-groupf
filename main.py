import pygame, sys                              #imports the pygame and sys modules

pygame.init()                                   #initializes all the pygame modules

SCREEN = pygame.display.set_mode((1280, 720))  #sets the display window size
pygame.display.set_caption("Jeopardy!")         #sets the window title

BG = pygame.color.Color("#000000")              #sets the background color to black

def play():                                    #Play screen 

def main_menu():                               #Main menu screen
    pygame.display.set_caption("Menu")         #sets the window title

    while True:                                #main loop
        SCREEN.blit(BG, (0, 0))                #fills the screen with the background color

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #gets the current mouse position

        MENU_TEXT = pygame.font.Font(None, 100).render("Main Menu", True, (255, 255, 255))  #renders the main menu text
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = pygame.Rect(540, 200, 200, 50)  #creates a rectangle for the play button
        QUIT_BUTTON = pygame.Rect(540, 300, 200, 50)   #creates a rectangle for the quit button

        Screen.blit(MENU_TEXT, MENU_RECT)  #draws the main menu text on the screen
        
main_menu()                                    #calls the main_menu function to start the program