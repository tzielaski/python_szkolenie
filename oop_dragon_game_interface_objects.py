import pygame
from dataclasses import dataclass

from pygame import font

from oop_dragon_game_config import Color, SCREEN_MIN_X, SCREEN_MIN_Y, SCREEN_MAX_X, SCREEN_MAX_Y, FONT_SIZE


@dataclass
class InfoRectangle:
    DEFAULT_SIZE_X = 100
    DEFAULT_SIZE_Y = 50
    info: str = ''
    size = DEFAULT_SIZE_X, DEFAULT_SIZE_Y
    position_x: int = 0
    position_y: int = 0
    color: Color = Color.WHITE

    def draw(self, surface: pygame.Surface):
        all_fonts = pygame.font.get_fonts()
        info_font_name = 'comicsansms' if 'comicsansms' in all_fonts else None
        info_font = font.SysFont(info_font_name, FONT_SIZE)
        text_img = info_font.render(self.info, True, self.color.value)
        surface.blit(text_img, (self.position_x, self.position_y))

    def get_position(self):
        return self.position_x, self.position_y

    def get_x(self):
        return self.position_x

    def get_y(self):
        return self.position_y

    def get_size_x(self):
        return self.size[0]

    def get_size_y(self):
        return self.size[1]

    def set_text(self, text):
        self.info = text

    def set_position(self, x, y):
        self.position_x = x if x >= SCREEN_MIN_X else SCREEN_MIN_X
        self.position_y = y if y >= SCREEN_MIN_Y else SCREEN_MIN_Y

        self.position_x = self.position_x if self.position_x <= SCREEN_MAX_X else SCREEN_MAX_X
        self.position_y = self.position_y if self.position_y <= SCREEN_MAX_Y else SCREEN_MAX_Y
