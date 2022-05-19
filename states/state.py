# Purpose: creates new State class that determines behavior for each state

from assets.assets import *

class State:

    def __init__(self, game):
        self.game = game
        self.previous_state = None

    def update(self, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.previous_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state.state_stack.pop()
        self.game.actions["fade"] = True