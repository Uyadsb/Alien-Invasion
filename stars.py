import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect() 
        
        #load image of star
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        
        # initialize pos of alien near the topleft
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
