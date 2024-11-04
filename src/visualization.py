import pygame, random

pygame.init()


WINDOW_SIZE = 800

WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) # Creates window and takes in dimensions as a tuple

pygame.display.set_caption('Sorting Algorithm Visualizer')

# Variables
RECT_WIDTH = 20
clock =pygame.time.Clock()
FPS = 160
RECT_BORDER_SPACING = 1
GREEN = (36, 204, 68)
CHARCOAL = (54, 69, 79) #Charcoal
BLACK = (0, 0, 0) #black
RUSTY_RED = (220, 52, 59) #Rusty Red
GREY = (85, 85, 85) # Grey
LIGHT_BLUE = (159, 226, 191) #Aqua Blue

# Rectangles are going to be objects of the rectangle class
class Rectangle:
    def __init__(self, color, x, height) -> None: # init self method defined.
        self.color = color
        self.x = x
        self.width = RECT_WIDTH
        self.height = height
   
    # Other methods created to change color of rectangles depending on use. Ex: sorted, selected, unselected, etc.
    def select(self):
        self.color = LIGHT_BLUE
 
    def unselect(self):
        self.color = BLACK
   
    def set_smallest(self):
        self.color = RUSTY_RED
   
    def set_sorted(self):
        self.color = GREEN

def create_rectangles(): # Function that creates the rectangles
    num_rectangles = WINDOW_SIZE // RECT_WIDTH - RECT_BORDER_SPACING # -1 is for leaving some space between window
    rectangles = [] # Empty list of all rectangles
    heights = []  # List of all heights

    # Generates random heights
    for i in range(RECT_BORDER_SPACING, num_rectangles):
        height = random.randint(10, WINDOW_SIZE//2)
        while height in heights: # Checks if generated height is already in height list, if so then new height generated.
            height = random.randint(10, WINDOW_SIZE//2)

        heights.append(height)
        rect = Rectangle(BLACK, i*RECT_WIDTH, height) # Creates rectangle instance, named rect
        rectangles.append(rect) # Appends rectangle to rectangles list.

    return rectangles

def draw_rects(rectangles_list): # Draw rectangle function
    WINDOW.fill(GREY) # Built in function in pygame fills background window with a color
    
    for rect in rectangles_list:
        pygame.draw.rect(WINDOW, rect.color, (rect.x, (WINDOW_SIZE)-rect.height , rect.width, rect.height))
        pygame.draw.line(WINDOW, CHARCOAL, (rect.x, (WINDOW_SIZE)),(rect.x, (WINDOW_SIZE)-rect.height)) # Draws black line at left side of rectangle
        pygame.draw.line(WINDOW, CHARCOAL, (rect.x+rect.width, (WINDOW_SIZE)),(rect.x+rect.width, (WINDOW_SIZE)-rect.height))
        pygame.draw.line(WINDOW, CHARCOAL, (rect.x, (WINDOW_SIZE)-rect.height),(rect.x + rect.width, (WINDOW_SIZE)-rect.height))

def display_text(txt, y, size):
    FONT = pygame.font.SysFont('arial', size) # Loads the system font
    text = FONT.render(txt, True, GREEN) # Renders the text
    text_rect = text.get_rect(center=(WINDOW_SIZE/2, y)) # Destination where, text is going to be.
    WINDOW.blit(text, text_rect) # Blits - copies contents of text surface onto another surface at specific location 


if __name__ == '__main__':
    print('TEST')