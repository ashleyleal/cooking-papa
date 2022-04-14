# Import required libraries
import pygame
import math
import time

import module

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

# Placeholder title text
placeholder_title = pygame.image.load(r"images\cookingPapaPlaceholderTitle.png")

# Sets up display window (w x h)
size_x = 500
size_y = 500
screen = pygame.display.set_mode((size_x, size_y))

# Sets the name of the window
pygame.display.set_caption("Cooking Papa")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

running = True

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

    # Fills window colour
    screen.fill(LIGHT_ORANGE)
    screen.blit(placeholder_title, (size_x/2, size_y/2))

    # Updates display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()