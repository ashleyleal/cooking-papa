# Purpose: the main file that runs the framework of the program

"""
Known issues

- Buttons don't lose functionality after screen is cleared (SOLVED)
- Don't know how to implement time delays (SOLVED)
    - time delays must be added outside of the game loops

"""

"""
To do

- Add transition screen between states (in progress)
- Learn how to implement music
- Stew cooking
- Cooking mechanics rating (requires time delay) (SOLVED)
- Shop
- Music and sound
- Saving data locally on player's game

"""

import pygame, math, time

from states.main_menu import Main_Menu
from assets.assets import *

# Define Game class
class Game: 
    
    current_recipe = None
    gold = 110 

    # Define init method
    def __init__(self):
        
        pygame.init()

        # Music causing error
        # pygame.mixer.music.load(menu_music)
        # pygame.mixer.music.play(1)

        # Configure window
        self.GAME_X, self.GAME_Y = 320, 180
        self.SCREEN_X, self.SCREEN_Y = 1280, 720
        self.game_canvas = pygame.Surface((self.GAME_X, self.GAME_Y))
        self.screen = pygame.display.set_mode((self.SCREEN_X, self.SCREEN_Y))
        pygame.display.set_caption("Cooking Papa")
        
        # Set state of game
        self.running, self.playing = True, True
        self.actions = {"click": False, "menu": False, "start": False, "shop": False, "quit": False, "recipe": False, "fade": False, "cooking": False, "music": False, "characters": False, "colours": False, "arrowup": False, "arrowdown": False, "arrowright": False, "arrowleft": False, "confirm_purchase": False}
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

            elif event.type == pygame.MOUSEBUTTONUP:
                self.actions["click"] = True

            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_UP:
                    self.actions["arrowup"] = True
                elif event.key == pygame.K_DOWN:
                    self.actions["arrowdown"] = True
                elif event.key == pygame.K_RIGHT:
                    self.actions["arrowright"] = True
                elif event.key == pygame.K_LEFT:
                    self.actions["arrowleft"] = True

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

    def customer_payment(self, amount):
        # Add amount to gold. Remove pass keyword after doing function; it is just there so the empty function doesn't error.
        try:
            if self.total_rating >= 3 and self.total_rating < 6:
                self.game.gold += 5
            elif self.total_rating >=6 and self.total_rating < 9:
                self.game.gold += 10
            elif self.total_rating == 9:
                self.game.gold += 15
        except:
            print("An error occurred in paying the player")

    def spend_gold(self, amount):
        # Subtract amount from gold but check if there is enough first and if there isn't enough return something to indicate that there isn't enough. Remove pass when done. 
        try:
            if self.gold >= amount:
                self.gold -= amount
            elif self.gold < amount:
                return "insufficient funds" 
        except:
            print("An error occurred in spending gold")
            
# Creates an instance of Game class and runs the game loop while the program is running            
if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()





    
        

