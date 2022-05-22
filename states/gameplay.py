import random, time
from states.state import State
from button import Button
from assets.assets import * 

class Gameplay(State):

    def __init__(self, game):
        State.__init__(self, game)

        self.selected_customer = self.generate_customer()
        self.selected_recipe = self.generate_order()
        
        self.enter_kitchen = False

        print(self.selected_recipe)

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        if actions["recipe"]:
            self.enter_kitchen = True

    def render(self, surface):

        if not self.enter_kitchen:
            surface.fill(WHISTLES_GOLD)
            self.game.draw_image(self.selected_customer, 1, surface, self.game.GAME_X / 2, 100)
            self.game.draw_image(restaurant_counter, 1, surface, self.game.GAME_X / 2, 100)
            self.game.draw_image(speech_bubble, 1, surface, self.game.GAME_X/ 2 + 60, self.game.GAME_Y / 2 - 50)
            self.show_order(surface)

        if return_button.draw(surface):
                self.game.actions["menu"] = True 

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
        possible_customers = [placeholder_customer]
        return random.choice(possible_customers) 

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

        

        




