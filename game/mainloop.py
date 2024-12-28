'''
Mainloop for Eerie PA game
'''

from setup import *
from gamewindow import GameWindow


screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Eerie, PA')
clock = pygame.time.Clock()

screen.fill( WHITE )


gw = GameWindow()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    gw.update()

    screen.fill( WHITE )

    gw.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


