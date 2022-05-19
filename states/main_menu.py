from states.state import State
from button import Button
from assets.assets import *

from states.shop_menu import Shop_Menu
from states.gameplay import Gameplay


class Main_Menu(State):

    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        super().update(actions)
        if actions["shop"]:
            new_state = Shop_Menu(self.game)
            new_state.enter_state()

        if actions["start"]:
            new_state = Gameplay(self.game)
            new_state.enter_state()

    def render(self, surface):
        self.game.gradient_rect(surface, WARM_CROISSANT, YUCCA_CREAM, surface.get_rect())
        #pygame.draw.rect(surface, YUCCA_CREAM, pygame.Rect(self.game.GAME_X - self.game.GAME_X / 2, 0, self.game.GAME_X / 2, self.game.GAME_Y))
        self.game.draw_image(game_logo, 1, surface, self.game.GAME_X / 2, 50)
        
        self.start_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 10 , play_button, 1)
        self.shop_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 37, shop_button, 1)
        self.quit_button = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 64, quit_button, 1)

        if self.start_button.draw(surface):
            self.game.actions["start"] = True

        if self.shop_button.draw(surface):
            self.game.actions["shop"] = True

        if self.quit_button.draw(surface):
            self.game.actions["quit"] = True
