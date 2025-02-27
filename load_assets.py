'''
-------------------------------------------------------------------------------
Name:  load_assets.py
Course: ICS4U1
Purpose: Load assets and frequently used buttons to keep main program and class files uncluttered
 
Author:   Ashley L & Fionna C
Created:  28/04/2022
------------------------------------------------------------------------------
'''

import pygame
from button import Button

pygame.font.init()
pygame.mixer.init(48000, -16, 1, 1024)

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
MARIO_FONT = pygame.font.Font("assets/fonts/Mario-Kart-DS.ttf", 25)
PIXELLARI_FONT = pygame.font.Font("assets/fonts/Pixellari.ttf", 11)
PRESS_START_FONT = pygame.font.Font("assets/fonts/PressStart.ttf", 6)
MINIMAL_FONT = pygame.font.Font("assets/fonts/minimal.ttf", 15)

cooking_papa = pygame.image.load("assets/images/images/cooking_papa.png")
papa_speech = pygame.image.load("assets/images/images/papas_bubble.png")

# Main Menu Assets
menu_bg = pygame.image.load("assets/images/images/Menu_bg.png")
game_logo = pygame.image.load("assets/images/images/main_menu_title.png")
play_button = pygame.image.load("assets/images/icons/Play.png")
shop_button = pygame.image.load("assets/images/icons/Shop.png")
quit_button = pygame.image.load("assets/images/icons/Quit.png")

# Shop Menu Assets
shop_title = pygame.image.load("assets/images/titles/Shop_title.png")
characters_button = pygame.image.load("assets/images/images/characters_button.png")
recolour_button = pygame.image.load("assets/images/images/recolour_button.png")
music_button = pygame.image.load("assets/images/images/music_button.png")
ok_button = pygame.image.load("assets/images/icons/ok_button.png")
confirm_purchase_bg = pygame.image.load("assets/images/images/Confirm_purchase_bg.png")
insuficent_funds_bg = pygame.image.load("assets/images/images/insuficent_funds.png")
Recolour_center_button = pygame.image.load("assets/images/images/Recolour_center_button.png")
price = pygame.image.load("assets/images/images/coin.png")
recolour_option_1 = pygame.image.load("assets/images/images/Recolour_option_1.png")
recolour_option_2 = pygame.image.load("assets/images/images/Recolour_option_2.png")
Wallpaper_title = pygame.image.load("assets/images/titles/Wallpaper_title.png")
purchased_bg = pygame.image.load("assets/images/images/Purchased_bg.png")
recolour_1 = pygame.image.load("assets/images/images/recolour_1.png")
recolour_2 = pygame.image.load("assets/images/images/recolour_2.png")
character_title = pygame.image.load("assets/images/titles/character_title.png")
speedwagon_buy = pygame.image.load("assets/images/images/speedwagon_buy.png")
speedwagon_buy_button = pygame.image.load("assets/images/images/speedwagon_buy_button.png")
speedwagon = pygame.image.load("assets/images/images/speedwagon.png")
equip_button = pygame.image.load("assets/images/icons/equip_button.png")
active_button = pygame.image.load("assets/images/icons/active_button.png")
recolour_pink = pygame.image.load("assets/images/images/recolour_11.png")
recolour_green = pygame.image.load("assets/images/images/recolour_22.png")
music_buy = pygame.image.load("assets/images/images/part_5_music.png")
music_title = pygame.image.load("assets/images/titles/music_title.png")
menu_music_button = pygame.image.load("assets/images/images/menu_music_button.png")

placeholder_button = pygame.image.load("assets/images/icons/buttonPlaceholder.png")
return_arrow = pygame.image.load("assets/images/icons/return_button.png")
skip_arrow = pygame.image.load("assets/images/icons/skip_button.png")
gold_icon = pygame.image.load("assets/images/icons/coin.png")
check_mark = pygame.image.load("assets/images/icons/Confirm_button.png")
red_cross = pygame.image.load("assets/images/icons/Cancel_button.png")
start = pygame.image.load("assets/images/icons/start_button.png")

# Customers
customer_1 = pygame.image.load("assets/images/images/Dio.png")
customer_2 = pygame.image.load("assets/images/images/Jotaro.png")
customer_3 = pygame.image.load("assets/images/images/funny_valentine.png")
customer_4 = pygame.image.load("assets/images/images/speedwagon.png")

# Kitchen assets
restaurant_counter = pygame.image.load("assets/images/images/restaurant_counter.png")
kitchen_grill = pygame.image.load("assets/images/images/kitchen_grill.png")
cutting_board = pygame.image.load("assets/images/images/kitchen_cutting_board.png")
kitchen_counter = pygame.image.load("assets/images/images/kitchen_counter.png")
deep_fryer = pygame.image.load("assets/images/images/kitchen_deep_fryer.png")
plate = pygame.image.load("assets/images/images/plate.png")

# Stew
carrot = pygame.image.load("assets/images/images/carrot.png")
beef = pygame.image.load("assets/images/images/beef.png")
stew_final = pygame.image.load("assets/images/images/stew_final.png")
pot = pygame.image.load("assets/images/images/pot.png")
slice_carrot_placeholder = pygame.image.load("assets/images/titles/slice_carrot_title.png")
slice_beef_placeholder = pygame.image.load("assets/images/titles/slice_beef_title.png")
cook_stew_placeholder = pygame.image.load("assets/images/titles/cook_stew_title.png")
stew_placeholder = pygame.image.load("assets/images/titles/stew_title.png")
click_button = pygame.image.load("assets/images/icons/click_button.png")
pot_smoke = pygame.image.load("assets/images/images/pot_smoke.png")

# Instruction panels
pink_instruction_panel = pygame.image.load("assets/images/images/papas_background_pink.png")
green_instruction_panel = pygame.image.load("assets/images/images/papas_background_green.png")
blue_instruction_panel = pygame.image.load("assets/images/images/papas_background_blue.png")

# Solid backgrounds
green_background = pygame.image.load("assets/images/images/papas_background_green_full.png")
pink_background = pygame.image.load("assets/images/images/papas_background_pink_full.png")
blue_background = pygame.image.load("assets/images/images/papas_background_blue_full.png")

# Cooking assets
cooking_bar = pygame.image.load("assets/images/images/cooking_bar.png")
time_bar = pygame.image.load("assets/images/images/time_bar.png")
cooking_arrow = pygame.image.load("assets/images/icons/cooking_arrow.png")
flip_button = pygame.image.load("assets/images/icons/flip_button.png")
speech_bubble = pygame.image.load("assets/images/icons/speech_bubble.png")
up_arrow = pygame.image.load("assets/images/icons/orange_up.png")
right_arrow = pygame.image.load("assets/images/icons/green_right.png")
left_arrow = pygame.image.load("assets/images/icons/pink_left.png")
down_arrow = pygame.image.load("assets/images/icons/blue_down.png")


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
slice_icon = pygame.image.load("assets/images/icons/slice_thing.png")
burger_assembly = pygame.image.load("assets/images/images/burger_assembly.png")
burger_sign = pygame.image.load("assets/images/images/burger_sign.png")

cook_patty_a = pygame.image.load("assets/images/images/cook_patty.png")
slice_tomato = pygame.image.load("assets/images/images/slice_tomato.png")
assemble_burger_a = pygame.image.load("assets/images/images/assemble_burger.png")
burger_text = pygame.image.load("assets/images/images/burger_text.png")

# Chicken
chicken = pygame.image.load("assets/images/images/chicken.png")
chicken_breast = pygame.image.load("assets/images/images/chicken_breast.png")
chicken_coating = pygame.image.load("assets/images/images/chicken_coating.png")
raw_chicken_1 = pygame.image.load("assets/images/images/raw_chicken1.png")
raw_chicken_2 = pygame.image.load("assets/images/images/raw_chicken2.png")
raw_chicken_3 = pygame.image.load("assets/images/images/raw_chicken3.png")
coated_chicken_1 = pygame.image.load("assets/images/images/raw_chicken1.png")
coated_chicken_2 = pygame.image.load("assets/images/images/raw_chicken2.png")
coated_chicken_3 = pygame.image.load("assets/images/images/raw_chicken3.png")
cooked_chicken_1 = pygame.image.load("assets/images/images/cooked_chicken1.png")
cooked_chicken_2 = pygame.image.load("assets/images/images/cooked_chicken2.png")
cooked_chicken_3 = pygame.image.load("assets/images/images/cooked_chicken3.png")
burned_chicken_1 = pygame.image.load("assets/images/images/burned_chicken1.png")
burned_chicken_2 = pygame.image.load("assets/images/images/burned_chicken2.png")
burned_chicken_3 = pygame.image.load("assets/images/images/burned_chicken3.png")

coat_chicken_a = pygame.image.load("assets/images/images/coat_chicken.png")
slice_chicken_a = pygame.image.load("assets/images/images/slice_chicken.png")
fry_chicken_a = pygame.image.load("assets/images/images/fry_chicken.png")
chicken_text = pygame.image.load("assets/images/images/fried_chicken.png")

# Reocurring buttons
return_button = Button(20, 20, return_arrow, 1)
skip_button = Button(300, 160, skip_arrow, 1)
confirm_order_button = Button(300, 160, check_mark, 1)
decline_order_button = Button(25, 160, red_cross, 1)

# Sounds
countdown_sound = pygame.mixer.Sound("assets/sounds/countdown.wav")
sizzling_sound = pygame.mixer.Sound("assets/sounds/sizzling.wav")
slice_sound = pygame.mixer.Sound("assets/sounds/slice.wav")

# Music
default_music = "assets/sounds/menu_music.mp3"
jojo_music = "assets/sounds/jojo_theme.mp3"
alishas_song = "assets/sounds/lil_cafe_beat.wav"
victory_song = "assets/sounds/victory.wav"

# Countdown
countdown_3 = pygame.image.load("assets/images/images/number_3.png")
countdown_2 = pygame.image.load("assets/images/images/number_2.png")
countdown_1 = pygame.image.load("assets/images/images/number_1.png")

# Star assets
one_star = pygame.image.load("assets/images/images/one_star.png")
two_stars = pygame.image.load("assets/images/images/two_stars.png")
three_stars = pygame.image.load("assets/images/images/three_stars.png")

# Save file
gold_save_data = "gold_data.txt"
