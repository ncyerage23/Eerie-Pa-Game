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
        self.map = Map('outside_test')

        #player stuff
        self.player = Player(0,0)


    def update(self):
        keys = pygame.key.get_pressed()
        speed = 75

        self.map.set_velocity(
            x=(keys[pygame.K_a] - keys[pygame.K_d]) * speed,
            y=(keys[pygame.K_w] - keys[pygame.K_s]) * speed,
        )
        
        self.map.update( .06 )
        self.player.update( ((keys[pygame.K_d] - keys[pygame.K_a]) * speed, (keys[pygame.K_s] - keys[pygame.K_w]) * speed) )
        self.display.update(self.map.name, (self.player.x, self.player.y))


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