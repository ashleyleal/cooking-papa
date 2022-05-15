import random
from states.state import State
from button import Button
from assets.assets import *

class Gameplay(State):

    def __init__(self, game):
        State.__init__(self, game)
        
        self.current_recipe = None

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        if actions["recipe"]:
            self.current_recipe = self.generate_order()

    def render(self, surface):

        if not self.game.actions["recipe"]:
            surface.fill(WHISTLES_GOLD)
            self.game.draw_text(surface, "game started", MARIO_FONT, NOBLE_BLACK, self.game.GAME_X / 2, 50)
            self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 100)
            if return_button.draw(surface):
                self.game.actions["menu"] = True 

        if check_button.draw(surface):
            self.game.actions["recipe"] = True
            
        if self.current_recipe == "Burger":
            self.cook_burger(surface)
        
        elif self.current_recipe == "Pizza":
            self.cook_pizza(surface)

        elif self.current_recipe == "Stew":
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

           # "Stew": {
                #Instructions
           # },
        }
        return(random.choice(list(possible_recipes.keys())))
        

    def generate_customer(self):
        possible_customers = []
        # selected customer is a random choice of the possible customers

    def cook_burger(self, surface):

        surface.fill(FANCY_MOSS)
        self.game.draw_image(kitchen_grill, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)
        self.game.draw_image(raw_burger_patty, 1, surface, self.game.GAME_X / 4, 135)


    def cook_pizza(self, surface):
        
        surface.fill(MINERAL_RED)

    def cook_stew(self, surface):
        pass

    def clear_recipe(self):
        self.current_recipe = None
        self.game.actions["recipe"] = False



