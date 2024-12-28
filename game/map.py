'''
Object for maps
'''

from setup import *
import os

class Map:
    def __init__(self, name, start_coords):
        self.name = name
        image_path = f"../images/maps/{name}.png"
        self.surf = pygame.image.load(image_path)
        self.rect = self.surf.get_rect()

        self.update(start_coords)

    def update(self, coords):
        pass


    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        