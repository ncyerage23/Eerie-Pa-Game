'''
File for constants and stuff for Eerie PA
'''

import pygame
from pygame.locals import *

pygame.display.init()
pygame.font.init()


#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Window Stuff
WIN_WIDTH = 1000
WIN_HEIGHT = 750
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)

FPS = 60

#GW stuff
GW_WIDTH = WIN_WIDTH - 50
GW_HEIGHT = WIN_HEIGHT - 50
GW_SIZE = (GW_WIDTH, GW_HEIGHT)

#Keys stuff
PLAYER_SPEED = 3
MOVEMENT_KEYS = {K_w: (0,PLAYER_SPEED), K_s: (0,-PLAYER_SPEED), K_a: (-PLAYER_SPEED,0), K_d: (PLAYER_SPEED,0)}

#tile stuff
TILE_SIZE = 50