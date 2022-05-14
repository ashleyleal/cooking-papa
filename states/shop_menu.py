from states.state import State
from button import Button
from assets.fontcolors import *

class Shop_Menu(State):

    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

    def render(self, surface):
        surface.fill(GREEN)
        pygame.draw.rect(surface, ORANGE, pygame.Rect(self.game.GAME_X - self.game.GAME_X / 2, 0, self.game.GAME_X / 2, self.game.GAME_Y))
        self.game.draw_text(surface, "Shop entered", YOSTER_FONT, WHITE, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        
        if return_button.draw(surface):
            self.game.actions["menu"] = True