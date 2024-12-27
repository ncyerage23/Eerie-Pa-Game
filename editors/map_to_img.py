'''
Editor file for Eerie PA
Converts map arrays to stitched together image
'''

import os
import json
import pygame
import sys

pygame.init()

GRID_SIZE = 32
CELL_SIZE = 75
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = WIDTH

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Builder")

#first get all the tiles and put it in an array
images_folder = "../images/tiles"
image_dict = {}
for f in os.listdir(images_folder):
    if f.endswith(('.png', '.jpg', '.jpeg')):
        img = pygame.image.load(os.path.join(images_folder, f)).convert_alpha()
        image_dict[ str( f[:(len(f)-4)] ) ] = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))


#now get all the maps
maps_folder = "../maps"
maps = [m for m in os.listdir(maps_folder) if m.endswith('.json')]

map_images_folder = "../images/maps"
os.makedirs(map_images_folder, exist_ok=True)

if os.path.exists(map_images_folder):
    # Iterate through all files in the folder
    for file in os.listdir(map_images_folder):
        file_path = os.path.join(map_images_folder, file)
        # Check if it's a file and remove it
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f"All files in {map_images_folder} have been deleted.")
else:
    print(f"The folder {map_images_folder} does not exist.")

#save each map as a png
for m in maps:
    map_path = os.path.join(maps_folder, m)
    with open(map_path, 'r') as map_file:
        grid_array = json.load(map_file)
        
        map_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)

        # Draw tiles onto the surface
        for row in range(len(grid_array)):
            for col in range(len(grid_array[row])):
                tile_name = grid_array[row][col]
                if tile_name is not None and tile_name in image_dict:
                    tile_image = image_dict[tile_name]
                    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    map_surface.blit(tile_image, rect)

        # Save the surface as an image file
        filename = f"{os.path.splitext(m)[0]}.png"
        save_path = os.path.join(map_images_folder, filename)

        try:
            pygame.image.save(map_surface, save_path)
            print(f"Image saved as {save_path}")
        except pygame.error as e:
            print(f"Error saving the image: {e}")
                

pygame.quit()