class settings:
    #to store all settings for the game 

    def __init__(self) :
        ''' initialize the game sttings '''
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        
        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2
        
        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 245, 90) 
        self.bullets_allowed = 3
        
        # aliens settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # meteor settings
        self.meteor_speed = 0.5
        
        # game speeds up
        self.speedup_scale = 1.1
        
        # increase alien points hit
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    # initial game settings
    def initialize_dynamic_settings(self):
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.ship_speed = 1.5
        self.meteor_speed = 0.5
        
        # scoring
        self.alien_points = 5.0
        
        # direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.meteor_speed *= self.speedup_scale
        self.alien_points *= self.score_scale