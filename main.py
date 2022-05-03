# Import required libraries
import pygame
import math

from module import draw_image, draw_text, gradient_rect
from button import Button

# Initialize pygame library
pygame.init()

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Colour palette
BLUE = (133, 203, 205)
LIGHT_BLUE = (168, 222, 224)
LIGHT_ORANGE = (249, 226, 174)
ORANGE = (251, 199, 141)
GREEN = (167, 214, 118)

NEXA_FONT = pygame.font.Font("assets/fonts/Nexa-Trial-Regular.ttf", 15)
YOSTER_FONT = pygame.font.Font("assets/fonts/yoster.ttf", 50)

# Load images
placeholder_title = pygame.image.load("assets/images/titles/cookingPapaPlaceholderTitle.png")
placeholder_button = pygame.image.load("assets/images/icons/buttonPlaceholder.png")
return_arrow = pygame.image.load("assets/images/icons/return_arrow.png")
gold_icon = pygame.image.load("assets/images/icons/coin.png")

# Sets up display window (w x h)
size_x = 1280
size_y = 720
screen = pygame.display.set_mode((size_x, size_y))

# Sets the name of the window
pygame.display.set_caption("Cooking Papa")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Universal return button
return_button = Button(50, 50, return_arrow, 5)

# Main menu screen
def main_menu():

    # Make variables global so that they can be modified from within this function
    global in_menu, running, is_shopping, is_playing

    # Initialize main menu buttons 
    start_button = Button((size_x / 2), (size_y / 2), placeholder_button, 0.9)
    shop_button = Button((size_x / 2), (size_y / 2) + 100, placeholder_button, 0.9)
    quit_button = Button((size_x / 2), (size_y / 2) + 200, placeholder_button, 0.9)

    # Fill screen
    screen.fill(ORANGE)
    pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(size_x - size_x / 2, 0, size_x / 2, size_y))
    
    # Draw Game title image
    draw_image(placeholder_title, 5, screen, size_x/2, 200)
    
    # Actions when start button pressed
    if start_button.draw(screen):
        in_menu = False
        is_playing = True
    
    # Actions when shop button pressed
    if shop_button.draw(screen):
        in_menu = False
        is_shopping = True
    
    # Actions when quit button pressed
    if quit_button.draw(screen):
        global running
        running = False

    pygame.display.update()

# Playing screen
def play():

    # Make variables global so that they can be modified from within this function
    global in_menu, running, is_shopping, is_playing
    
    # Fills screen with colour to give illusion of new screen
    screen.fill(BLUE)
    draw_text("Game started", YOSTER_FONT, WHITE, screen, size_x/2, size_y/3)

    # Play game states

    if at_counter:
        counter()
    
    elif in_kitchen:
        kitchen

    # Returns player to main menu when button is pressed
    if return_button.draw(screen):
        in_menu = True
        is_playing = False

    draw_image(gold_icon, 5, screen, size_x - 150, size_y - 50)

    pygame.display.update()

# Shop screen
def shop_menu():

    # Make variables global so that they can be modified from within this function
    global in_menu, running, is_shopping, is_playing
    
    # Fills screen with colour to give illusion of new screen
    screen.fill(GREEN)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(size_x - size_x / 2, 0, size_x / 2, size_y))
    draw_text("Shop entered", NEXA_FONT, BLACK, screen, size_x/2, size_y/2)

    # Returns player to main menu when button is pressed
    if return_button.draw(screen):
        
        in_menu = True
        is_shopping = False

    pygame.display.update()  

# Variable to determine whether main game loop is running
running = True

# Variables to determine which state the game is in
in_menu = True
is_playing = False
is_shopping = False

# Functions for each play state
def counter():
    counter = pygame.draw.rect(screen, LIGHT_ORANGE, pygame.Rect(0, size_y / 2, size_x, size_y / 2))

def kitchen():
    pygame.draw.rect(screen, ORANGE, pygame.Rect(0,size_y / 2, size_x, size_y / 2))

# Variables to determine which play state the game is in

at_counter = True
in_kitchen = False

# Game loop
while running:

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_playing, is_shopping = False, False
                in_menu = True

        # elif event.type == pygame.KEYUP:
        #     print("button released")

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print("clicked")

        # elif event.type == pygame.MOUSEBUTTONUP:
        #     print("click released")

        

    if in_menu:
        main_menu()

    if is_playing:
        play()

    if is_shopping:
        shop_menu()
    
    # Updates display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()