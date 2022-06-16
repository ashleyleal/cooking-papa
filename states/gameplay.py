'''
-------------------------------------------------------------------------------
Name:  gameplay.py
Course: ICS4U1
Purpose: Contains Restaurant and Kitchen child classes that inherit from State class, controls main game mechanics such as customer and recipe generating and cooking 
 
Author:   Ashley L & Fionna C
Created:  01/05/2022
------------------------------------------------------------------------------
'''

#  Import required modules and classes
import random
from states.shop_menu import Colours
from states.state import State
from button import Button
from load_assets import * 

# Restaurant state define behaviour inside of restaurant when serving customers
class Restaurant(State):

    # Inherits from game and State class
    def __init__(self, game):
        State.__init__(self, game)
        # Nested dictionary of all possible recipes, the steps, and descriptions for each step
        self.possible_recipes =  ["Burger", "Fried Chicken", "Stew"]
        self.set_order()

    # Method that selects and returns a recipe from possible_recipes dictionary
    def generate_order(self):  
        return random.choice(self.possible_recipes)

    # Method that selects and returns a customer image
    def generate_customer(self):
        possible_customers = [customer_1, customer_2, customer_3]
        if self.game.owned_character_1 == True:
            possible_customers.append(speedwagon)
        return random.choice(possible_customers) 

    # Method that sets the returned recipes and customers and passes them to the game class variable current_recipe
    def set_order(self):
        self.selected_customer = self.generate_customer()
        self.game.current_recipe = self.generate_order()

    # Updates events based on action triggers
    def update(self, actions):
        # Enters Main Menu state when menu action is triggered
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()
        # "Rerolls" customer and recipe when recipe action is triggered 
        if actions["recipe"]:
            self.set_order()
        # Enters Kitchen state when cooking action is triggered
        if actions["cooking"]:
            new_state = Kitchen(self.game)
            new_state.enter_state()

    # Render loop that continously updates screen based on current conditions
    def render(self, surface):

        # Fills the background, draws the customer, counter, and speech bubble, and draws the selected recipe
        if self.game.colour_one_owned == True:
            self.game.draw_image(recolour_1, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)

        elif self.game.colour_two_owned == True:
            self.game.draw_image(recolour_2, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        else:
            surface.fill(WHISTLES_GOLD)
        
        self.game.draw_image(self.selected_customer, 1, surface, self.game.GAME_X / 2, 100)
        self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 115)
        self.game.draw_image(speech_bubble, 1, surface, self.game.GAME_X/ 2 + 80, self.game.GAME_Y / 2 - 50)
        self.game.draw_gold(surface, self.game.GAME_X / 2, 170, NOBLE_BLACK)
        self.show_order(surface)

        # Draw buttons and trigger actions when buttons are pressed
        if return_button.draw(surface):
            self.game.actions["menu"] = True
        if decline_order_button.draw(surface):
            self.game.actions["recipe"] = True
        if confirm_order_button.draw(surface):
            self.game.actions["cooking"] = True

    # Method that draws the selected recipe in the customer's speech bubble
    def show_order(self, surface):
        
        icon_position = self.game.GAME_X/ 2 + 80, self.game.GAME_Y / 2 - 57
        
        if self.game.current_recipe == "Burger":
            self.game.draw_image(burger_icon, 1, surface, icon_position[0], icon_position[1])
        
        elif self.game.current_recipe == "Fried Chicken":
            self.game.draw_image(chicken_icon, 1, surface, icon_position[0], icon_position[1])
        
        elif self.game.current_recipe == "Stew":
            self.game.draw_image(stew_icon, 1, surface, icon_position[0], icon_position[1])
        
        
# Kitchen state defines behaviour when the user is currently cooking
class Kitchen(State):

    # Inherit attributes from parent state class State 
    def __init__(self, game):
        State.__init__(self, game)

        # Variables that set attributes for events in the cooking processes
        self.current_recipe = self.game.current_recipe
        self.countdown_triggered = False
        self.countdown_completed = False
        self.rating_triggered = False
        self.ingredient_rating = {

            "first": 0,
            "second": 0,
            "third": 0

        }
        self.total_rating = 0
        self.next_step = False

        # Controls which number is shown on the screen to emulate countdown
        self.countdown = {
            3: False,
            2: False,
            1: False
        }

        # Variables for burger cooking
        self.burger_patty_speed = 0.15
        self.burger_patty_pos = 0
        self.stew_speed = 0.15
        self.stew_pos = 0
        self.stop_button_posx, self.stop_button_posy = self.game.GAME_X / 4, self.game.GAME_Y / 5
        self.stop_button_velx, self.stop_button_vely = 1,1
        
        self.slice_speed = 0.25
        self.slice_pos = [0]

        
        self.slice_statuses = {
            
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False

            }

        self.burger_positions = {

            1: [False, "", self.game.GAME_Y / 2 + 45],
            2: [False, "", self.game.GAME_Y / 2 + 40],
            3: [False, "", self.game.GAME_Y / 2 + 35],
            4: [False, "", self.game.GAME_Y / 2 + 30],
            "done": False,

            "cheese": False,
            "patty": False,
            "lettuce": False,
            "tomato": False

            }

        self.burger_assembly_progress = 0
        self.burger_assembled_properly = 0

        self.chicken_slice = {
            
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False

            }
        
        self.beef_slice = {
            
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False

            }
        self.beef_slice_speed = 0.25
        self.beef_slice_pos = 0

        self.chicken_coat_speed = 0.30
        self.chicken_coat_pos = 0

        self.chicken_coat_clicks = 20
        self.current_chicken = raw_chicken_1

        # Controls which step the user is currently on
        self.step_1 = True
        self.step_2 = False
        self.step_3 = False
        self.evaluation = False

        # Says whether a cooking step is completed 
        self.cooking_done = False

    # Things that happen when certain variables are modified through gameplay, is outside of render loop
    def update(self, actions):
        # If menu actions is triggered the main menu state is entered
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()
        if actions["start"]:
            new_state = Restaurant(self.game)
            new_state.enter_state()

        # If countdown_triggered find the current time and compare it to the time when the countdown is triggered to set which numbers are shown on the screen
        if self.countdown_triggered:
            pygame.mixer.Sound.play(countdown_sound)
            current_time = pygame.time.get_ticks()
            if current_time - self.button_time >= 100 and current_time - self.button_time < 1100:
                self.countdown[3] = True
            if current_time - self.button_time >= 1100 and current_time - self.button_time < 2100:
                self.countdown[2] = True
                self.countdown[3] = False
            if current_time - self.button_time >= 2100 and current_time - self.button_time < 3100:
                self.countdown[2] = False
                self.countdown[1] = True
            if current_time - self.button_time >= 3100 and current_time - self.button_time < 4100:
                self.countdown[1] = False
                pygame.mixer.Sound.stop(countdown_sound)
            if current_time - self.button_time >= 4100 and current_time - self.button_time < 5100:
              
                # Reset countdown variable and set completed to true
                pygame.mixer.Sound.stop(countdown_sound)
                self.countdown_triggered = False
                self.countdown_completed = True
                

        if self.current_recipe == "Burger" and self.step_3:
            
            def get_rating():
                self.burger_positions["done"] = True
                if self.burger_positions[1][1] == sliced_tomato:
                    self.burger_assembled_properly += 1
                if self.burger_positions[2][1] == lettuce:
                    self.burger_assembled_properly += 1
                if self.burger_positions[3][1] == cooked_patty:
                    self.burger_assembled_properly += 1
                if self.burger_positions[4][1] == cheese:
                    self.burger_assembled_properly += 1

                if self.burger_assembled_properly == 4:
                    self.ingredient_rating["third"] = 3

                elif self.burger_assembled_properly == 3 or self.burger_assembled_properly == 2:
                    self.ingredient_rating["third"] = 2

                elif self.burger_assembled_properly == 1 or self.burger_assembled_properly == 0:
                    self.ingredient_rating["third"] = 1

                self.play_victory_music()
                self.cooking_done = True
                self.completed_time = pygame.time.get_ticks()

            if not self.burger_positions["done"]:
                if self.game.actions["arrowup"]:
                    if self.burger_positions["cheese"] == False:
                        self.burger_assembly_progress += 1
                        self.burger_positions[self.burger_assembly_progress][0] = True
                        self.burger_positions[self.burger_assembly_progress][1] = cheese
                        self.burger_positions["cheese"] = True
                        if self.burger_assembly_progress == 4:
                            get_rating()    
                if self.game.actions["arrowdown"]:
                    if self.burger_positions["patty"] == False:
                        self.burger_assembly_progress += 1
                        self.burger_positions[self.burger_assembly_progress][0] = True
                        self.burger_positions[self.burger_assembly_progress][1] = cooked_patty
                        self.burger_positions["patty"] = True
                        if self.burger_assembly_progress == 4:
                            get_rating()
                if self.game.actions["arrowright"]:
                    if self.burger_positions["lettuce"] == False:
                        self.burger_assembly_progress += 1
                        self.burger_positions[self.burger_assembly_progress][0] = True
                        self.burger_positions[self.burger_assembly_progress][1] = lettuce
                        self.burger_positions["lettuce"] = True
                        if self.burger_assembly_progress == 4:
                            get_rating()
                if self.game.actions["arrowleft"]:
                    if self.burger_positions["tomato"] == False:
                        self.burger_assembly_progress += 1
                        self.burger_positions[self.burger_assembly_progress][0] = True
                        self.burger_positions[self.burger_assembly_progress][1] = sliced_tomato
                        self.burger_positions["tomato"] = True
                        if self.burger_assembly_progress == 4:
                            get_rating()
        
        # When one cooking step is completed wait some time and trigger the rating screen. Then wait some more time and switch to the next cooking step
        if self.cooking_done:
            if pygame.time.get_ticks() > self.completed_time + 3000:
                self.rating_triggered = True
                if pygame.time.get_ticks() > self.completed_time + 6000:
                    self.next_step = True

        if self.countdown_completed:
            if (self.current_recipe == "Burger" and self.step_1) or (self.current_recipe == "Fried Chicken" and self.step_3):
                    pygame.mixer.Sound.play(sizzling_sound)
                    if self.cooking_done:
                        pygame.mixer.Sound.stop(sizzling_sound)
                    
    # Render loop that continously updates screen based on current conditions 
    def render(self, surface):

        # Run the appropriate cooking process depending on the current customer order
        if self.current_recipe == "Burger":
            self.cook_burger(surface)
        elif self.current_recipe == "Fried Chicken":
            self.cook_chicken(surface)
        elif self.current_recipe == "Stew":
            self.cook_stew(surface)
        
    # Define method that cooks the burger
    def cook_burger(self, surface):

        # Define method for cooking the burger patty
        def cook_patty(surface):
            self.draw_cooking_background(surface, green_instruction_panel, kitchen_grill)

            # Changes the text in cooking papa's speech bubble depending on the conditions

            if not self.cooking_done:
                
                self.game.draw_text(surface, "FLIP AT THE", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "RIGHT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done: 
                
                if (self.burger_patty_pos >= 0 and self.burger_patty_pos <= 40) or self.burger_patty_pos > 90:
                    self.ingredient_rating["first"] = 1

                elif (self.burger_patty_pos > 40 and self.burger_patty_pos <= 50) or (self.burger_patty_pos > 80 and self.burger_patty_pos <= 90):
                    self.ingredient_rating["first"] = 2

                elif self.burger_patty_pos > 50 and self.burger_patty_pos <= 80:
                    self.ingredient_rating["first"] = 3

                self.display_rating_message(surface) 
                          

            # Draw the cooking bar that shows how cooked the patty is
            self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            # Prompt countdown
            self.trigger_countdown(surface)

            # Start cooking process when countdown is completed
            if self.countdown_completed:
                
                stop_button = Button(self.stop_button_posx, self.stop_button_posy, flip_button, 1)

                self.stop_button_posx += self.stop_button_velx
                self.stop_button_posy += self.stop_button_vely

                if self.stop_button_posx >= self.game.GAME_X / 2 - 9 or self.stop_button_posx <= 9:
                    self.stop_button_velx *= -1

                if self.stop_button_posy >= self.game.GAME_Y / 2 - 28 or self.stop_button_posy <= 5:
                    self.stop_button_vely *= -1

                if stop_button.draw(surface):
                    self.cooking_done = True
                    self.completed_time = pygame.time.get_ticks()
                    self.burger_patty_speed, self.stop_button_velx, self.stop_button_vely = 0, 0, 0

                self.game.draw_image(cooking_arrow, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4 - 65 + self.burger_patty_pos, self.game.GAME_Y / 4 + 10)
                
                self.burger_patty_pos += self.burger_patty_speed

                # Stops the cooking arrow when it reaches the end of the bar
                if self.burger_patty_pos >= 135:
                    self.burger_patty_speed, self.stop_button_velx, self.stop_button_vely = 0, 0, 0

                    if skip_button.draw(surface):
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                # Draw the appropriate patty depending on the cooking arrow position
                elif self.burger_patty_pos >= 0 and self.burger_patty_pos <= 40:
                    self.game.draw_image(raw_patty, 1, surface, self.game.GAME_X / 4, 135)

                elif self.burger_patty_pos > 40 and self.burger_patty_pos <= 90:
                    self.game.draw_image(cooked_patty, 1, surface, self.game.GAME_X / 4, 135)

                elif self.burger_patty_pos > 90:
                    self.game.draw_image(burned_patty, 1, surface, self.game.GAME_X / 4, 135)

                if self.rating_triggered:
                    self.rating_screen(surface, green_background, cook_patty_a)
                    
                if self.next_step:
                    self.reset_status(1)

        # Define method for cutting the tomato
        def cut_tomato(surface):
            self.draw_cooking_background(surface, green_instruction_panel, cutting_board)

            self.slice(surface, self.slice_speed, self.slice_pos, whole_tomato, self.slice_statuses, 105, 165, 20, "second")

            if self.rating_triggered:
                pygame.mixer.Sound.stop(slice_sound)
                self.rating_screen(surface, green_background, slice_tomato)
                    
                if self.next_step:
                    self.reset_status(2)

        # Define function to assemble burger
        def assemble_burger(surface):
            
            self.draw_cooking_background(surface, green_instruction_panel, kitchen_counter)

            if not self.cooking_done:
                self.game.draw_text(surface, "ASSEMBLE IN", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "RIGHT ORDER!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            self.game.draw_image(burger_assembly, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 5)
            self.game.draw_image(burger_sign, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 3.5)
            self.game.draw_image(plate, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2 + 55)
            self.game.draw_image(bottom_bun, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2 + 50)

            if self.burger_positions[1][0] == True:
               self.game.draw_image(self.burger_positions[1][1], 1, surface, self.game.GAME_X / 4, self.burger_positions[1][2])
            if self.burger_positions[2][0] == True:
               self.game.draw_image(self.burger_positions[2][1], 1, surface, self.game.GAME_X / 4, self.burger_positions[2][2])
            if self.burger_positions[3][0] == True:
               self.game.draw_image(self.burger_positions[3][1], 1, surface, self.game.GAME_X / 4, self.burger_positions[3][2])
            if self.burger_positions[4][0] == True:
               self.game.draw_image(self.burger_positions[4][1], 1, surface, self.game.GAME_X / 4, self.burger_positions[4][2])

            if self.burger_positions["done"]:
                self.game.draw_image(top_bun, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2 + 25)
                
            if self.cooking_done:
                self.display_rating_message(surface)

            if self.rating_triggered:
                self.rating_screen(surface, green_background, assemble_burger_a)

                if self.next_step:
                    self.reset_status(3)

        surface.fill(FANCY_MOSS)
        if self.step_1:
            cook_patty(surface)
        elif self.step_2:
            cut_tomato(surface)
        elif self.step_3:
            assemble_burger(surface)
        elif self.evaluation:
            self.final_rating(surface, "Burger", green_background)

    # Define method that cooks the fried chicken
    def cook_chicken(self, surface):

        def cut_chicken(surface):
            self.draw_cooking_background(surface, pink_instruction_panel, cutting_board)

            self.slice(surface, self.slice_speed, self.slice_pos, chicken_breast, self.slice_statuses, 105, 165, 25, "first")

            if self.rating_triggered:
                pygame.mixer.Sound.stop(slice_sound)
                self.rating_screen(surface, pink_background, slice_chicken_a)
                
                if self.next_step:
                    self.reset_status(1)

        def coat_chicken(surface):
            coated_chicken_button = Button(self.game.GAME_X / 4, 135, coated_chicken_1, 1)
            raw_chicken_button = Button(self.game.GAME_X / 4, 135, raw_chicken_1, 1) 
            self.draw_cooking_background(surface, pink_instruction_panel, cutting_board)
            self.game.draw_image(chicken_coating, 1, surface, self.game.GAME_X / 4, 130)
            
            if not self.cooking_done:
                
                self.game.draw_text(surface, "COAT THE", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "CHICKEN!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done:

                if self.chicken_coat_pos >= 104:
                    self.ingredient_rating["second"] = 1

                elif self.chicken_coat_pos > 35 and self.chicken_coat_pos < 104:
                    self.ingredient_rating["second"] = 2

                elif self.chicken_coat_pos <= 35:
                    self.ingredient_rating["second"] = 3

                self.display_rating_message(surface)

            self.game.draw_image(time_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            self.trigger_countdown(surface)

            if self.countdown_completed:

                self.game.draw_image(cooking_arrow, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4 - 65 + self.chicken_coat_pos, self.game.GAME_Y / 4 + 10)
                self.chicken_coat_pos += self.chicken_coat_speed

                self.game.draw_text(surface, str(self.chicken_coat_clicks), MINIMAL_FONT, NOBLE_BLACK, self.game.GAME_X / 4, 70)

                if raw_chicken_button.draw(surface) and self.chicken_coat_clicks >= 1:
                    self.chicken_coat_clicks -=1

                if self.chicken_coat_clicks == 0:
                    self.chicken_coat_speed = 0
                    if coated_chicken_button.draw(surface):
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                if self.chicken_coat_pos >= 135:
                    self.chicken_coat_speed = 0
                    if skip_button.draw(surface):
                        print(self.cooking_done)
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()
                        print(self.cooking_done)
    
                if self.rating_triggered:
                    self.rating_screen(surface, pink_background, coat_chicken_a)
                    
                if self.next_step:
                    self.reset_status(2)
                
        def fry_chicken(surface):
            self.draw_cooking_background(surface, pink_instruction_panel, deep_fryer)

            if not self.cooking_done:
                
                self.game.draw_text(surface, "FLIP AT THE", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "RIGHT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done: 
                
                if (self.burger_patty_pos >= 0 and self.burger_patty_pos <= 40) or self.burger_patty_pos > 90:
                    self.ingredient_rating["third"] = 1

                elif (self.burger_patty_pos > 40 and self.burger_patty_pos <= 50) or (self.burger_patty_pos > 80 and self.burger_patty_pos <= 90):
                    self.ingredient_rating["third"] = 2

                elif self.burger_patty_pos > 50 and self.burger_patty_pos <= 80:
                    self.ingredient_rating["third"] = 3

                self.display_rating_message(surface) 
                          
            # Draw the cooking bar that shows how cooked the patty is
            self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            # Prompt countdown
            self.trigger_countdown(surface)

            # Start cooking process when countdown is completed
            if self.countdown_completed:
                
                stop_button = Button(self.stop_button_posx, self.stop_button_posy, flip_button, 1)

                self.stop_button_posx += self.stop_button_velx
                self.stop_button_posy += self.stop_button_vely

                if self.stop_button_posx >= self.game.GAME_X / 2 - 9 or self.stop_button_posx <= 9:
                    self.stop_button_velx *= -1

                if self.stop_button_posy >= self.game.GAME_Y / 2 - 28 or self.stop_button_posy <= 5:
                    self.stop_button_vely *= -1

                if stop_button.draw(surface):
                    self.play_victory_music()
                    self.cooking_done = True
                    self.completed_time = pygame.time.get_ticks()
                    self.burger_patty_speed, self.stop_button_velx, self.stop_button_vely = 0, 0, 0

                self.game.draw_image(cooking_arrow, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4 - 65 + self.burger_patty_pos, self.game.GAME_Y / 4 + 10)
                
                self.burger_patty_pos += self.burger_patty_speed

                # Stops the cooking arrow when it reaches the end of the bar
                if self.burger_patty_pos >= 135:
                    self.burger_patty_speed, self.stop_button_velx, self.stop_button_vely = 0, 0, 0

                    if skip_button.draw(surface):
                        self.play_victory_music()
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                # Draw the appropriate patty depending on the cooking arrow position
                elif self.burger_patty_pos >= 0 and self.burger_patty_pos <= 40:
                    self.game.draw_image(coated_chicken_1, 1, surface, self.game.GAME_X / 4, 135)

                elif self.burger_patty_pos > 40 and self.burger_patty_pos <= 90:
                    self.game.draw_image(cooked_chicken_1, 1, surface, self.game.GAME_X / 4, 135)

                elif self.burger_patty_pos > 90:
                    self.game.draw_image(burned_chicken_1, 1, surface, self.game.GAME_X / 4, 135)

                if self.rating_triggered:
                    self.rating_screen(surface, pink_background, fry_chicken_a)
                    
                if self.next_step:
                    self.reset_status(3)

        surface.fill(CARNATION_ROSE)

        if self.step_1:
            cut_chicken(surface)
        elif self.step_2:
            coat_chicken(surface)
        elif self.step_3:
            fry_chicken(surface)
        elif self.evaluation:
            self.final_rating(surface, "Fried Chicken", pink_background)

    # Define method that cooks the stew
    def cook_stew(self, surface):

        # Define a methond for cutting the carrot
        def cut_carrot(surface):
            self.draw_cooking_background(surface, blue_instruction_panel, cutting_board)

            self.slice(surface, self.slice_speed, self.slice_pos, carrot, self.slice_statuses, 130, 150, 15, "first")

            if self.rating_triggered:
                self.rating_screen(surface, blue_background, slice_carrot_placeholder)
                    
                if self.next_step:
                    self.reset_status(1)
        
        # Define a method for cutting the beef
        def cut_beef(surface):
            
            self.draw_cooking_background(surface, blue_instruction_panel, cutting_board)

            if not self.cooking_done:

                self.game.draw_text(surface, "SLICE AS FAST", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "AS YOU CAN!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done:

                if self.beef_slice_pos >= 104:
                    self.ingredient_rating["second"] = 1

                elif self.beef_slice_pos > 35 and self.beef_slice_pos < 104:
                    self.ingredient_rating["second"] = 2

                elif self.beef_slice_pos <= 35:
                    self.ingredient_rating["second"] = 3

                self.display_rating_message(surface)

            self.game.draw_image(time_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            self.trigger_countdown(surface)

            if self.countdown_completed:

                self.game.draw_image(beef, 1, surface, self.game.GAME_X / 4, 135)

                button_12_pos_x = self.game.GAME_X / 4 - 25
                button_34_pos_x = self.game.GAME_X / 4
                button_56_pos_x = self.game.GAME_X / 4 + 25

                topbutton_pos_y = 105
                bottombutton_pos_y = 165

                self.game.draw_image(cooking_arrow, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4 - 65 + self.beef_slice_pos, self.game.GAME_Y / 4 + 10)
                self.beef_slice_pos += self.beef_slice_speed

                if self.beef_slice_pos >= 135:
                    self.beef_slice_speed = 0
                    if skip_button.draw(surface):
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                slice_1_button = Button(button_12_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_2_button = Button(button_12_pos_x, topbutton_pos_y, slice_icon, 1)
                slice_3_button = Button(button_34_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_4_button = Button(button_34_pos_x, topbutton_pos_y, slice_icon, 1)
                slice_5_button = Button(button_56_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_6_button = Button(button_56_pos_x, topbutton_pos_y, slice_icon, 1)

                if slice_1_button.draw(surface):
                    self.beef_slice[1] = True

                if self.beef_slice[1]:
                    if slice_2_button.draw(surface):
                        self.beef_slice[2] = True

                if self.beef_slice[2]:    
                    if slice_3_button.draw(surface):
                        self.beef_slice[3] = True

                if self.beef_slice[3]:
                    if slice_4_button.draw(surface):
                        self.beef_slice[4] = True

                if self.beef_slice[4]:
                    if slice_5_button.draw(surface):
                        self.beef_slice[5] = True

                if self.beef_slice[5]:
                    if slice_6_button.draw(surface):
                        self.beef_slice[6] = True
                        self.beef_slice_speed = 0
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                if self.beef_slice[1] and self.beef_slice[2]:
                    pygame.draw.line(surface, WARM_CROISSANT, (button_12_pos_x, bottombutton_pos_y),(button_12_pos_x, topbutton_pos_y))

                if self.beef_slice[3] and self.beef_slice[4]:
                    pygame.draw.line(surface, WARM_CROISSANT, (button_34_pos_x, bottombutton_pos_y),(button_34_pos_x, topbutton_pos_y))

                if self.beef_slice[5] and self.beef_slice[6]:
                    pygame.draw.line(surface, WARM_CROISSANT, (button_56_pos_x, bottombutton_pos_y),(button_56_pos_x, topbutton_pos_y))

                if self.rating_triggered:
                    self.rating_screen(surface, pink_background, slice_beef_placeholder)

                    if self.next_step:
                        self.reset_status(2)


        def make_stew(surface):
            self.draw_cooking_background(surface, blue_instruction_panel, kitchen_grill)

            # Changes the text in cooking papa's speech bubble depending on the conditions
            if not self.cooking_done:
                
                self.game.draw_text(surface, "CLICK AT THE", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "RIGHT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done: 
                
                if (self.stew_pos >= 0 and self.stew_pos <= 40) or self.stew_pos > 90:
                    self.ingredient_rating["third"] = 1

                elif (self.stew_pos > 40 and self.stew_pos <= 50) or (self.stew_pos > 80 and self.stew_pos <= 90):
                    self.ingredient_rating["third"] = 2

                elif self.stew_pos > 50 and self.stew_pos <= 80:
                    self.ingredient_rating["third"] = 3

                self.display_rating_message(surface) 
                          
            # Draw the cooking bar that shows how cooked the stew is
            self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            # Prompt countdown
            self.trigger_countdown(surface)

            # Start cooking process when countdown is completed
            if self.countdown_completed:
                
                # Initialize button
                stop_button = Button(self.stop_button_posx, self.stop_button_posy, click_button, 1)

                self.stop_button_posx += self.stop_button_velx
                self.stop_button_posy += self.stop_button_vely

                if self.stop_button_posx >= self.game.GAME_X / 2 - 9 or self.stop_button_posx <= 9:
                    self.stop_button_velx *= -1

                if self.stop_button_posy >= self.game.GAME_Y / 2 - 28 or self.stop_button_posy <= 5:
                    self.stop_button_vely *= -1

                if stop_button.draw(surface):
                    self.play_victory_music()
                    self.cooking_done = True
                    self.completed_time = pygame.time.get_ticks()
                    self.stew_speed, self.stop_button_velx, self.stop_button_vely = 0, 0, 0

                self.game.draw_image(cooking_arrow, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4 - 65 + self.stew_pos, self.game.GAME_Y / 4 + 10)
                
                self.stew_pos += self.stew_speed

                # Stops the cooking arrow when it reaches the end of the bar
                if self.stew_pos >= 135:
                    self.stew_speed, self.stop_button_velx, self.stop_button_vely = 0, 0, 0

                    if skip_button.draw(surface):
                        self.play_victory_music()
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                
                elif self.stew_pos >= 0 and self.stew_pos <= 40:
                    self.game.draw_image(pot, 1, surface, self.game.GAME_X / 4 + 7, 125)

                elif self.stew_pos > 40 and self.stew_pos <= 90:
                    self.game.draw_image(pot_smoke, 1, surface, self.game.GAME_X / 4 + 7, 110)

                elif self.stew_pos > 90:
                    self.game.draw_image(pot_smoke, 1, surface, self.game.GAME_X / 4 + 7, 110)

                if self.rating_triggered:
                    self.rating_screen(surface, blue_background, cook_stew_placeholder)
                    
                if self.next_step:
                    self.reset_status(3)

        surface.fill(YUCCA_CREAM)

        if self.step_1:
            cut_carrot(surface)
        elif self.step_2:
            cut_beef(surface)
        elif self.step_3:
            make_stew(surface)
        elif self.evaluation:
            self.final_rating(surface, "Stew", blue_background)

    # Define method for cooking steps that require slicing action
    def slice(self, surface, speed, arrow_pos, image, slice_status, top_pos, bottom_pos, x_offset, step):

            # Changes the text in cooking papa's speech bubble depending on the conditions
            if not self.cooking_done:
                
                self.game.draw_text(surface, "SLICE AS FAST", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "AS YOU CAN!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done:

                pygame.mixer.Sound.stop(slice_sound)

                if arrow_pos[0] >= 104:
                    self.ingredient_rating[step] = 1

                elif arrow_pos[0] > 35 and arrow_pos[0] < 104:
                    self.ingredient_rating[step] = 2

                elif arrow_pos[0] <= 35:
                    self.ingredient_rating[step] = 3

                self.display_rating_message(surface)

            self.game.draw_image(time_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            self.trigger_countdown(surface)

            if self.countdown_completed:     

                self.game.draw_image(image, 1, surface, self.game.GAME_X / 4, 135)

                button_12_pos_x = self.game.GAME_X / 4 - x_offset
                button_34_pos_x = self.game.GAME_X / 4
                button_56_pos_x = self.game.GAME_X / 4 + x_offset

                topbutton_pos_y = top_pos
                bottombutton_pos_y = bottom_pos

                self.game.draw_image(cooking_arrow, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4 - 65 + arrow_pos[0], self.game.GAME_Y / 4 + 10)
                
                if not self.cooking_done and not arrow_pos[0] >= 135:
                    arrow_pos.append(speed)
                    arrow_pos[0] += arrow_pos[1]
                    arrow_pos.pop()

                if arrow_pos[0] >= 135:
                    if skip_button.draw(surface):
                        if step == "third":
                            self.play_victory_music()
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                slice_1_button = Button(button_12_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_2_button = Button(button_12_pos_x, topbutton_pos_y, slice_icon, 1)
                slice_3_button = Button(button_34_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_4_button = Button(button_34_pos_x, topbutton_pos_y, slice_icon, 1)
                slice_5_button = Button(button_56_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_6_button = Button(button_56_pos_x, topbutton_pos_y, slice_icon, 1)

                if slice_1_button.draw(surface):
                    slice_status[1] = True

                if slice_status[1]:
                    if slice_2_button.draw(surface):
                        slice_status[2] = True
                        
                if slice_status[2]:    
                    if slice_3_button.draw(surface):
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(slice_sound))    
                        slice_status[3] = True
                            
                if slice_status[3]:
                    if slice_4_button.draw(surface):
                        slice_status[4] = True
                                
                if slice_status[4]:
                    if slice_5_button.draw(surface):
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(slice_sound))
                        slice_status[5] = True  
                                    
                if slice_status[5]:
                    if slice_6_button.draw(surface):
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(slice_sound))
                        slice_status[6] = True
                        if step == "third":
                            self.play_victory_music()
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                if slice_status[1] and slice_status[2]:
                    pygame.draw.line(surface, WARM_CROISSANT, (button_12_pos_x, bottombutton_pos_y),(button_12_pos_x, topbutton_pos_y))
                
                if slice_status[3] and slice_status[4]:
                    pygame.draw.line(surface, WARM_CROISSANT, (button_34_pos_x, bottombutton_pos_y),(button_34_pos_x, topbutton_pos_y))

                if slice_status[5] and slice_status[6]:
                    pygame.draw.line(surface, WARM_CROISSANT, (button_56_pos_x, bottombutton_pos_y),(button_56_pos_x, topbutton_pos_y))

                if self.rating_triggered:
                    for i in range(len(slice_status)):
                        slice_status[i] = False
                    
    # Clears the screen and shows the user's rating after a ingredient cooking step
    def rating_screen(self, surface, background_image, step_text_image):
        self.game.draw_image(background_image, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_image(step_text_image, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 4)
        
        if self.step_1:
            ingredient_rating = self.ingredient_rating["first"]
        elif self.step_2:
            ingredient_rating = self.ingredient_rating["second"]
        elif self.step_3:
            ingredient_rating = self.ingredient_rating["third"]

        if ingredient_rating == 3:
            self.game.draw_image(three_stars, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        elif ingredient_rating == 2:
            self.game.draw_image(two_stars, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        elif ingredient_rating == 1:
            self.game.draw_image(one_star, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)

    # Resets the status for cooking processes
    def reset_status(self, current_step):
        self.cooking_done = False
        self.countdown_triggered = False
        self.countdown_completed = False
        self.rating_triggered = False
        self.next_step = False

        if current_step == 1:
            self.step_1 = False
            self.step_2 = True

        elif current_step == 2:
            self.step_2 = False
            self.step_3 = True

        elif current_step == 3:
            self.step_3 = False
            self.evaluation = True

    # Draws a button that the player presses to trigger the countdown
    def trigger_countdown(self, surface):
        start_button = Button(self.game.GAME_X / 2, self.game.GAME_Y / 2, start, 1)
                
        if not self.countdown_triggered and not self.countdown_completed:
            if start_button.draw(surface):
                self.button_time = pygame.time.get_ticks()
                self.countdown_triggered = True

        if self.countdown[3]:
            self.game.draw_image(countdown_3, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)

        elif self.countdown[2]:
            self.game.draw_image(countdown_2, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)

        elif self.countdown[1]:
            self.game.draw_image(countdown_1, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)
            
    # Draws the right cooking background based on the color and cooking bg passed in as arguments
    def draw_cooking_background(self, surface, colourbg, cookingbg):
        self.game.draw_image(cookingbg, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)
        self.game.draw_image(colourbg, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 2)
        self.game.draw_image(cooking_papa, 1, surface, 215, 128)
        self.game.draw_image(papa_speech, 1, surface, 275, 110)

    def display_rating_message(self, surface):
        
        if self.step_1:
            ingredient_rating = self.ingredient_rating["first"]
        elif self.step_2:
            ingredient_rating = self.ingredient_rating["second"]
        elif self.step_3:
            ingredient_rating = self.ingredient_rating["third"]
        
        if ingredient_rating == 3:
            self.game.draw_text(surface, "PERFECT!", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
            self.game.draw_text(surface, "EXCELLENT JOB", MINIMAL_FONT, NOBLE_BLACK, 276, 110)

        elif ingredient_rating == 2:
            self.game.draw_text(surface, "GOOD JOB!", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
            self.game.draw_text(surface, "DOING GREAT!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

        elif ingredient_rating == 1:
            self.game.draw_text(surface, "TRY HARDER", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
            self.game.draw_text(surface, "NEXT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

    def final_rating(self, surface, recipe, bg_image):
        
        self.game.draw_image(bg_image, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)

        if recipe == "Burger":
            self.game.draw_image(burger_text, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 5)
            self.game.draw_image(burger, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        elif recipe == "Fried Chicken":
            self.game.draw_image(chicken_text, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 5)
            self.game.draw_image(chicken, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        elif recipe == "Stew":
            self.game.draw_image(stew_placeholder, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 5)
            self.game.draw_image(stew_final, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
            
        self.total_rating = self.ingredient_rating["first"] + self.ingredient_rating["second"] + self.ingredient_rating["third"]

        if self.total_rating >= 3 and self.total_rating < 6:
            self.game.draw_image(one_star, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2 + self.game.GAME_Y / 3)
        elif self.total_rating >=6 and self.total_rating < 9:
            self.game.draw_image(two_stars, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2 + self.game.GAME_Y / 3)
        elif self.total_rating == 9:
            self.game.draw_image(three_stars, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2 + self.game.GAME_Y / 3)

        if skip_button.draw(surface):
            self.game.actions["start"] = True
            self.game.customer_payment(self.total_rating)
            if self.game.music == True:
                pygame.mixer.music.unload()
                pygame.mixer.music.load(jojo_music)
                pygame.mixer.music.play(-1, 225)
            else:
                pygame.mixer.music.unload()
                pygame.mixer.music.load(default_music)
                pygame.mixer.music.play(-1)
        
    def play_victory_music(self):
            pygame.mixer.music.unload()
            pygame.mixer.music.load(victory_song)
            pygame.mixer.music.play(-1)

    








