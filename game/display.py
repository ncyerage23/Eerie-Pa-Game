'''
Display file for testing
'''

from setup import *

class Display(pygame.Surface):
    def __init__(self):
        super().__init__( (300, 100), pygame.SRCALPHA )
        self.rect = self.get_rect()
        self.rect.left = 5
        self.rect.top = 5
        self.font = pygame.font.Font(None, 25)

    #the "geometry management" can be way improved here, but not a huge deal
    def update(self, level, player_coords):
        self.fill((0, 0, 0, 0))
        box_list = []

        lvl_lbl = self.font.render(f'Level: {level}', True, WHITE)
        lvl_rect = lvl_lbl.get_rect()
        box_list.append((lvl_lbl, lvl_rect))

        x_lbl = self.font.render(f'X: {player_coords[0]}', True, WHITE)
        x_rect = x_lbl.get_rect()
        box_list.append((x_lbl, x_rect))

        y_lbl = self.font.render(f'Y: {player_coords[1]}', True, WHITE)
        y_rect = y_lbl.get_rect()
        box_list.append((y_lbl, y_rect))

        top, left = 5, 5
        for box in box_list:
            lbl = box[0]
            rect = box[1]
            rect.top = top
            rect.left = left
            self.blit(lbl, rect)

            top = top + rect.height + 5

        self.rect.height = top + 10


    def draw(self, screen):
        screen.blit(self, self.rect)