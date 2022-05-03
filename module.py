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

def gradient_rect(window, top_colour, bottom_colour, target_rect):
    # Draw a vertical-gradient filled rectangle covering <target_rect> 
    colour_rect = pygame.Surface((2, 2))                                  
    pygame.draw.line(colour_rect, top_colour, (0, 0), (1, 0))            
    pygame.draw.line(colour_rect, bottom_colour, (0, 1), (1, 1))            
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height)) 
    window.blit(colour_rect, target_rect)
