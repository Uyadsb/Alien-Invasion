import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' Class represent a alien from the fleet '''
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        # load the source image of alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # initialize pos of alien near the topleft
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # make rect float
        self.x = float(self.rect.x )
        
    def check_edges(self):
        # return true if it is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
            return True
 
    # make alien move 
    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x