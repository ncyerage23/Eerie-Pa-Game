'''
Map builder for Eerie PA

still needs to be able to change size of the map
'''

import pygame
import sys
import os
import json  # To save and open grid data as JSON files

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 32
CELL_SIZE = 20
BUTTON_HEIGHT = 50
PICKER_HEIGHT = 50

# Screen dimensions
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE + BUTTON_HEIGHT + PICKER_HEIGHT

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Builder")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Load images from the '../images' folder
images_folder = "../images/tiles"
image_files = [f for f in os.listdir(images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
images = [pygame.image.load(os.path.join(images_folder, img)).convert_alpha() for img in image_files]
scaled_images = [pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE)) for img in images]

# Create a dictionary of image names corresponding to the images
image_names = {img_file: img_file.split('.')[0] for img_file in image_files}

# Grid initialization (empty grid)
grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_image = None
current_image_name = None

# Font
font = pygame.font.Font(None, 36)

# Buttons
buttons = {
    "save": pygame.Rect(0, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT , 100, BUTTON_HEIGHT),
    "clear": pygame.Rect(100, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT , 100, BUTTON_HEIGHT),
    "open": pygame.Rect(200, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT , 100, BUTTON_HEIGHT),
    "fill_all": pygame.Rect(300, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT , 100, BUTTON_HEIGHT)  # New button
}

# Draw the grid and images
def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # If there's an image in the grid cell, draw it
            if grid[row][col] is not None:
                screen.blit(grid[row][col][0], rect)

# Draw the buttons
def draw_buttons():
    pygame.draw.rect(screen, (0, 200, 0), buttons["save"])
    screen.blit(font.render("Save", True, (255, 255, 255)), (10, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT + 10))

    pygame.draw.rect(screen, (200, 0, 0), buttons["clear"])
    screen.blit(font.render("Clear", True, (255, 255, 255)), (110, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT + 10))

    pygame.draw.rect(screen, (100, 100, 200), buttons["open"])
    screen.blit(font.render("Open", True, (255, 255, 255)), (210, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT  + 10))
    
    # New "Fill All" button
    pygame.draw.rect(screen, (200, 200, 0), buttons["fill_all"])
    screen.blit(font.render("Fill All", True, (255, 255, 255)), (310, HEIGHT - BUTTON_HEIGHT - PICKER_HEIGHT + 10))

# Paint the selected image into the grid cell
def paint_cell(pos):
    x, y = pos
    if y < GRID_SIZE * CELL_SIZE:
        row, col = y // CELL_SIZE, x // CELL_SIZE
        if current_image_name is not None:  # Use the image name, not the image object
            grid[row][col] = current_image, current_image_name

# Save the grid as an array of image names
def save_image_as_array():
    """Save the grid as an array of image names."""
    filename = input("Enter a filename (without extension): ") + ".json"
    
    # Set the directory to save the file in "../maps"
    maps_folder = "../maps"
    if not os.path.exists(maps_folder):
        os.makedirs(maps_folder)  # Create the maps folder if it doesn't exist
    save_path = os.path.join(maps_folder, filename)

    # Create a 2D array of image names based on the grid
    grid_array = []
    for row in range(GRID_SIZE):
        grid_row = []
        for col in range(GRID_SIZE):
            image = grid[row][col]  # Get the image name directly
            grid_row.append(image[1])
        grid_array.append(grid_row)

    # Save the grid array as a JSON file
    try:
        with open(save_path, 'w') as f:
            json.dump(grid_array, f)
        print(f"Grid saved as {save_path}")
    except IOError:
        print("Error saving the grid array.")

# Clear the grid
def clear_grid():
    global grid
    grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Load image from the list
def load_image_from_list(index):
    global current_image, current_image_name
    current_image = scaled_images[index]
    current_image_name = image_files[index].split('.')[0]  # Store the image name (without extension)

# Load the grid from a JSON file
def load_grid_from_file(filename):
    """Load the grid from a JSON file in the ../maps directory."""
    maps_folder = "../maps"
    load_path = os.path.join(maps_folder, filename)

    try:
        with open(load_path, 'r') as f:
            grid_array = json.load(f)

        # Reconstruct the grid using image names
        global grid
        grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                image_name = grid_array[row][col]
                if image_name:
                    image_path = os.path.join(images_folder, f"{image_name}.png")
                    if os.path.exists(image_path):
                        img = pygame.image.load(image_path).convert_alpha()
                        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
                        grid[row][col] = img, image_name
        print(f"Grid loaded from {load_path}")
    except (IOError, json.JSONDecodeError):
        print("Error loading the grid from the file.")

# Fill the entire grid with the selected image
def fill_all_spots():
    if current_image is not None:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                grid[row][col] = current_image, current_image_name

# Main loop
running = True
painting = False
while running:
    screen.fill((255, 255, 255))

    draw_grid()
    draw_buttons()

    # Display image options for selection (in a row at the bottom)
    tile_buttons_y = HEIGHT - CELL_SIZE - 5
    for i, img in enumerate(scaled_images):
        x_offset = i * (CELL_SIZE + 5)
        screen.blit(img, (x_offset, tile_buttons_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["save"].collidepoint(event.pos):
                save_image_as_array()  # Save the grid as an array of image names
            elif buttons["clear"].collidepoint(event.pos):
                clear_grid()
            elif buttons["open"].collidepoint(event.pos):
                filename = input("Enter the filename to open (without .json extension): ") + ".json"
                load_grid_from_file(filename)  # Open the grid from a JSON file
            elif buttons["fill_all"].collidepoint(event.pos):
                fill_all_spots()  # Fill the grid with the selected image
            elif event.pos[1] > tile_buttons_y:  # Check if the click is in the tile selection area
                selected_index = event.pos[0] // (CELL_SIZE + 5)
                if selected_index < len(scaled_images):
                    load_image_from_list(selected_index)
            else:
                painting = True
                paint_cell(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            painting = False
        elif event.type == pygame.MOUSEMOTION and painting:
            paint_cell(event.pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
