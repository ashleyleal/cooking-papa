'''
-------------------------------------------------------------------------------
Name:  main.py
Course: ICS4U1
Purpose: Contains the Game class which contains the main loop, the event processing loop, various frequently used functions, and the attributes of game instances
 
Author:   Ashley L & Fionna C
Created:  29/04/2022
------------------------------------------------------------------------------
'''
import pygame, json

from states.main_menu import Main_Menu
from load_assets import *

# Define Game class
class Game: 
    
    # Loads the player's gold from the file
    with open(gold_save_data) as f:
        gold = json.load(f)
        print("gold data loaded")

    # Initializes variables for owned items from the shop
    current_recipe = None
    current_song = default_music
    colour_one_owned = False
    colour_two_owned = False
    owned_character_1 = False
    music = False

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

    # Defines method that pays the player gold by increasing the amount of gold
    def customer_payment(self, total_rating):
        # Add amount to gold depending on player's rating. Use try and except to prevent the program from crashing during an error.
        try:
            if total_rating >= 3 and total_rating < 6:
                self.gold += 5
            elif total_rating >=6 and total_rating < 9:
                self.gold += 10
            elif total_rating == 9:
                self.gold += 15
            self.update_save_data()
        except:
            print("An error occurred in paying the player")

    # Defines method that let's the player spend gold by decreasing the amount of gold
    def spend_gold(self, amount):
        # Subtract amount from gold but check if there is enough first and if there isn't enough return something to indicate that there isn't enough. 
        try:
            if self.gold >= amount:
                self.gold -= amount
                self.update_save_data()
                return True
            elif self.gold < amount:
                return False
        except:
            print("An error occurred in spending gold")

    # Defines method that draws the gold icon with the amount of gold owned by the player
    def draw_gold(self, surface, px, py, colour):
        self.draw_image(gold_icon, 1, surface, px - 10, py)
        self.draw_text(surface, str(self.gold), MINIMAL_FONT, colour, px + 10, py)
            
    # Defines method that updates the gold data on the file
    def update_save_data(self):
        with open(gold_save_data, "w") as f:
            json.dump(self.gold, f)
            print("gold data updated")

# Creates an instance of Game class and runs the game loop while the program is running            
if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()




    
        

