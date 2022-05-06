import pygame, random
from module import *




def generate_customer(posx, posy, surface):

    # Choose random name
    # Draw customer base image
    customer_base = pygame.image.load("assets/images/images/customer_base.png")
    draw_image(customer_base, 1, surface, posx, posy)
    # Get customer base image rectangle
    customer_rect = customer_base.get_rect()
    # Load clothing and accessories images
    # Draw clothing and accessories according to customer base rectangle

# All accessories and clothing must be the same resolution and centered to ensure that it is applied to the customer base properly

possible_recipes = {

    "Burger": ["Cook Patty", "Slice Tomato", "Add Sauce"],
    "Pasta": ["Stir Pasta", "Drain Pasta", "Add Sauce"]

    }

def choose_recipe(self):
    print("Lol")
    selected_recipe = random.choice(possible_recipes)
    print(selected_recipe)

# Cooking mechanism

# Define functions for every possible "minigame" ingredient preparation

# Assign functions to recipes and cooking animations

# Calculate player accuracy

# Calculate gold profit



