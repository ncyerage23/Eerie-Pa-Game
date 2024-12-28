'''
Player for Eerie, PA
'''

from setup import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.surf = pygame.Surface( (50,50) )
        self.surf.fill(RED)
        self.rect = self.surf.get_rect( topleft = pos )
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[K_d]:
            self.direction.x += 1
        
        if keys[K_a]:
            self.direction.x -= 1

        if keys[K_w]:
            self.direction.y -= 1
        
        if keys[K_s]:
            self.direction.y += 1

        if not( keys[K_a] or keys[K_d] ):
            self.direction.x = 0
        
        if not( keys[K_w] or keys[K_s] ):
            self.direction.y = 0


    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * 1
		#self.collision('horizontal')
        self.hitbox.y += self.direction.y * 1
		#self.collision('vertical')
        self.rect.center = self.hitbox.center
        

    def update(self):
        self.get_input()
        self.move()

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
