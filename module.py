import pygame

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_image(image, scale, surface, x, y):
    imagerect = image.get_rect()
    imagescaled = pygame.transform.scale(image, (imagerect.right * scale, imagerect.bottom * scale))
    imagerect.x, imagerect.y = image.get_width(), image.get_height()
    surface.blit(imagescaled, imagescaled.get_rect(center = (x,y)))

