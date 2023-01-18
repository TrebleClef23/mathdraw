import pygame
from pygame.color import Color, THECOLORS

WINDOW_SIZE = (640, 480)
GRAPHS_SIZE = (640, 400)
GRAPHS_RECT = pygame.rect.Rect((0, 0), GRAPHS_SIZE)

CONTROLLER_RADIUS: int = 4
PRESSED_WIDTH: int = 1
LINE_WIDTH: int = 2

COLOR: Color = Color(THECOLORS['black'])
BACKGROUND: Color = Color(THECOLORS['white'])
PRESSED_COLOR: Color = Color(THECOLORS['blue'])
