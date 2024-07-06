import pygame

class Sound:
    def __init__(self):
        self.levelup = pygame.mixer.Sound("sounds/level_up.wav")
        self.bullet_shoot = pygame.mixer.Sound("sounds/bullet_shoot.wav")
        self.big_explosion = pygame.mixer.Sound("sounds/big_explosion.wav")
        self.small_explosion = pygame.mixer.Sound("sounds/small_explosion.wav")
        self.Explosion_meteor = pygame.mixer.Sound("sounds/Explosion_meteor.wav")