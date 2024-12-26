'''
Setup file for Eerie, PA
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

import random
import math

pygame.display.init()
pygame.font.init()

MOVEMENT_KEYS = [K_w, K_a, K_s, K_d]
MOVEMENTS = {
    K_d: (1, 0),
    K_a: (-1, 0),
    K_s: (0, -1), 
    K_w: (0, 1)
}