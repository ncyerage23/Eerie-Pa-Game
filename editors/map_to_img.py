'''
Editor file for Eerie PA
Converts map arrays to stitched together image

Screw chatgpt, just do this yourself. It's easy, lol
'''

import os
import json
from PIL import Image

def create_image_from_map(map_filename, tiles_folder, output_folder):
    # Load the map JSON file
    try:
        with open(map_filename, 'r') as f:
            map_data = json.load(f)
    except Exception as e:
        print(f"Error loading map file {map_filename}: {e}")
        return

    # Check if the map is empty
    if not map_data:
        print(f"No data found in {map_filename}")
        return

    try:
        # Assuming all tiles are the same size, get the size of the first tile
        first_tile = map_data[0][0] + '.png'  # Ensure the .png extension
        tile_width, tile_height = Image.open(os.path.join(tiles_folder, first_tile)).size
    except Exception as e:
        print(f"Error loading first tile {first_tile} for {map_filename}: {e}")
        return

    # Create a new image with appropriate size
    map_width = len(map_data[0]) * tile_width
    map_height = len(map_data) * tile_height
    output_image = Image.new('RGBA', (map_width, map_height), (255, 255, 255, 0))  # Transparent background

    # Place tiles in the correct positions
    for row_index, row in enumerate(map_data):
        for col_index, tile_name in enumerate(row):
            if tile_name:
                tile_filename = tile_name + '.png'  # Ensure the .png extension

                tile_path = os.path.join(tiles_folder, tile_filename)
                if os.path.exists(tile_path):
                    try:
                        tile_image = Image.open(tile_path)
                        x = col_index * tile_width
                        y = row_index * tile_height
                        output_image.paste(tile_image, (x, y))
                    except Exception as e:
                        print(f"Error pasting tile {tile_filename} at ({x}, {y}) for {map_filename}: {e}")
                else:
                    print(f"Tile {tile_filename} not found in {tiles_folder}")

    # Save the output image
    output_image_filename = os.path.join(output_folder, os.path.basename(map_filename).replace('.json', '.png'))
    try:
        output_image.save(output_image_filename)
        print(f"Created image: {output_image_filename}")
    except Exception as e:
        print(f"Error saving output image {output_image_filename}: {e}")

def process_maps(maps_folder, tiles_folder, output_folder):
    # Process each JSON map file in the maps folder
    for map_filename in os.listdir(maps_folder):
        if map_filename.endswith('.json'):
            map_filepath = os.path.join(maps_folder, map_filename)
            create_image_from_map(map_filepath, tiles_folder, output_folder)

if __name__ == '__main__':
    maps_folder = '../maps'
    tiles_folder = '../images/tiles'
    output_folder = '../images/maps'

    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    process_maps(maps_folder, tiles_folder, output_folder)
