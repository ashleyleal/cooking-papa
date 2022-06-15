# Purpose: Shop_Menu child class that inherits from State class 

from states.state import State
from button import Button
from load_assets import *

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
        if actions["characters"]:
          new_state = characters(self.game)
          new_state.enter_state()
        if actions["colours"]:
          new_state = colours(self.game)
          new_state.enter_state()
        if actions["music"]:
          new_state = music(self.game)
          new_state.enter_state()


    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
        self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
        self.game.draw_image(shop_title, 1, surface, self.game.GAME_X / 2, 38)
        self.game.draw_image(characters_button, 1, surface, 80, 120)
        self.game.draw_image(recolour_button, 1, surface, self.game.GAME_X / 2, 120)
        self.game.draw_image(music_button, 1, surface, 242, 120)
        
        #(Draw buttons for avaliable music)
        #(Draw buttons for avaliable characters)
        #(Draw buttons for avaliable colours)
        #(Draw buttons for confirm or decline purchase)
        #(Draw bg for confirm or decline purchase prompt)
  
        self.characters_button = Button(80, 120, characters_button, 1)
        self.recolour_button = Button((self.game.GAME_X / 2), 120, recolour_button, 1)
        self.music_button = Button(242, 120, music_button, 1)
        
        #(Assign buttons for avaliable music, avaliable characters, avaliable colours, confirm and decline purchases)
      
        if return_button.draw(surface):
          self.game.actions ["menu"] = True
        if self.characters_button.draw(surface):
            self.game.actions["characters"] = True
        if self.recolour_button.draw(surface):
          self.game.actions["colours"] = True
        if self.music_button.draw(surface):
          self.game.actions["music"] = True

class characters(State):
      # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)

        self.prompt_confirm_purchase = False
        self.owned_character_1 = False
        self.owned_character_2 = False
        self.owned_character_3 = False

    def update(self, actions):
        super().update(actions)
        if actions["shop"]:
          new_state = Shop_Menu(self.game)
          new_state.enter_state()
     
    def render(self, surface):
      self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
      self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
      self.game.draw_image(character_title, 1, surface, self.game.GAME_X / 2, 32)
      self.game.draw_image(speedwagon_buy, 1, surface,self.game.GAME_X / 2 - 60, 120)
      self.game.draw_image(speedwagon_buy_button, 1, surface, self.game.GAME_X / 2 + 60, self.game.GAME_Y / 2 + 30 )

      self.speedwagon_buy_button = Button(self.game.GAME_X / 2 + 60, self.game.GAME_Y / 2 + 30 )

      if return_button.draw(surface):
        self.game.actions["shop"] = True
      #if character_option_1.draw(surface):
        #self.prompt_confirm_purchase = True
        
        #self.game.draw_image(confirm_purchase)
        #self.game.draw_image(confirm_purchase_button)
        #self.game.draw_image(decline_purchase_button)
        
        #self.confirm_purchase_button = Button()
        #self.decline_purchase_button = Button()

        #if confirm_purchase_button.draw(surface):
          #if self.game.spend_gold == "insuficent funds":
            #self.game.draw_image(insuficent_funds)
            #self.game.draw_image(ok_button)

            #self.ok_button = Button()

            #if ok_button.draw(surface):
              #self.game.actions["characters"] = True

          #elif self.owned_character_1 = True:
            #self.game.draw_image(character_owned)
            #self.game.draw_image(ok_button)

            #self.ok_button = Button()

            #if ok_button(surface):
              #self.game.actions["characters"] = True

          #elif:
            #self.game.spend_gold()
            #self.character_owned = True

          #if decline_purchase_button.draw(surface):
            #self.game.actions["characters"] = True



class colours(State):
  # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)
        self.buy = False
        self.cry = False
        
        
    def update(self, actions):
        super().update(actions)
        if actions["shop"]:
          new_state = Shop_Menu(self.game)
          new_state.enter_state()
        if actions["colours"]:
          new_state = colours(self.game)
          new_state.enter_state()
        


    def render(self, surface):
      self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
      self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
      self.game.draw_image(Wallpaper_title, 1, surface, self.game.GAME_X / 2, 38)
      self.game.draw_image(Recolour_center_button, 1, surface, self.game.GAME_X /2, 119)
      self.game.draw_image(Recolour_option_1, 1, surface, 80, 119)
      self.game.draw_image(Recolour_option_2, 1, surface, 242, 120)

      self.Recolour_option_1 = Button(80, 119, Recolour_option_1, 1)
      self.Recolour_option_2 = Button(242, 120, Recolour_option_2, 1)

      
      if return_button.draw(surface):
        self.game.actions["shop"] = True

      if self.Recolour_option_1.draw(surface):
        self.buy = True
      
      if self.buy == True:
        self.game.draw_image(confirm_purchase_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2 )
        self.game.draw_image(red_cross, 1, surface, 130, 110)
        self.game.draw_image(check_mark, 1, surface, 190, 110)

        self.red_cross = Button(130, 110, red_cross, 1)
        self.check_mark = Button(190, 110, check_mark, 1)

        if self.red_cross.draw(surface):
          self.game.actions["colours"] = True

        if self.check_mark.draw(surface):
          self.game.spend_gold(25)
          self.cry = True
          self.game.colour_one_owned = True
          print("money spent")
          
        if self.cry == True:
          self.game.draw_image(purchased_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)
          if self.ok_button.draw(surface):
            self.game.actions["colours"] = True
          
        if self.game.gold < 25:
          self.game.draw_image(insuficent_funds_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["colours"] = True

          





class music(State):
  # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)
    def update(self, actions):
        super().update(actions)
        if actions["shop"]:
          new_state = Shop_Menu(self.game)
          new_state.enter_state()
     
    def render(self, surface):
      self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
      self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
      self.game.draw_image(music_button, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)

      if return_button.draw(surface):
        self.game.actions["shop"] = True


 #make a dictionary of all purchasable items and their prices (dictonary for each class for the items and prices in said class)
 #when player clicks button that corresponds to purchasing the item, call the spend gold function, check return value 
 #(if spend_gold = "insufficent funds" draw the image) 
  
  
