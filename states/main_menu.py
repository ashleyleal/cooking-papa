from states.state import State
from button import Button
from assets.assets import *

from states.shop_menu import Shop_Menu
from states.gameplay import Gameplay


class Main_Menu(State):

    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        if actions["shop"]:
            new_state = Shop_Menu(self.game)
            new_state.enter_state()

        if actions["start"]:
            new_state = Gameplay(self.game)
            new_state.enter_state()

        self.game.reset_keys()

    def render(self, surface):
        surface.fill(ORANGE)
        pygame.draw.rect(surface, LIGHT_BLUE, pygame.Rect(self.game.GAME_X - self.game.GAME_X / 2, 0, self.game.GAME_X / 2, self.game.GAME_Y))
        self.game.draw_image(placeholder_title, 1, surface, self.game.GAME_X / 2, 50)
        
        self.start_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2), placeholder_button, 0.25)
        self.shop_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 25, placeholder_button, 0.25)
        self.quit_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 50, placeholder_button, 0.25)

        if self.start_button.draw(surface):
            self.game.actions["start"] = True

        if self.shop_button.draw(surface):
            self.game.actions["shop"] = True

        if self.quit_button.draw(surface):
            self.game.actions["quit"] = True
