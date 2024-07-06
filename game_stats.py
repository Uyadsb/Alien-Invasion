class GameStats:
    # track statistics for Alien Invasion
    
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        # start the game with inactive state
        self.game_active = False
        
        # high score 
        self.high_score = 0
        
    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        
        # set score and level to 0
        self.score = 0
        self.level = 0
        
        