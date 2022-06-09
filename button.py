# Purpose: Button class that handles behaviour for all clickable UI
import pygame

# Button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # debounce
        self.clicked = False

    def draw(self, surface):
        action = False
        # mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Creates a new rectangle that is compatible with the upscaled game_canvas
        new_rect = pygame.Rect(self.rect.x * 4, self.rect.y * 4, self.rect.w * 4, self.rect.h * 4)

        # Check mouseover and clicked conditions
        if new_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    pygame.time.delay(250)
                    self.clicked = True
                    action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def hover(self):
        # Increase scale of button when mouse pos is the same as button rect position

        # Set instance variable for scale
        # Set instance varibale for button rect
        # Get mouse pos
        # If mouse pos is equal to button rect coordinates: 
            # Multiply scale by a factor of 3
        pass

