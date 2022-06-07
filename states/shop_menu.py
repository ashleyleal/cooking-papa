# Purpose: Shop_Menu child class that inherits from State class 

from states.state import State
from button import Button
from assets.assets import *

class Shop_Menu(State):

    # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)

    # Updates events based on action triggers
    def update(self, actions):
        super().update(actions)
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
        self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        #self.game.draw_image(shop_title, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        #self.game.draw_image(shop_button_1, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        #self.game.draw_image(shop_button_2, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        #self.game.draw_image(shop_button_3, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        #(Draw buttons for avaliable music)
        #(Draw buttons for avaliable characters)
        #(Draw buttons for avaliable colours)
        #(Draw buttons for confirm or decline purchase)
        #(Draw bg for confirm or decline purchase prompt)
  
        self.shop_button_1 = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 10, shop_button_1, 1)
        self.shop_button_2 = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 37, shop_button_2, 1)
        self.shop_button_3 = Button((self.game.GAME_X / 2), (self.game.GAME_Y / 2) + 64, shop_button_3, 1)
        #(Assign buttons for avaliable music, avaliable characters, avaliable colours, confirm and decline purchases)
      
  
        if return_button.draw(surface):
            self.game.actions["menu"] = True
          
        if shop_button_1.draw(surface):
            self.game.actions["characters"] = True
          
        if shop_button_2.draw(surface):
            self.game.actions["colours"] = True
          
        if shop_button_3.draw(surface):
            self.game.actions["music"] = True

        if game.actions["characters"] == True:
          pass
          #draw all images for characters menu
          #draw all buttons for characters menu
      
        elif game.action["colours"] == True:
          pass
         #draw all images for colours menu
         #draw all buttons for colours menu

        elif game.actions["music"] == True:
          pass
        #draw all images for music menu
        #draw all buttons for music menu 
          
          
        """
        if actions menu then
          return to menu

elif action actions charater
      draw everything in the character menu

      elif 
        """
