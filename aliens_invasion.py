import sys
from time import sleep

import pygame

from settings import settings
from ship import ship
from bullet import Bullet
from aliens import Alien
from stars import Star
from game_stats import GameStats
from button import Button
from score import Score
from meteor import Meteor
from sounds import Sound

from random import randint


#class to manage assets and behavior 
class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.settings = settings()
        ''' # if you  want to make screen with your own size just make the three lines later comment and rewrite this line, go to settings.py and modify it ! 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        '''
        self.screen = pygame.display.set_mode( (0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width 
        
        self.stats = GameStats(self)
        self.score = Score(self)
        self.sound = Sound()
        
        self.stars = pygame.sprite.Group()
        self._create_stars()
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group() 
        self.meteors = pygame.sprite.Group()
        self
        self._create_fleet()
        self._create_meteor()
        
        # play buttin
        self.play_button = Button(self, "Play")
        
        pygame.display.set_caption("Alien Invasion")
        
        #background color 
        ''' use the RGB rule to fix colors
       (255,0,0) is red , (0,255,0) is green, (0,0,255) is blue 
        modify it to create a default color '''
        
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active :
                self.ship.update() 
                self._update_bullets()
                self._update_aliens()
                self._update_meteor()
                
            self._update_screen()
    
    def _update_meteor(self):
        self.meteors.update()
        for meteor in self.meteors.sprites():
            if meteor.check_bottom():
                self.meteors.empty()
                self._create_meteor()
                break
        # meteor and ship collision
        if pygame.sprite.spritecollideany(self.ship, self.meteors):
            self.sound.Explosion_meteor.play()
            self._ship_hits()
 
    
    def _create_meteor(self):
        for i in range(randint(1,4)):
            meteor = Meteor(self)
            self.meteors.add(meteor)
    
    def _check_bottom(self):
        screen_rect = self.screen.get_rect()
        # check if any alien reached the bottom
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hits()
                break
    
    def _ship_hits(self):
        if self.stats.ships_left > 0:
            # eleminate one of ships left
            self.stats.ships_left -= 1
            self.score.prep_ships()
        
            # Rid any bullets and aliens 
            self.aliens.empty()
            self.bullets.empty()
            self.meteors.empty()
            
        
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            self._create_meteor()
            
            # pause
            sleep(0.75)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            
    def _update_aliens(self):
        # Check if the fleet is at an edge
        self._check_fleet_edges()
        # Update the positions of all aliens in the fleet
        self.aliens.update()
        # aliens and ship collision
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.sound.big_explosion.play()
            self._ship_hits()
        # check if any alien reached the bottom
        self._check_bottom()
    
    # Respond appropriately if any aliens have reached an edge.
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def  _change_fleet_direction(self):
        # Drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        # Spacing and number stars 
        available_space_x = self.settings.screen_width - (2 * star_width)
        available_number = available_space_x // (2 * star_width)
        number_stars = available_number // 2
        
        # spacing and number rows
        available_space_y = self.settings.screen_height - (2 * star_height)
        available_rows = available_space_y // (2 * star_height)
        number_rows = available_rows // 2
        
        # create stars of galaxy
        for row_number in range(number_rows):
            for star_number in range(number_stars):
                self._create_star(star_number, row_number)
    
    def _create_star(self,star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + randint(10,20) * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + randint(10,15) * star_height * row_number
        self.stars.add(star)
        
    def _create_fleet(self):
        # create an alien and find the number of aliens in a row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Spacing between each alien is equal to one alien width.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # number of rows 
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - (ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full rows of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self,alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
              
    def _update_bullets(self):
        self.bullets.update() 
        # rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet) 
        
        # check collisions and update fleet
        self._collision_bullets_aliens()      
        
    def _collision_bullets_aliens(self):
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            self.sound.small_explosion.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score.prep_score()
            self.score.check_high_score()

             
        # destroy existing bullets and create a new fleet
        if not self.aliens : 
            self.bullets.empty()
            self.meteors.empty()
            self._create_fleet() 
            self._create_meteor()
            self.settings.increase_speed()
            
            # increase level
            self.stats.level += 1
            self.sound.levelup.play()
            self.score.prep_level()
                                      
    def _check_events(self):
        #watch the keyboard and mouse function
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._event_KEYDOWN(event)       
                elif event.type == pygame.KEYUP:
                    self._event_KEYUP(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self._check_button_mouse_pos(mouse_pos) :
                        self._check_play_button()
                                            
    
    def _check_button_mouse_pos(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            return True
    
    # start new game when click on play button
    def _check_play_button(self):
        if not self.stats.game_active:
            # reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.score.prep_score()
            self.score.prep_level()
            self.score.prep_ships()

            # rid the aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            self.meteors.empty()
            
            
            # create a new fleet and center the ship and
            self._create_fleet()
            self.ship.center_ship()
            self._create_meteor()
            
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            
            
    # fire 
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sound.bullet_shoot.play()
        
    # check event function
    # keypresses
    def _event_KEYDOWN(self,event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
            self.ship.moving_left = True              
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE or event.key == pygame.K_p:
            self._fire_bullet()
        elif event.key == pygame.K_UP or event.key == pygame.K_z:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_RETURN:
            self._check_play_button()
            

    # key releases
    def _event_KEYUP(self,event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
            self.ship.moving_right = False    
        if event.key == pygame.K_LEFT or event.key == pygame.K_q :
            self.ship.moving_left = False
        if event.key == pygame.K_UP or event.key == pygame.K_z:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False
    
    #redraw the background each loop
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        # Draw the score information.
        self.score.show_score()
        
        # draw meteor 
        self.meteors.draw(self.screen)
        
        # draw play button in inactive game state
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        #to move screen into next image
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()