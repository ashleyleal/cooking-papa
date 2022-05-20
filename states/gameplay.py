# Purpose: Gameplay child class that inherits from State class 

import random, time
from states.state import State
from button import Button
from assets.assets import *

class Gameplay(State):

    def __init__(self, game):
        State.__init__(self, game)
        
        self.selected_recipe = None
        self.current_recipe = None

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        if actions["recipe"]:
            self.selected_recipe = self.generate_order()
            pygame.time.delay(1000)
            self.current_recipe = self.selected_recipe

    def render(self, surface):

        if not self.game.actions["recipe"]:
            surface.fill(WHISTLES_GOLD)
            self.game.draw_text(surface, "game started", MARIO_FONT, NOBLE_BLACK, self.game.GAME_X / 2, 50)
            self.generate_customer(surface)
            self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 100)
            if return_button.draw(surface):
                self.game.actions["menu"] = True 

        if check_button.draw(surface):
            self.game.actions["recipe"] = True
 
        if self.selected_recipe == "Burger":
            self.game.draw_image(burger, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)
            if self.current_recipe == "Burger":
                self.cook_burger(surface)
        
        elif self.selected_recipe == "Pizza":
            self.cook_pizza(surface)

        elif self.selected_recipe == "Stew":
            self.cook_stew(surface)


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

    def show_order(self, surface):
        self.game.draw_image


    def generate_customer(self, surface):
        possible_customers = []
        # selected customer is a random choice of the possible customers
        self.game.draw_image(placeholder_customer, 1, surface, self.game.GAME_X / 2, self.game.GAME_Y / 2)

    def cook_burger(self, surface):

        # create accumulator variable for performance rating (outside of loop)
        # fill screen
        surface.fill(FANCY_MOSS)
        self.cook_patty(surface)
        self.cut_tomato(surface)

    def cook_patty(self, surface):
        self.game.draw_image(kitchen_grill, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)
        self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 4)
        self.game.draw_image(raw_patty, 1, surface, self.game.GAME_X / 4, 135)

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


    def cut_tomato(self, surface):

        # create variable for performance rating
        # draw counter and cutting board
        # draw whole tomato

        pass

    def assemble_burger(self, surface):
        pass


    def cook_pizza(self, surface):
        
        surface.fill(MINERAL_RED)

    def cook_stew(self, surface):
        pass

    def clear_recipe(self):
        self.current_recipe = None
        self.game.actions["recipe"] = False



