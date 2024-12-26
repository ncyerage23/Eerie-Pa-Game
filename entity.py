'''
Objects for entities (characters, animals, usable objects) 
'''

from setup import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Entity, self).__init__()

        self.surf = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()

        
    def set_coord(self, coord):
        self.rect.center = coord
    

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


class Test(Entity):
    def __init__(self, coords):
        super().__init__(50, 50)
        self.coords = coords

    def update(self, player_location):
        self.surf.fill((0,255,0))
        self.rect.centerx = 500 + (self.coords[0] - player_location[0])
        self.rect.centery = 325 + (self.coords[1] - player_location[1])


class Player(Entity):
    def __init__(self):
        super().__init__(50, 50)
        self.color = (255,255,255)
        self.surf.fill(self.color)
        self.coords = (0,0)

    def get_loc(self):
        return self.coords

    def set_loc(self, coord):
        self.coords = coord

    def update(self, keys_pressed):
        self.surf.fill(self.color)
        self.set_coord( (500, 325) )
        
        for key in MOVEMENT_KEYS:
            if keys_pressed[key]:
                x, y = self.get_loc()
                x = x + MOVEMENTS[key][0]
                y = y + MOVEMENTS[key][1]
                self.set_loc((x, y))


