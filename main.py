# Purpose: the main file that runs the framework of the program

"""
Known issues

- Buttons don't lose functionality after screen is cleared
- Don't know how to implement time delays
    - time delays must be added outside of the game loops

"""

"""
To do

- Add transition screen between states (in progress)
- Learn how to implement music
- Burger cooking
- Pizza cooking
- Stew cooking
- Other food I don't remember
- Cooking mechanics rating (requires time delay)
- Shop
- Music and sound
- Saving data locally on player's game

"""

import pygame, math, time

from states.main_menu import Main_Menu
from assets.assets import *

# Define Game class
class Game: 
    
    gold = 0 

    # Define init method
    def __init__(self):
        
        pygame.init()
        
        # Configure window
        self.GAME_X, self.GAME_Y = 320, 180
        self.SCREEN_X, self.SCREEN_Y = 1280, 720
        self.game_canvas = pygame.Surface((self.GAME_X, self.GAME_Y))
        self.screen = pygame.display.set_mode((self.SCREEN_X, self.SCREEN_Y))
        pygame.display.set_caption("Cooking Papa")
        
        # Set state of game
        self.running, self.playing = True, True
        self.actions = {"menu": False, "start": False, "shop": False, "quit": False, "recipe": False, "fade": False}
        self.state_stack = []
        self.load_states()
        
        self.clock = pygame.time.Clock()

    # Define method that gets events, updates actions, and renders the screen while game is playing
    def game_loop(self):
        # Loop while playing 
        while self.playing:
            self.get_events()
            self.update()
            self.render()

    # Define method that runs event processing loop
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.actions["quit"]:
                self.running = False
                self.playing = False

    # Update state and resets actions (events)
    def update(self):
        self.state_stack[-1].update(self.actions)
        self.reset_keys()

    # Define method that changes the screen when state is changed
    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_X, self.SCREEN_Y)), (0, 0))
        pygame.display.flip()
        self.clock.tick(60)

    # Define method that draws text
    def draw_text(self, surface, text, font, color, px, py):
        text_obj = font.render(text, False, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (px, py)
        surface.blit(text_obj, text_rect)

    # Define method that draws images
    def draw_image(self, image, scale, surface, px, py):
        image_rect = image.get_rect()
        image_scaled = pygame.transform.scale(image, (image_rect.right * scale, image_rect.bottom * scale))
        image_rect.x, image_rect.y = image.get_width(), image.get_height()
        surface.blit(image_scaled, image_scaled.get_rect(center = (px, py)))

    # Define method that creates a vertical gradient of two colors
    def gradient_rect(self, surface, top_color, bottom_color, target_rect):
        color_rect = pygame.Surface((2, 2))
        pygame.draw.line(color_rect, top_color, (0, 0), (1, 0))            
        pygame.draw.line(color_rect, bottom_color, (0, 1), (1, 1))
        color_rect = pygame.transform.smoothscale(color_rect, (target_rect.width, target_rect.height))
        surface.blit(color_rect, target_rect)

    # Defines method that sets the Main menu as the first state in the stack because it is the starting point for the game
    def load_states(self):
        self.main_menu = Main_Menu(self)
        self.state_stack.append(self.main_menu)

    # Defines method that resets the status of the actions
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    # Defines method that creates a fade out white transition between scenes (work in progress)
    def fade_screen(self, surface):
        fade = pygame.Surface((self.GAME_X, self.GAME_Y))
        fade.fill((0,0,0,1))
        alpha_key = 1
        while alpha_key <= 255:
            self.surface.blit(fade, self.surface.get_rect())
            alpha_key += 1
            pygame.time.delay(1000)

    # Defines method that draws the countdown numbers (work in progress, need to move to Gameplay class)
    def draw_countdown(self, surface):
        for i in range(3):
            self.draw_text(surface, str(i), MARIO_FONT, MARBLE_WHITE, self.GAME_X/2, self.GAME_Y/2)
            pygame.time.delay(1000)

# Creates an instance of Game class and runs the game loop while the program is running            
if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()





    
        

