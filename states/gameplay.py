# Purpose: Gameplay child class that inherits from State class, controls main game mechanics such as customer and recipe generating and cooking 

"""
To do list:
- Add return button to each cooking screen that goes back to restaurant
"""

#  Import required modules and classes
import random, time
from states.state import State
from button import Button
from assets.assets import * 

# Restaurant state define behaviour inside of restaurant when serving customers
class Restaurant(State):

    # Inherits from game and State class
    def __init__(self, game):
        State.__init__(self, game)
        
        # Nested dictionary of all possible recipes, the steps, and descriptions for each step
        self.possible_recipes =  {
            
            "Burger": {
                "Cook Patty": "Flip at the right time!",
                "Slice Tomato": "Click two points to make a slice.",
                "Assemble Burger": "Put the ingredients of the burger together by pressing the right button at the right time"
            },
            "Pizza": {
                "Roll Dough": "Scroll your mouse to move the rolling pin back and forth until the dough is rolled.",
                "Add Toppings": "Drag the toppings to the pizza.",
                "Place in Oven": "Put the pizza in the oven"
            },
            "Fried Chicken": {
                "": "",
                "": "",
                "": "",
            }
        }

        self.set_order()

    # Method that selects and returns a recipe from possible_recipes dictionary
    def generate_order(self): 
        selected = random.choice(list(self.possible_recipes.keys()))
        return(selected, self.possible_recipes[selected])

    # Method that selects and returns a customer image
    def generate_customer(self):
        possible_customers = [customer_1, customer_2, customer_3]
        return random.choice(possible_customers) 

    # Method that sets the returned recipes and customers and passes them to the game class variable current_recipe
    def set_order(self):
        returned = self.generate_order()
        self.selected_customer = self.generate_customer()
        self.selected_recipe = returned[0]
        self.game.current_recipe = self.selected_recipe

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
        surface.fill(WHISTLES_GOLD)
        self.game.draw_image(self.selected_customer, 1, surface, self.game.GAME_X / 2, 100)
        self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 105)
        self.game.draw_image(speech_bubble, 1, surface, self.game.GAME_X/ 2 + 60, self.game.GAME_Y / 2 - 50)
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
        
        icon_position = self.game.GAME_X/ 2 + 60, self.game.GAME_Y / 2 - 57
        
        if self.selected_recipe == "Burger":
            self.game.draw_image(burger_icon, 1, surface, icon_position[0], icon_position[1])

        elif self.selected_recipe == "Pizza":
            self.game.draw_image(pizza_icon, 1, surface, icon_position[0], icon_position[1])
        
        #elif self.selected_recipe == "Stew":
            #self.game.draw_image(stew_icon, 1, surface, icon_position[0], icon_position[1])

        elif self.selected_recipe == "Fried Chicken":
            self.game.draw_image(chicken_icon, 1, surface, icon_position[0], icon_position[1])

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
        self.ingredient_rating = None
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
        self.stop_button_posx, self.stop_button_posy = self.game.GAME_X / 4, self.game.GAME_Y / 5
        self.stop_button_velx, self.stop_button_vely = 1,1
        self.tomato_time_limit = 1500
        
        self.tomato_slice = {
            
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False

            }
        
        # Controls which step the user is currently on
        self.step_1 = True
        self.step_2 = False
        self.step_3 = False

        # Says whether a cooking step is completed 
        self.cooking_done = False

    # Things that happen when certain variables are modified through gameplay, is outside of render loop
    def update(self, actions):
        # If menu actions is triggered the main menu state is entered
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        # If countdown_triggered find the current time and compare it to the time when the countdown is triggered to set which numbers are shown on the screen
        if self.countdown_triggered:
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
            if current_time - self.button_time >= 4100 and current_time - self.button_time < 5100:
                
                # Reset countdown variable and set completed to true
                self.countdown_triggered = False
                self.countdown_completed = True

        # When one cooking step is completed wait some time and trigger the rating screen. Then wait some more time and switch to the next cooking step
        if self.cooking_done:
            if pygame.time.get_ticks() > self.completed_time + 3000:
                self.rating_triggered = True
                if pygame.time.get_ticks() > self.completed_time + 6000:
                    self.next_step = True

    # Render loop that continously updates screen based on current conditions 
    def render(self, surface):

        # Run the appropriate cooking process depending on the current customer order
        if self.current_recipe == "Burger":
            self.cook_burger(surface)
        elif self.current_recipe == "Pizza":
            self.cook_pizza(surface) 
        #elif self.current_recipe == "Stew":
            #self.cook_stew(surface)
        elif self.current_recipe == "Fried Chicken":
            self.cook_chicken(surface)

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
                    self.game.draw_text(surface, "TRY BETTER", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                    self.game.draw_text(surface, "NEXT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)
                    self.ingredient_rating = 1

                elif (self.burger_patty_pos > 40 and self.burger_patty_pos <= 50) or (self.burger_patty_pos > 80 and self.burger_patty_pos <= 90):
                    self.game.draw_text(surface, "GOOD JOB!", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                    self.game.draw_text(surface, "DOING GREAT!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)
                    self.ingredient_rating = 2

                elif self.burger_patty_pos > 50 and self.burger_patty_pos <= 80:
                    self.game.draw_text(surface, "PERFECT!", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                    self.game.draw_text(surface, "EXCELLENT JOB", MINIMAL_FONT, NOBLE_BLACK, 276, 110)
                    self.ingredient_rating = 3

                # Add the ingredient rating to the total recipe rating
                self.total_rating += self.ingredient_rating                

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

                # Draw the appropriate patty depending on the cooking arrow position
                elif self.burger_patty_pos >= 0 and self.burger_patty_pos <= 40:
                    self.game.draw_image(raw_patty, 1, surface, self.game.GAME_X / 4, 135)

                elif self.burger_patty_pos > 40 and self.burger_patty_pos <= 90:
                    self.game.draw_image(cooked_patty, 1, surface, self.game.GAME_X / 4, 135)

                elif self.burger_patty_pos > 90:
                    self.game.draw_image(burned_patty, 1, surface, self.game.GAME_X / 4, 135)

                if self.rating_triggered:
                    self.rating_screen(surface, green_background, "COOK PATTY")
                    
                if self.next_step:
                    self.reset_status(1)

        # Define method for cutting the tomato
        def cut_tomato(surface):
            self.draw_cooking_background(surface, green_instruction_panel, cutting_board)

            if not self.cooking_done:
                
                self.game.draw_text(surface, "SLICE AT THE", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                self.game.draw_text(surface, "RIGHT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)

            if self.cooking_done:

                if (self.burger_patty_pos >= 0 and self.burger_patty_pos <= 40) or self.burger_patty_pos > 90:
                    self.game.draw_text(surface, "TRY BETTER", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                    self.game.draw_text(surface, "NEXT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)
                    self.ingredient_rating = 1

                elif (self.burger_patty_pos > 40 and self.burger_patty_pos <= 50) or (self.burger_patty_pos > 80 and self.burger_patty_pos <= 90):
                    self.game.draw_text(surface, "GOOD JOB!", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                    self.game.draw_text(surface, "DOING GREAT!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)
                    self.ingredient_rating = 2

                elif self.burger_patty_pos > 50 and self.burger_patty_pos <= 80:
                    self.game.draw_text(surface, "PERFECT!", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
                    self.game.draw_text(surface, "EXCELLENT JOB", MINIMAL_FONT, NOBLE_BLACK, 276, 110)
                    self.ingredient_rating = 3

                self.total_rating += self.ingredient_rating
    
            self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            self.trigger_countdown(surface)

            if self.countdown_completed:
                
                stop_button = Button(self.game.GAME_X, 80, flip_button, 1)
                self.game.draw_image(whole_tomato, 1, surface, self.game.GAME_X / 4, 135)


                button_12_pos_x = self.game.GAME_X / 4 - 20
                button_34_pos_x = self.game.GAME_X / 4
                button_56_pos_x = self.game.GAME_X / 4 + 20

                topbutton_pos_y = 105
                bottombutton_pos_y = 165

                # IN PROGRESSSSSSSS
                slice_1_button = Button(button_12_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_2_button = Button(button_12_pos_x, topbutton_pos_y, slice_icon, 1)
                slice_3_button = Button(button_34_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_4_button = Button(button_34_pos_x, topbutton_pos_y, slice_icon, 1)
                slice_5_button = Button(button_56_pos_x, bottombutton_pos_y, slice_icon, 1)
                slice_6_button = Button(button_56_pos_x, topbutton_pos_y, slice_icon, 1)

                if slice_1_button.draw(surface):
                    self.tomato_slice[1] = True

                if self.tomato_slice[1] == True:
                    if slice_2_button.draw(surface):
                        self.tomato_slice[2] = True
                        
                if self.tomato_slice[2] == True:    
                    if slice_3_button.draw(surface):
                        self.tomato_slice[3] = True
                            
                if self.tomato_slice[3] == True:
                    if slice_4_button.draw(surface):
                        self.tomato_slice[4] = True
                                
                if self.tomato_slice[4] == True:
                    if slice_5_button.draw(surface):
                        self.tomato_slice[5] = True
                                    
                if self.tomato_slice[5] == True:
                    if slice_6_button.draw(surface):
                        self.tomato_slice[6] = True
                        self.cooking_done = True
                        self.completed_time = pygame.time.get_ticks()

                if self.rating_triggered:
                    self.rating_screen(surface, green_background, "SLICE TOMATO")
                    
                    if self.next_step:
                        self.reset_status(2)

        # Define function to assemble burger
        def assemble_burger(surface):
            self.draw_cooking_background(surface, green_instruction_panel, cutting_board)

        surface.fill(FANCY_MOSS)
        
        if self.step_1:
            cook_patty(surface)
        elif self.step_2:
            cut_tomato(surface)
        elif self.step_3:
            assemble_burger(surface)
        
    def cook_pizza(self, surface):

        def roll_dough(surface):
            self.draw_cooking_background(surface, pink_instruction_panel, cutting_board)

        def add_sauce(surface):
            pass

        def add_toppings(surface):
            pass

        surface.fill(CARNATION_ROSE)
        if self.step_1:
            roll_dough(surface)
        elif self.step_2:
            add_sauce(surface)
        elif self.step_3:
            add_toppings(surface)

    """
    def cook_stew(self, surface):

        def step_1(surface):
            pass

        def step_2(surface):
            pass

        def step_3(surface):
            pass

        surface.fill(KASHMIR_PINK)
        step_1(surface)
        step_2(surface)
        step_3(surface)
    """

    def cook_chicken(self, surface):

        def step_1(surface):
            pass

        def step_2(surface):
            pass

        def step_3(surface):
            pass

        surface.fill(WARM_CROISSANT)
        step_1(surface)
        step_2(surface)
        step_3(surface)

    # Clears the screen and shows the user's rating after a ingredient cooking step
    def rating_screen(self, surface, background_image, step_name):
        self.game.draw_image(background_image, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        self.game.draw_text(surface, str(step_name), MARIO_FONT, NOBLE_BLACK, self.game.GAME_X / 2, self.game.GAME_Y / 4)
        self.game.draw_text(surface, str(self.ingredient_rating), MARIO_FONT, NOBLE_BLACK, self.game.GAME_X / 2, self.game.GAME_Y / 2)
        
        # Change text to number of stars by drawing with offsets in for loop. Fionna do this pls
        # FIONNA

    # Resets the status for cooking processes
    def reset_status(self, current_step):
        self.cooking_done = False
        self.countdown_triggered = False
        self.countdown_completed = False
        self.rating_triggered = False
        self.ingredient_rating = 0
        self.next_step = False

        if current_step == 1:
            self.step_1 = False
            self.step_2 = True

        elif current_step == 2:
            self.step_2 = False
            self.step_3 = True

        elif current_step == 3:
            self.step_3 = False

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








