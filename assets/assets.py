# Purpose: Load assets and buttons to keep main program and class programs uncluttered

import pygame
from button import Button

pygame.font.init()
pygame.mixer.init()

MARBLE_WHITE = (242, 240, 229)
SILVER_BULLET = (184, 181, 185)
SUVA_GREY = (134, 129, 136)
DIGITAL_GREY = (100, 99, 101)
NIGHT_GREY = (69, 68, 79)
MAGIC_NIGHT = (58, 56, 88)
NOBLE_BLACK = (33, 33, 35)
OBSIDIAN_BLACK = (53, 43, 66)
PALACE_ARMS = (67, 67, 106)
BLUE_SONKI = (75, 128, 202)
ARCTIC_OCEAN = (104, 194, 211)
YUCCA_CREAM = (162, 220, 199)
WHISTLES_GOLD = (237, 225, 158)
DESERT_CARAVAN = (211, 160, 104)
MINERAL_RED = (180, 82, 82)
MEDICINE_MAN = (106, 83, 110)
SOVEREIGN = (75, 65, 88)
SEQUOIA = (128, 73, 58)
TUSCAN_SOIL = (167, 123, 91)
WARM_CROISSANT = (229, 206, 180)
SOFT_FERN = (194, 211, 104)
BROCCOLI = (138, 176, 96)
GREEN_HOUR = (86, 123, 121)
DEEP_EVERGREEN = (78, 88, 74)
FERN_SHADE = (123, 114, 67)
FANCY_MOSS = (178, 180, 126)
KASHMIR_PINK = (237, 200, 196)
CARNATION_ROSE = (207, 138, 203)
PURPLE_STONE = (95, 85, 106)

# Fonts
MARIO_FONT = pygame.font.Font("assets/fonts/Mario-Kart-DS.ttf", 18)
PIXELLARI_FONT = pygame.font.Font("assets/fonts/Pixellari.ttf", 11)
PRESS_START_FONT = pygame.font.Font("assets/fonts/PressStart.ttf", 6)
MINIMAL_FONT = pygame.font.Font("assets/fonts/minimal.ttf", 15)

cooking_papa = pygame.image.load("assets/images/images/cooking_papa.png")
papa_speech = pygame.image.load("assets/images/images/papas_bubble.png")

# Main Menu Assets
game_logo = pygame.image.load("assets/images/titles/cookingPapaPlaceholderTitle.png")
play_button = pygame.image.load("assets/images/icons/play_button.png")
shop_button = pygame.image.load("assets/images/icons/shop_button.png")
quit_button = pygame.image.load("assets/images/icons/quit_button.png")

placeholder_button = pygame.image.load("assets/images/icons/buttonPlaceholder.png")
return_arrow = pygame.image.load("assets/images/icons/return_arrow.png")
gold_icon = pygame.image.load("assets/images/icons/coin.png")
check_mark = pygame.image.load("assets/images/icons/check_mark.png")
red_cross = pygame.image.load("assets/images/icons/red_cross.png")
start = pygame.image.load("assets/images/icons/start_button.png")

# Customers
customer_1 = pygame.image.load("assets/images/images/customer_1.png")
customer_2 = pygame.image.load("assets/images/images/customer_2.png")
customer_3 = pygame.image.load("assets/images/images/customer_3.png")

# Kitchen assets
restaurant_counter = pygame.image.load("assets/images/images/restaurant_counter.png")
kitchen_grill = pygame.image.load("assets/images/images/kitchen_grill.png")
cutting_board = pygame.image.load("assets/images/images/kitchen_cutting_board.png")

pink_instruction_panel = pygame.image.load("assets/images/images/papas_background_pink.png")
green_instruction_panel = pygame.image.load("assets/images/images/papas_background_green.png")
cooking_bar = pygame.image.load("assets/images/images/cooking_bar.png")
speech_bubble = pygame.image.load("assets/images/icons/speech_bubble.png")

# Order icons
burger_icon = pygame.image.load("assets/images/icons/burger_icon.png")
pizza_icon = pygame.image.load("assets/images/icons/pizza_icon.png")
chicken_icon = pygame.image.load("assets/images/icons/chicken_icon.png")
stew_icon = pygame.image.load("assets/images/icons/stew_icon.png")

# Burger
burger = pygame.image.load("assets/images/images/burger.png")
raw_patty = pygame.image.load("assets/images/images/raw_burger_patty.png")
cooked_patty = pygame.image.load("assets/images/images/cooked_burger_patty.png")
burned_patty = pygame.image.load("assets/images/images/burned_burger_patty.png")
top_bun = pygame.image.load("assets/images/images/top_burger_bun.png")
bottom_bun = pygame.image.load("assets/images/images/bottom_burger_bun.png")
sliced_tomato = pygame.image.load("assets/images/images/burger_sliced_tomato.png")
whole_tomato = pygame.image.load("assets/images/images/burger_whole_tomato.png")
lettuce = pygame.image.load("assets/images/images/burger_lettuce.png")
cheese = pygame.image.load("assets/images/images/burger_cheese.png")

# Reocurring buttons
return_button = Button(20, 20, return_arrow, 1)
confirm_order_button = Button(300, 160, check_mark, 1)
decline_order_button = Button(25, 160, red_cross, 1)

menu_music = "assets/sounds/menu_music.mp3"

# Countdown
countdown_3 = pygame.image.load("assets/images/images/number_3.png")
countdown_2 = pygame.image.load("assets/images/images/number_2.png")
countdown_1 = pygame.image.load("assets/images/images/number_1.png")
