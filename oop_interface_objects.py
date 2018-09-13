import pygame
from dataclasses import dataclass

from pygame import font

from oop_dragon_game_config import Color


@dataclass
class InfoRectangle:
    DEFAULT_SIZE_X = 100
    DEFAULT_SIZE_Y = 50
    info: str = ''
    size = DEFAULT_SIZE_X, DEFAULT_SIZE_Y
    position: (int, int) = (0, 0)

    def draw(self, surface: pygame.Surface):
        rect = (
            self.get_x(),
            self.get_y(),
            self.get_size_x(),
            self.get_size_y()
        )
        info_font = font.SysFont(font.get_default_font(), 32)
        text_img = info_font.render(self.info, True, Color.WHITE.value)
        surface.blit(text_img, self.position)

    def get_position(self):
        return self.position

    def get_x(self):
        return self.position[0]

    def get_y(self):
        return self.position[1]

    def get_size_x(self):
        return self.size[0]

    def get_size_y(self):
        return self.size[1]

    def set_text(self, text):
        self.info = text
