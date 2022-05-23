# Purpose: Gameplay child class that inherits from State class, controls main game mechanics such as customer and recipe generating and cooking 

"""
To do list:

- Add return button to each cooking screen that goes back to restaurant
- Will need to make another state for being in the kitchen because buttons don't work after screen flipped

"""
import random, time
from states.state import State
from button import Button
from assets.assets import * 

class Restaurant(State):

    def __init__(self, game):
        State.__init__(self, game)
        
        self.possible_recipes =  {
            "Burger": {
                "Cook Patty": "Flip at the right time!",
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

        self.set_order()

    def generate_order(self): 
        selected = random.choice(list(self.possible_recipes.keys()))
        return(selected, self.possible_recipes[selected])

    def generate_customer(self):
        possible_customers = [customer_1, customer_2, customer_3]
        return random.choice(possible_customers) 

    def set_order(self):
        returned = self.generate_order()
        self.selected_customer = self.generate_customer()
        self.selected_recipe = returned[0]
        self.game.current_recipe = self.selected_recipe

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        if actions["recipe"]:
            self.set_order()

        if actions["cooking"]:
            new_state = Kitchen(self.game)
            new_state.enter_state()

    def render(self, surface):

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
            self.game.actions["cooking"] = True

        
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


class Kitchen(State):

    def __init__(self, game):
        State.__init__(self, game)

        self.current_recipe = self.game.current_recipe
        self.countdown_triggered = False
        
        self.countdown = {

            3: False,
            2: False,
            1: False

        }

    def update(self, actions):
        if actions["menu"]:
            main_menu = self.game.state_stack[0]
            main_menu.enter_state()

        if self.countdown_triggered:
            current_time = pygame.time.get_ticks()
            print(current_time)
            
            print("3")
            self.countdown[3] = True
            
            if pygame.time.get_ticks() >= current_time + 1:
                print("2")
                self.countdown[3] = False
                self.countdown[2] = True
            elif pygame.time.get_ticks() == current_time + 2000:
                print("1")
                self.countdown[2] = False
                self.countdown[1] = True
            elif pygame.time.get_ticks() == current_time + 3000:
                self.countdown[1] = True
            elif pygame.time.get_ticks() == current_time + 4000:
                self.countdown_triggered = False


    def render(self, surface):

        if self.current_recipe == "Burger":
            self.cook_burger(surface) 


    def cook_burger(self, surface):

        def cook_patty(surface):
            self.game.draw_image(kitchen_grill, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)
            #pygame.draw.rect(surface, PALACE_ARMS, pygame.Rect(self.game.GAME_X - self.game.GAME_X / 2, 0, self.game.GAME_X / 2, self.game.GAME_Y))
            self.game.draw_image(green_instruction_panel, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 2)
            self.game.draw_image(cooking_papa, 1, surface, 215, 128)
            self.game.draw_image(papa_speech, 1, surface, 275, 110)
            #self.game.draw_text(surface, str(self.possible_recipes[self.selected_recipe]["Cook Patty"]), PIXELLARI_FONT, NOBLE_BLACK, 275, 110)
            self.game.draw_text(surface, "FLIP AT THE", MINIMAL_FONT, NOBLE_BLACK, 275, 95)
            self.game.draw_text(surface, "RIGHT TIME!", MINIMAL_FONT, NOBLE_BLACK, 275, 110)
            self.game.draw_image(cooking_bar, 1, surface, self.game.GAME_X / 2 + self.game.GAME_X / 4, self.game.GAME_Y / 4)

            start_button = Button(self.game.GAME_X / 2, self.game.GAME_Y / 2, play_button, 1)
            if start_button.draw(surface):
                self.countdown_triggered = True

            if self.countdown[3]:
                print("3")
                self.game.draw_image(countdown_3, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)

            elif self.countdown[2]:
                print("2")
                self.game.draw_image(countdown_2, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)

            elif self.countdown[1]:
                print("1")
                self.game.draw_image(countdown_1, 1, surface, self.game.GAME_X / 4, self.game.GAME_Y / 2)

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


