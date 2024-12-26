'''
Player for Eerie, PA
'''

from setup import *

class Player(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        super(Player, self).__init__()
        self.surf = pygame.Surface( (50,50) )
        self.rect = self.surf.get_rect()
        self.rect.center = (GW_WIDTH // 2, GW_HEIGHT // 2)

        self.x, self.y = startX, startY
    
    def update(self):
        self.surf.fill(RED)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
