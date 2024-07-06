import pygame


#class to manage the ship 
class ship() :
    def __init__(self, ai_game) :
        self.screen = ai_game.screen
        self.screen_rect =  ai_game.screen.get_rect()
        #load the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings
        # Start each new ship at the bottom center of the screen. 
        self.rect.midbottom = self.screen_rect.midbottom
    
        # decimal value to speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False    
        self.moving_left = False
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        # update the x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        if self.moving_up and self.rect.top > 0 :
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom :
            self.y += self.settings.ship_speed
            
        # update rect from self.x and self.y
        self.rect.x = self.x     
        self.rect.y = self.y       
    
        