'''
File for gamewindow actions for Eerie, PA
'''

from setup import *
from display import Display

class GameWindow(pygame.Surface):
    def __init__(self):
        super().__init__(WIN_SIZE)
        self.fill(BLACK)
        self.rect = self.get_rect()

        #display stuff
        self.display = Display()

        #player stuff
        self.player = None

    def update(self):
        self.display.update()


    def draw(self, screen):
        w,h = screen.get_size()
        self.rect.center = (w//2, h//2)

        #first draw environment
        #then objects
        #then characters
        #then display

        self.display.draw(self)
        screen.blit(self, self.rect)