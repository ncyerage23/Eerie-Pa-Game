'''
Mainloop for Eerie PA game
'''

from setup import *


screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Eerie, PA')
clock = pygame.time.Clock()

screen.fill( BLACK )


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    


    pygame.display.flip()
    clock.tick(60)

pygame.quit()


