'''
Mainloop for Eerie PA display -- 12/26/24
'''

from setup import *
import entity as en
import display as dis


screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption('Eerie, PA')
clock = pygame.time.Clock()

screen.fill( (0,0,0) )

p1 = en.Player()
d = dis.Display()
test = en.Test((200, 200))


running = True
while running:

    key = None
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    p1.update(pygame.key.get_pressed())
    d.update(p1.coords)
    test.update(p1.coords)

    screen.fill( (0,0,0) )
    d.draw(screen)
    p1.draw(screen)
    test.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


