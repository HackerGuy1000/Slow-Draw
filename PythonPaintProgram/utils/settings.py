import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
ORANGE = (255,128,0)
YELLOW = (207,163,0)
PURPLE = (127,0,255)
BROWN = (102,51,0)

FPS = 240

WIDTH, HEIGHT = 700, 800    

ROWS = COLS = 75

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = False


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
