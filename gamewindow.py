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

        #level stuff
        self.level = 'hi'


    def update(self, keys):
        for key in MOVEMENT_KEYS:
            if keys[key]:
                delta = MOVEMENT_KEYS[key]
                print(delta)

        self.display.update(self.level)


    def draw(self, screen):
        w,h = screen.get_size()
        self.rect.center = (w//2, h//2)

        #first draw environment
        #then objects
        #then characters
        #then display

        self.display.draw(self)
        screen.blit(self, self.rect)