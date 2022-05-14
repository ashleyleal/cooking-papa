from states.state import State
from button import Button
from assets.assets import *

class Gameplay(State):

    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

    def render(self, surface):
        surface.fill(BLUE)
        self.game.draw_text(surface, "Game started", YOSTER_FONT, WHITE, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 100)

        if return_button.draw(surface):
            self.game.actions["menu"] = True
        