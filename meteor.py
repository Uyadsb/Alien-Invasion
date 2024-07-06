import pygame
from pygame.sprite import Sprite
from random import randint

class Meteor(Sprite):
    
    def __init__(self, game):
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load("images/meteor.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.y = randint(-200 , 0 )
        self.rect.x = randint(20, self.settings.screen_width - 20 )
        
         # make rect float
        self.y = float(self.rect.y )
    
    # check if meteor reached the bottom
    def check_bottom(self):
        if self.rect.bottom == self.screen_rect.bottom + 200:
            return True
    
    
    # meteor movement
    def update(self):
        self.y += self.settings.meteor_speed
        self.rect.y = self.y