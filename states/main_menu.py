# Purpose: Main_Menu child class that inherits from State class, provides pathway to switch into other classes 

# Import required modules and classes
from states.state import State
from button import Button
from assets.assets import *

from states.shop_menu import Shop_Menu
from states.gameplay import Restaurant

# Defines behaviour and attributes from the State class while in the main menu
class Main_Menu(State):

    # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)

    # Updates events based on action triggers
    def update(self, actions):
        super().update(actions)
        # Enters Shop state when shop action is triggered
        if actions["shop"]:
            new_state = Shop_Menu(self.game)
            new_state.enter_state()
        # Enters Restaurant state when start action is triggered
        if actions["start"]:
            new_state = Restaurant(self.game)
            new_state.enter_state()

    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
        # Draw background and title screen logo
        self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_image(game_logo, 1, surface, self.game.GAME_X / 2, 38)
        
        # Initialize buttons with position, image, and scale
        self.start_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 5 , play_button, 1)
        self.shop_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 32, shop_button, 1)
        self.quit_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 59, quit_button, 1)

        # Draw buttons and trigger actions when buttons are pressed
        if self.start_button.draw(surface):
            self.game.actions["start"] = True
        if self.shop_button.draw(surface):
            self.game.actions["shop"] = True
        if self.quit_button.draw(surface):
            self.game.actions["quit"] = True
