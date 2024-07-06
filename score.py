import pygame.font
from pygame.sprite import Group

from ship_score import ShipScore

# class to report scoring infos
class Score:
    def __init__(self, game):
        # initialize scoreboard 
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.ships = pygame.sprite.Group()
        
        # font settings for scoring info
        self.text_color = (220,220,220)
        self.font = pygame.font.SysFont(None, 48)
        
        # initiale score image
        self.prep_score()
        
        self.prep_high_score()
        
        # make level 
        self.prep_level()
        
        # make ships left
        self.prep_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left + 1):
            ship = ShipScore(self.game)
            ship.rect.x = 10 + 1.3 * ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship) 

    def prep_score(self):
        # turn score into rendred image 
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Display score at the topright of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 20
        
    def prep_high_score(self)    :
        # turn score into rendred image 
        high_score = round(self.stats.high_score, -1)
        score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Display score at the topright of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    # Check to see if there's a new high score.
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        # position of lavel label
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def show_score(self):
        # Draw scores, level, and ships to the screen.
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)