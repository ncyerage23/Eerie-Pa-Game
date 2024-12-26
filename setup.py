'''
File for constants and stuff for Eerie PA
'''

import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_p,
    K_SPACE,
    K_w,
    K_a,
    K_s,
    K_d
)

pygame.display.init()
pygame.font.init()


#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Window Stuff
WIN_SIZE = (1000, 750)