from enum import Enum

SCREEN_MIN_X = 0
SCREEN_MAX_X = 1024
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 768
BACKGROUND_SIZE_X = 470
BACKGROUND_SIZE_Y = 403
FONT_SIZE = 16


class Color(Enum):
    # RGB
    BLACK = 000000
    WHITE = 255, 255, 255
    GOLD = 255, 215, 0


class Status(Enum):
    ALIVE = 1
    DEAD = 0
    ATTACK = 2
    MOVE = 3