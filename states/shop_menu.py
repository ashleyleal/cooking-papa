# Purpose: Shop_Menu child class that inherits from State class 

from states.state import State
from button import Button
from assets.assets import *

class Shop_Menu(State):

    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        super().update(actions)
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
        self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        
        if return_button.draw(surface):
            self.game.actions["menu"] = True
