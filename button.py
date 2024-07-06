import pygame.font 

class Button:
    def __init__(self,game,msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set dimension of the buttom
        self.width, self.height = 250,75
        self.button_color = (15,255,7)
        self.msg_color = (255,255,255)
        self.font = pygame.font.SysFont(None,60)
        
        # build the button's rect object and center it 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # button msg prepped only once
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.mgs_image = self.font.render(msg, True, self.msg_color, self.button_color)
        self.msg_image_rect = self.mgs_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button (self):
        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.mgs_image, self.msg_image_rect)