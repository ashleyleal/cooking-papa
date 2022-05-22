# Purpose: Gameplay child class that inherits from State class, controls main game mechanics such as customer and recipe generating and cooking 

"""
To do list:

- Add return button to each cooking screen that goes back to restaurant

"""

import random, time
from states.state import State
from button import Button
from assets.assets import * 

class Gameplay(State):

    def __init__(self, game):
        State.__init__(self, game)
        
        self.set_order()
        self.kitchen_entered = False

    def generate_order(self): 
        possible_recipes = {
            "Burger": {
                "Cook Patty": "Wait unti the bar reaches the middle to ensure that the patty is cooked.",
                "Slice Tomato": "Click two points to make a slice.",
                "Assemble Burger": "Put the ingredients of the burger together"
            },
            "Pizza": {
                "Roll Dough": "Scroll your mouse to move the rolling pin back and forth until the dough is rolled.",
                "Add Toppings": "Drag the toppings to the pizza.",
                "Place in Oven": "Put the pizza in the oven"
            },
            "Stew": {
                "Cut vegetables": "",
                "": "",
                "": "",
            },
            "Fried Chicken": {
                "": "",
                "": "",
                "": "",
            }
        }
        return(random.choice(list(possible_recipes.keys())))

    def generate_customer(self):
        possible_customers = [customer_1, customer_2, customer_3]
        return random.choice(possible_customers) 

    def set_order(self):
        self.selected_customer = self.generate_customer()
        self.selected_recipe = self.generate_order()

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        if actions["recipe"]:
            self.set_order()

        if actions["restaurant"]:
            new_state = Gameplay(self.game)
            new_state.enter_state()

    def render(self, surface):

        if not self.kitchen_entered:
            surface.fill(WHISTLES_GOLD)
            self.game.draw_image(self.selected_customer, 1, surface, self.game.GAME_X / 2, 100)
            self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 105)
            self.game.draw_image(speech_bubble, 1, surface, self.game.GAME_X/ 2 + 60, self.game.GAME_Y / 2 - 50)
            self.show_order(surface)

            if return_button.draw(surface):
                self.game.actions["menu"] = True

            if decline_order_button.draw(surface):
                self.game.actions["recipe"] = True

            if confirm_order_button.draw(surface):
                self.kitchen_entered = True

                if self.selected_recipe == "Burger":
                    self.cook_burger(surface)

                elif self.selected_recipe == "Pizza":
                    self.cook_pizza(surface) 

                elif self.selected_recipe == "Stew":
                    self.cook_stew(surface)
            
                elif self.selected_recipe == "Fried Chicken":
                    self.cook_chicken(surface)

        
    def show_order(self, surface):  # MUST BE INSIDE OF LOOP
        
        icon_position = self.game.GAME_X/ 2 + 60, self.game.GAME_Y / 2 - 57
        
        if self.selected_recipe == "Burger":
            self.game.draw_image(burger_icon, 1, surface, icon_position[0], icon_position[1])

        elif self.selected_recipe == "Pizza":
            self.game.draw_image(pizza_icon, 1, surface, icon_position[0], icon_position[1])

        elif self.selected_recipe == "Stew":
            self.game.draw_image(stew_icon, 1, surface, icon_position[0], icon_position[1])

        elif self.selected_recipe == "Fried Chicken":
            self.game.draw_image(chicken_icon, 1, surface, icon_position[0], icon_position[1])


    def cook_burger(self, surface):

        def cook_patty(surface):
            self.game.draw_image(kitchen_grill, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)
            #pygame.draw.rect(surface, PALACE_ARMS, pygame.Rect(self.game.GAME_X - self.game.GAME_X / 2, 0, self.game.GAME_X / 2, self.game.GAME_Y))
            self.game.draw_image(instruction_panel, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 2)
            #self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 4)
            #self.game.draw_image(raw_patty, 1, surface, self.game.GAME_X / 4, 135)

        # create variable for performance rating
        # define variable for position of cooking arrow
        # define velocity of cooking arrow
        #draw grill
        #draw cooking bar and arrow
        #draw raw patty
        #if arrow reaches middle draw cooked patty
        # if arrow reaches red draw burned patty
        # when player clicks, set velocity to 0
        # if player clicks when position is in blue or red area, 1 point to accumulator
        # if yellow area, 2 points
        # if green area, 3 points
        # return points


        def cut_tomato(surface):

            # create variable for performance rating
            # draw counter and cutting board
            # draw whole tomato

            pass

        def assemble_burger(surface):
            pass

        surface.fill(FANCY_MOSS)
        cook_patty(surface)
        cut_tomato(surface)
        
    def cook_pizza(self, surface):

        def roll_dough(surface):
            self.game.draw_image(cutting_board, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)

        def add_sauce(surface):
            pass

        def add_toppings(surface):
            pass

        surface.fill(MINERAL_RED)
        roll_dough(surface)
        add_sauce(surface)
        add_toppings(surface)

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




