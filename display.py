'''
File for testing displays
'''

from setup import *

class Display(pygame.Surface):
    def __init__(self):
        super().__init__( (50, 50), pygame.SRCALPHA )

        self.rect = self.get_rect()
        self.rect.center = 25, 25
        self.font = pygame.font.Font(None, 25)
    
    def update(self, player_coords):
        self.fill((255,255,255))

        x_lbl = self.font.render(f'X: {player_coords[0]}', True, (0,0,0))
        y_lbl = self.font.render(f'Y: {player_coords[1]}', True, (0,0,0))

        x_rect = x_lbl.get_rect()
        y_rect = y_lbl.get_rect()

        x_rect.left = 5
        y_rect.left = 5

        x_rect.top = 5
        y_rect.top = x_rect.top + x_rect.height + 5

        self.blit(x_lbl, x_rect)
        self.blit(y_lbl, y_rect)

    
    def draw(self, screen):
        screen.blit(self, self.rect)

