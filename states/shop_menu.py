'''
-------------------------------------------------------------------------------
Name:  shop_menu.py
Course: ICS4U1
Purpose: Contains Shop Menu, Characters, Colours, and Music classes (states) that define behaviour in each section of the shop
 
Author:   Ashley L & Fionna C
Created:  01/05/2022
------------------------------------------------------------------------------
'''

# Import required modules
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
        # Enters Main Menu state when action is triggered
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

            # Enters Character state when action is triggered
        if actions["characters"]:
          new_state = Characters(self.game)
          new_state.enter_state()

          # Enters Colours state when action is triggered
        if actions["colours"]:
          new_state = Colours(self.game)
          new_state.enter_state()

          # Enters Music state when action is triggered
        if actions["music"]:
          new_state = Music(self.game)
          new_state.enter_state()


    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
        self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
        self.game.draw_image(shop_title, 1, surface, self.game.GAME_X / 2, 38)
        self.game.draw_image(characters_button, 1, surface, 80, 120)
        self.game.draw_image(recolour_button, 1, surface, self.game.GAME_X / 2, 120)
        self.game.draw_image(music_button, 1, surface, 242, 120)
  
        # Initialize buttons
        self.characters_button = Button(80, 120, characters_button, 1)
        self.recolour_button = Button((self.game.GAME_X / 2), 120, recolour_button, 1)
        self.music_button = Button(242, 120, music_button, 1)
       
        # Draw buttons and trigger actions when buttons are pressed
        if return_button.draw(surface):
          self.game.actions ["menu"] = True
          pygame.mixer.music.unload()
          pygame.mixer.music.load(self.game.current_song)
          pygame.mixer.music.play(-1)

        if self.characters_button.draw(surface):
            self.game.actions["characters"] = True

        if self.recolour_button.draw(surface):
          self.game.actions["colours"] = True

        if self.music_button.draw(surface):
          self.game.actions["music"] = True

class Characters(State):
    # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)

        self.buy = False
        self.ok = False
    # Updates events based on action triggers
    def update(self, actions):
        super().update(actions)
        
        # Enters Shop state when action is triggered
        if actions["shop"]:
          new_state = Shop_Menu(self.game)
          new_state.enter_state()
        
        # Enters Character state when action is triggered
        if actions["characters"]:
          new_state = Characters(self.game)
          new_state.enter_state()

    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
      self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
      self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
      self.game.draw_image(character_title, 1, surface, self.game.GAME_X / 2, 32)
      self.game.draw_image(speedwagon_buy, 1, surface,self.game.GAME_X / 2 - 60, 120)
      self.game.draw_image(speedwagon_buy_button, 1, surface, self.game.GAME_X / 2 + 60, self.game.GAME_Y / 2 + 30 )

      # Initialize button
      self.speedwagon_buy_button = Button(self.game.GAME_X / 2 + 60, self.game.GAME_Y / 2 + 30, speedwagon_buy_button, 1 )

      # Draw buttons and trigger actions when buttons are pressed
      if return_button.draw(surface):
        self.game.actions["shop"] = True

      if self.speedwagon_buy_button.draw(surface):
        self.buy = True

      if self.buy == True:
        self.game.draw_image(confirm_purchase_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_image(red_cross, 1, surface, 130, 110)
        self.game.draw_image(check_mark, 1, surface, 190, 110)

        # Initialize buttons
        self.red_cross = Button(130, 110, red_cross, 1)
        self.check_mark = Button(190, 110, check_mark, 1)

        if self.red_cross.draw(surface):
          self.game.actions["characters"] = True

        if self.check_mark.draw(surface) and self.game.gold >= 45:
          self.game.spend_gold(45)
          self.ok = True
          self.game.owned_character_1 = True
          print("money spent")
        
        if self.ok == True:
          self.game.draw_image(purchased_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)
          
          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["characters"] = True
          
        if self.game.gold < 45:
          self.game.draw_image(insuficent_funds_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)

          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["characters"] = True
           
class Colours(State):
  # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)
        self.buy1 = False
        self.buy2 = False
        self.cry = False

    # Updates events based on action triggers
    def update(self, actions):
        super().update(actions)
        if actions["shop"]:
          new_state = Shop_Menu(self.game)
          new_state.enter_state()
          # Enters Shop state when action is triggered

        if actions["colours"]:
          new_state = Colours(self.game)
          new_state.enter_state()
          # Enters Colours state when action is triggered

    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
      self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
      self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
      self.game.draw_image(Wallpaper_title, 1, surface, self.game.GAME_X / 2, 38)
      self.game.draw_image(Recolour_center_button, 1, surface, self.game.GAME_X /2, 119)
      self.game.draw_image(recolour_option_1, 1, surface, 78, 120)
      self.game.draw_image(recolour_option_2, 1, surface, 242, 119)
      
      # Initialize button
      self.Recolour_option_1 = Button(78, 120, recolour_option_1, 1)
      self.Recolour_option_2 = Button(242, 119, recolour_option_2, 1)
     
      # Draw buttons and trigger actions when buttons are pressed
      if return_button.draw(surface):
        self.game.actions["shop"] = True

      if self.Recolour_option_1.draw(surface):
        self.buy1 = True
    
      if self.Recolour_option_2.draw(surface):
        self.buy2 = True
        
      if self.buy1 == True:

        self.game.draw_image(confirm_purchase_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2 )
        self.game.draw_image(red_cross, 1, surface, 130, 110)
        self.game.draw_image(check_mark, 1, surface, 190, 110)
        
        # Initialize buttons
        self.red_cross = Button(130, 110, red_cross, 1)
        self.check_mark = Button(190, 110, check_mark, 1)

        if self.red_cross.draw(surface):
          self.game.actions["colours"] = True

        if self.check_mark.draw(surface) and self.game.gold >= 25:
          self.game.spend_gold(25)
          self.cry = True
          self.game.colour_one_owned = True
          self.game.colour_two_owned = False
         
        if self.cry == True:
          self.game.draw_image(purchased_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)

          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["colours"] = True
            
        if self.game.gold < 25:
          self.game.draw_image(insuficent_funds_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)

          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["colours"] = True

      if self.buy2 == True:
        self.game.draw_image(confirm_purchase_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2 )
        self.game.draw_image(red_cross, 1, surface, 130, 110)
        self.game.draw_image(check_mark, 1, surface, 190, 110)
        
        # Initialize button
        self.red_cross = Button(130, 110, red_cross, 1)
        self.check_mark = Button(190, 110, check_mark, 1)

        if self.red_cross.draw(surface):
          self.game.actions["colours"] = True

        if self.check_mark.draw(surface):
          self.game.spend_gold(25)
          self.cry = True
          self.game.colour_two_owned = True
          self.game.colour_one_owned = False
          
        if self.cry == True:
          self.game.draw_image(purchased_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)

          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["colours"] = True
          
        if self.game.gold < 25:
          self.game.draw_image(insuficent_funds_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)

          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["colours"] = True
      
         
class Music(State):
  # Inherit init method from State class 
    def __init__(self, game):
        State.__init__(self, game)
        self.buy = False
        self.ok = False
    
    # Updates events based on action triggers
    def update(self, actions):
        super().update(actions)
        if actions["shop"]:
          new_state = Shop_Menu(self.game)
          new_state.enter_state()
          # Enter Shop state when action is triggered

        if actions["music"]:
          new_state = Music(self.game)
          new_state.enter_state()
          # Enter Music state when action is triggered
     
    # Render loop that continously updates screen based on current conditions
    def render(self, surface):
      self.game.draw_image(menu_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
      self.game.draw_gold(surface, self.game.GAME_X - 35, 15, MARBLE_WHITE)
      self.game.draw_image(music_title, 1, surface, self.game.GAME_X / 2, 35)
      self.game.draw_image(music_buy, 1, surface, self.game.GAME_X - 90, self.game.GAME_Y -58)
      self.game.draw_image(speedwagon_buy_button, 1, surface, self.game.GAME_X / 2 - 60, self.game.GAME_Y / 2 - 5 )
      self.game.draw_image(menu_music_button, 1, surface, self.game.GAME_X / 2 - 60, self.game.GAME_Y / 2 + 50)
      
      # Initialize buttons
      self.speedwagon_buy_button = Button(self.game.GAME_X / 2 - 60, self.game.GAME_Y / 2 - 5, speedwagon_buy_button, 1)
      self.menu_music_button = Button(self.game.GAME_X / 2 - 60, self.game.GAME_Y / 2 + 50, menu_music_button, 1)

      if return_button.draw(surface):
        self.game.actions["shop"] = True
      
      if self.menu_music_button.draw(surface):
        self.game.current_song = default_music

      if self.speedwagon_buy_button.draw(surface):
        self.buy = True

      if self.buy == True:
        self.game.draw_image(confirm_purchase_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_image(red_cross, 1, surface, 130, 110)
        self.game.draw_image(check_mark, 1, surface, 190, 110)
        
        # Initialize buttons
        self.red_cross = Button(130, 110, red_cross, 1)
        self.check_mark = Button(190, 110, check_mark, 1)

        if self.red_cross.draw(surface):
          self.game.actions["music"] = True

        if self.check_mark.draw(surface) and self.game.gold >= 45:
          self.game.spend_gold(45)
          self.ok = True
          self.game.music = True
          self.game.current_song = jojo_music
          print("money spent")
        
        if self.ok == True:
          self.game.draw_image(purchased_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)
          
          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["music"] = True
          
        if self.game.gold < 45:
          self.game.draw_image(insuficent_funds_bg, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
          self.game.draw_image(ok_button, 1, surface, self.game.GAME_X / 2, 115)

          # Initialize button
          self.ok_button = Button(self.game.GAME_X / 2, 115, ok_button, 1)

          if self.ok_button.draw(surface):
            self.game.actions["music"] = True
  
  
