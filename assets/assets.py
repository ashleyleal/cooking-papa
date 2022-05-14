import pygame
from button import Button

pygame.font.init()

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(133, 203, 205)
LIGHT_BLUE = pygame.Color(168, 222, 224)
LIGHT_ORANGE = pygame.Color(249, 226, 174)
ORANGE = pygame.Color(251, 199, 141)
GREEN = pygame.Color(167, 214, 118)

NEXA_FONT = pygame.font.Font("assets/fonts/Nexa-Trial-Regular.ttf", 15)
DAYDREAM_FONT = pygame.font.Font("assets/fonts/Daydream.ttf", 15)
YOSTER_FONT = pygame.font.Font("assets/fonts/yoster.ttf", 15)

placeholder_title = pygame.image.load("assets/images/titles/cookingPapaPlaceholderTitle.png")
placeholder_button = pygame.image.load("assets/images/icons/buttonPlaceholder.png")
return_arrow = pygame.image.load("assets/images/icons/return_arrow.png")
gold_icon = pygame.image.load("assets/images/icons/coin.png")
restaurant_counter = pygame.image.load("assets/images/images/restaurant_counter.png")
kitchen_grill = pygame.image.load("assets/images/images/kitchen_grill.png")

return_button = Button(25, 25, return_arrow, 0.5)