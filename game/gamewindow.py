'''
File for gamewindow actions for Eerie, PA
'''

from setup import *
from display import Display
from player import Player
from level import Level

class GameWindow(pygame.Surface):
    def __init__(self):
        super().__init__(WIN_SIZE)
        self.fill(BLACK)
        self.rect = self.get_rect()

        #player stuff
        self.player = Player( (25,25) )

        #display stuff
        self.display = Display()

        #level stuff
        #self.current_level = Level('outside_test', self, self.player)


    def update(self):
        self.player.update()
        self.display.update('hi', (0, 0))


    def draw(self, screen):
        self.fill(BLACK)

        w,h = screen.get_size()
        self.rect.center = (w//2, h//2)

        #first draw map

        #then objects

        #then characters
        self.player.draw(self)

        #then display
        self.display.draw(self)

        screen.blit(self, self.rect)