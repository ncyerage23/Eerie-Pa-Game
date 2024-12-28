'''
Object for maps
'''

from setup import *
import os

class Map:
    def __init__(self, name):
        self.name = name
        image_path = f"../images/maps/{name}.png"
        self.surf = pygame.image.load(image_path)
        self.rect = self.surf.get_rect()
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        """Update the map's position based on velocity and time delta."""
        self.rect.move_ip(self.velocity * dt)

    def set_velocity(self, x, y):
        """Set the velocity of the map."""
        self.velocity = pygame.Vector2(x, y)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        