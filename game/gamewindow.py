'''
File for gamewindow actions for Eerie, PA
'''

from setup import *
from display import Display
from player import Player
from map import Map

class GameWindow(pygame.Surface):
    def __init__(self):
        super().__init__(WIN_SIZE)
        self.fill(BLACK)
        self.rect = self.get_rect()

        #display stuff
        self.display = Display()

        #map stuff
        self.map = Map()

        #player stuff
        self.player = Player(0,0)


    def update(self, keys):
        for key in MOVEMENT_KEYS:
            if keys[key]:
                delta = MOVEMENT_KEYS[key]
                print(delta)
            
        self.map.update()
        self.player.update()
        self.display.update(self.level, (self.player.x, self.player.y))


    def draw(self, screen):
        self.fill(BLACK)

        w,h = screen.get_size()
        self.rect.center = (w//2, h//2)

        #first draw map
        self.map.draw(self)

        #then objects

        #then characters
        self.player.draw(self)

        #then display
        self.display.draw(self)


        screen.blit(self, self.rect)