'''
Tile painter for Eerie PA
'''

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 32
CELL_SIZE = 20
BUTTON_HEIGHT = 50

# Screen dimensions
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE + BUTTON_HEIGHT

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tile Painter")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
current_color = (255, 255, 255, 255)  # Default to white
transparent_color = (0, 0, 0, 0)  # Transparent
grid = [[transparent_color for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
eraser_mode = False

# Font
font = pygame.font.Font(None, 36)

# Buttons
buttons = {
    "save": pygame.Rect(0, GRID_SIZE * CELL_SIZE, 100, BUTTON_HEIGHT),
    "color": pygame.Rect(100, GRID_SIZE * CELL_SIZE, 100, BUTTON_HEIGHT),
    "eraser": pygame.Rect(200, GRID_SIZE * CELL_SIZE, 100, BUTTON_HEIGHT),
    "fill_all": pygame.Rect(300, GRID_SIZE * CELL_SIZE, 100, BUTTON_HEIGHT),
    "open": pygame.Rect(400, GRID_SIZE * CELL_SIZE, 100, BUTTON_HEIGHT),
}

# Indicator position
color_indicator_rect = pygame.Rect(420, GRID_SIZE * CELL_SIZE + 10, 30, 30)
color_indicator_rect.left = 550


def draw_grid():
    """Draw the grid and painted cells with smaller grid lines."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = grid[row][col]
            if color == transparent_color:
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Border only (thin lines)
            else:
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Border


def draw_buttons():
    """Draw the buttons."""
    pygame.draw.rect(screen, (0, 200, 0), buttons["save"])
    screen.blit(font.render("Save", True, (255, 255, 255)), (10, GRID_SIZE * CELL_SIZE + 10))
    
    pygame.draw.rect(screen, (0, 0, 200), buttons["color"])
    screen.blit(font.render("Color", True, (255, 255, 255)), (110, GRID_SIZE * CELL_SIZE + 10))
    
    pygame.draw.rect(screen, (200, 0, 0), buttons["eraser"])
    screen.blit(font.render("Eraser", True, (255, 255, 255)), (210, GRID_SIZE * CELL_SIZE + 10))
    
    pygame.draw.rect(screen, (200, 200, 0), buttons["fill_all"])
    screen.blit(font.render("Fill All", True, (255, 255, 255)), (310, GRID_SIZE * CELL_SIZE + 10))

    pygame.draw.rect(screen, (100, 100, 200), buttons["open"])
    screen.blit(font.render("Open", True, (255, 255, 255)), (410, GRID_SIZE * CELL_SIZE + 10))


def draw_color_indicator():
    """Draw the current color indicator."""
    if eraser_mode:
        # Display "Transparent" text when eraser is active
        pygame.draw.rect(screen, (200,200,200), color_indicator_rect, 1)  # Border
        screen.blit(font.render("T", True, (200, 200, 200)), (425, GRID_SIZE * CELL_SIZE + 10))
    else:
        pygame.draw.rect(screen, current_color, color_indicator_rect)  # Filled with current color
        pygame.draw.rect(screen, (200, 200, 200), color_indicator_rect, 1)  # Border


def save_image():
    """Save the grid as an image file in the '../images' folder."""
    images_folder = "../images/tiles"
    filename = input("Enter a filename (without extension): ") + ".png"
    save_path = f"{images_folder}/{filename}"

    # Save image
    image_surface = pygame.Surface((WIDTH, GRID_SIZE * CELL_SIZE), pygame.SRCALPHA, 32)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(image_surface, grid[row][col], rect)
    
    try:
        pygame.image.save(image_surface, save_path)
        print(f"Image saved as {save_path}")
    except pygame.error:
        print("Error saving the image.")


def load_image():
    """Load an image from the '../images' folder into the grid."""
    images_folder = "../images/tiles"
    filename = input("Enter the filename to load (without extension): ") + ".png"
    load_path = f"{images_folder}/{filename}"

    try:
        image = pygame.image.load(load_path).convert_alpha()  # Ensure alpha transparency is handled
        image = pygame.transform.scale(image, (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))  # Resize to fit grid
        image_data = pygame.surfarray.array3d(image)  # Convert to 3D array (RGB)

        # Load image data into the grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                # Get the RGB values and ensure we preserve transparency
                r, g, b = image_data[col * CELL_SIZE, row * CELL_SIZE]  # Note: array3d gives (col, row) indexing
                grid[row][col] = (r, g, b, 255)  # Set the color in the grid (opaque)
        
        print(f"Image '{filename}' loaded successfully.")
    except pygame.error:
        print(f"File '{filename}' not found in {images_folder}.")



def choose_color():
    """Prompt the user to input an RGB color."""
    global current_color, eraser_mode
    eraser_mode = False
    try:
        r = int(input("Enter red value (0-255): "))
        g = int(input("Enter green value (0-255): "))
        b = int(input("Enter blue value (0-255): "))
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            current_color = (r, g, b, 255)
            print(f"Color inputted: ({r}, {g}, {b})\n")
        else:
            print("Invalid RGB values. Please enter numbers between 0 and 255.")
    except ValueError:
        print("Invalid input. Please enter integers for RGB values.")


def fill_all():
    """Fill the entire grid with the current color."""
    global grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid[row][col] = current_color if not eraser_mode else transparent_color


def paint_cell(pos):
    """Paint the cell at the given position."""
    x, y = pos
    if y < GRID_SIZE * CELL_SIZE:  # Prevent painting outside the grid area
        row, col = y // CELL_SIZE, x // CELL_SIZE
        if eraser_mode:
            grid[row][col] = transparent_color
        else:
            grid[row][col] = current_color


# Main loop
running = True
painting = False
while running:
    screen.fill((255, 255, 255))
    
    draw_grid()
    draw_buttons()
    draw_color_indicator()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["save"].collidepoint(event.pos):
                save_image()
            elif buttons["color"].collidepoint(event.pos):
                choose_color()
            elif buttons["eraser"].collidepoint(event.pos):
                eraser_mode = True
                current_color = transparent_color
            elif buttons["fill_all"].collidepoint(event.pos):
                fill_all()
            elif buttons["open"].collidepoint(event.pos):
                load_image()
            else:
                painting = True
                paint_cell(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            painting = False
        elif event.type == pygame.MOUSEMOTION and painting:
            # Only paint if the mouse is inside the grid
            if 0 <= event.pos[0] < WIDTH and 0 <= event.pos[1] < GRID_SIZE * CELL_SIZE:
                paint_cell(event.pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
