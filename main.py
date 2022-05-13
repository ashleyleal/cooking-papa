# Import required libraries
import pygame
import math
#your mom lol
from module import *
from button import *
from play import *

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

NEXA_FONT = pygame.font.Font("assets/fonts/Nexa-Trial-Regular.ttf", 20)

# Load images
placeholder_title = pygame.image.load("assets/images/titles/cookingPapaPlaceholderTitle.png")
placeholder_button = pygame.image.load("assets/images/icons/buttonPlaceholder.png")
return_arrow = pygame.image.load("assets/images/icons/return_arrow.png")
gold_icon = pygame.image.load("assets/images/icons/coin.png")
restaurant_counter = pygame.image.load("assets/images/images/restaurant_counter.png")
kitchen_grill = pygame.image.load("assets/images/images/kitchen_grill.png")

# Native resolution of game
game_x, game_y = 320, 180
game_canvas = pygame.Surface((game_x, game_y))

# Sets up display window (w x h)
screen_x, screen_y = 1280, 720
screen = pygame.display.set_mode((screen_x, screen_y))

# Sets the name of the window
pygame.display.set_caption("Cooking Papa")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Universal return button
return_button = Button(25, 25, return_arrow, 0.5)

# Main menu screen
def main_menu():

    # Make variables global so that they can be modified from within this function
    global in_menu, running, is_shopping, is_playing

    # Initialize main menu buttons 
    start_button = Button((game_x / 2), (game_y / 2), placeholder_button, 0.25)
    shop_button = Button((game_x / 2), (game_y / 2) + 25, placeholder_button, 0.25)
    quit_button = Button((game_x / 2), (game_y / 2) + 50, placeholder_button, 0.25)

    # Fill screen
    game_canvas.fill(ORANGE)
    pygame.draw.rect(game_canvas, LIGHT_BLUE, pygame.Rect(game_x - game_x / 2, 0, game_x / 2, game_y))
    
    # Draw Game title image
    draw_image(placeholder_title, 1, game_canvas, game_x/2, 50)
    
    # Actions when start button pressed
    if start_button.draw(game_canvas):
        in_menu = False
        is_playing = True
    
    # Actions when shop button pressed
    if shop_button.draw(game_canvas):
        in_menu = False
        is_shopping = True
    
    # Actions when quit button pressed
    if quit_button.draw(game_canvas):
        global running
        running = False


# Playing screen
def play():

    # Make variables global so that they can be modified from within this function
    global in_menu, running, is_shopping, is_playing, in_kitchen, at_counter
    
    # Fills screen with colour to give illusion of new screen
    game_canvas.fill(BLUE)
    draw_text("Game started", NEXA_FONT, WHITE, game_canvas, game_x/2, game_y/3)

    # Play game states

    if at_counter:
        counter()
    
    elif in_kitchen:
        kitchen()

    # Returns player to main menu when button is pressed
    if return_button.draw(game_canvas):
        in_menu = True
        is_playing = False
        in_kitchen = False
        at_counter = True

    draw_image(gold_icon, 2, game_canvas, game_x - 35, game_y - 35)


# Shop screen
def shop_menu():

    # Make variables global so that they can be modified from within this function
    global in_menu, running, is_shopping, is_playing
    
    # Fills screen with colour to give illusion of new screen
    game_canvas.fill(GREEN)
    pygame.draw.rect(game_canvas, ORANGE, pygame.Rect(game_x - game_x / 2, 0, game_x / 2, game_y))
    draw_text("Shop entered", NEXA_FONT, BLACK, game_canvas, game_x/2, game_y/2)

    # Returns player to main menu when button is pressed
    if return_button.draw(game_canvas):
        
        in_menu = True
        is_shopping = False


# Variable to determine whether main game loop is running
running = True

# Variables to determine which state the game is in
in_menu = True
is_playing = False
is_shopping = False

# Functions for each play state
def counter():
    global at_counter, in_kitchen
    # Draw GUI
    generate_customer(game_x/2, game_y/2, game_canvas)
    counter = draw_image(restaurant_counter, 1, game_canvas, game_x/2, 100)
    take_order = Button((game_x / 3), (game_y / 3), placeholder_button, 0.25)

    if take_order.draw(game_canvas):
        at_counter = False
        in_kitchen = True

    # Generate customer
    # Generate order
    # Button to start

def kitchen():
    pygame.draw.rect(game_canvas, ORANGE, pygame.Rect(0,game_y / 2, game_x, game_y / 2))
    grill = draw_image(kitchen_grill, 1, game_canvas, game_x/2, game_y/2)

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
    screen.blit(pygame.transform.scale(game_canvas, (screen_x, screen_y)), (0,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
