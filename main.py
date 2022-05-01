# Import required libraries
import pygame
import math
import time

import module
import button

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

NEXA_FONT = ("assets/fonts/Nexa-Trial-Regular.ttf")

# Placeholder title text
placeholder_title = pygame.image.load("assets/images/cookingPapaPlaceholderTitle.png")

# Placeholder button image
placeholder_button = pygame.image.load("assets/images/buttonPlaceholder.png")

# Sets up display window (w x h)
size_x = 700
size_y = 500
screen = pygame.display.set_mode((size_x, size_y))

# Sets the name of the window
pygame.display.set_caption("Cooking Papa")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize main menu buttons here

start_button = button.Button((size_x / 2) - 80, (size_y / 2) - 50, placeholder_button, 0.8)
customize_button = button.Button((size_x / 2) - 80, (size_y / 2) + 50, placeholder_button, 0.8)
quit_button = button.Button((size_x / 2) - 80, (size_y / 2) + 150, placeholder_button, 0.8)

def main_menu():
    #main menu loop here
    screen.fill(ORANGE) #screen fill for testing purposes only
    screen.blit(pygame.transform.scale(placeholder_title, (450, 100)), ((size_x / 2) - 220, (size_y / 2) - 170))
    if start_button.draw(screen):
        print("Start game")
        play()
    if customize_button.draw(screen):
        shop_menu()
    if quit_button.draw(screen):
        global running
        running = False

def play():
    while True:
        screen.fill(ORANGE)
        back = button.Button(50, 50, placeholder_button, 0.5)
        module.draw_text(text, font, color, surface, x, y)
        pygame.display.update()

def shop_menu():
    print("Shop menu")    

# Variable to determine whether main game loop is running
running = True

# Variables to determine which state the game is in
playing = False
shopping = False

# Game loop
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            print("button pressed")

        elif event.type == pygame.KEYUP:
            print("button released")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked")

        elif event.type == pygame.MOUSEBUTTONUP:
            print("click released")

    main_menu()
    
    # Updates display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()