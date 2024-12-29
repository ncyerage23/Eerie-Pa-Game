'''
Level object for Eerie PA
'''

from setup import *


class Level:
    def __init__(self, level_name, display_surface, player):
        self.display_surface = display_surface
        self.level_name = level_name
        self.player = player

        self.visibles = None
        self.obstacles = pygame.sprite.Group()

        self.get_map()
    
    def get_map(self):
        pass





