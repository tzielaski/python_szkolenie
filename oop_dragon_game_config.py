import pygame
from enum import Enum

SCREEN_MIN_X = 0
SCREEN_MAX_X = 1024
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 768
BACKGROUND_SIZE_X = 470
BACKGROUND_SIZE_Y = 403


class Color(Enum):
    # RGB
    BLACK = 000000
    WHITE = 255, 255, 255
