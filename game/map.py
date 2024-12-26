'''
Object for maps
'''

from setup import *

#should the map be an array of tiles? idek

class Map(pygame.Surface):
    def __init__(self, width, height):
        super().__init__( (width * TILE_SIZE, height * TILE_SIZE) )

        #fill up map (idk really)