'''
-------------------------------------------------------------------------------
Name:  button.py
Course: ICS4U1
Purpose: Contains Button class that handles behaviour for all clickable UI
 
Author:   Ashley L & Fionna C
Created:  28/04/2022
------------------------------------------------------------------------------
'''

import pygame

# Button class
class Button():
    
    # Initialize button with x, y center position, image, and scale multiplier
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        # Creates a new rectangle that is compatible with the upscaled game_canvas
        new_rect = pygame.Rect(self.rect.x * 4, self.rect.y * 4, self.rect.w * 4, self.rect.h * 4)
        # Check mouseover and clicked conditions
        if new_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                pygame.time.delay(225)
                beep_sound = pygame.mixer.Sound("assets/sounds/beep.mp3")
                pygame.mixer.Sound.play(beep_sound)
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

