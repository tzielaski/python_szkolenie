import random

import pygame

from oop_dragon_easy import Dragon
from oop_dragon_game_config import SCREEN_MIN_X, SCREEN_MAX_X, SCREEN_MIN_Y, SCREEN_MAX_Y
from oop_dragon_game_gold import GoldGenerator
from oop_interface_objects import InfoRectangle


class SuperDragon(Dragon):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_hit_points = self.hit_points
        self.set_img(self.DRAGON_PNG)
        self.life_info = InfoRectangle(position_x=self.position_x, position_y=self.position_y)

    def move(self, left=0, right=0, down=0, up=0):
        """
        >>> drag = SuperDragon(name='test'); drag.move(right=SCREEN_MAX_X+1, down=SCREEN_MAX_Y+1);
        >>> (x,y) = drag.get_position()
        >>> (x,y) == (SCREEN_MAX_X, SCREEN_MAX_Y)
        True

        >>> drag = SuperDragon(name='test'); drag.move(left=SCREEN_MAX_X+1, right=SCREEN_MAX_Y+1);
        >>> (x,y) = drag.get_position()
        >>> (x,y) == (SCREEN_MIN_X, SCREEN_MIN_Y)
        True

        """
        if self.is_alive():
            self.set_position(
                self.position_x + right - left,
                self.position_y + down - up
            )

    def set_position(self, x, y):
        self.position_x = x if x >= SCREEN_MIN_X else SCREEN_MIN_X
        self.position_y = y if y >= SCREEN_MIN_Y else SCREEN_MIN_Y

        self.position_x = self.position_x if self.position_x <= SCREEN_MAX_X else SCREEN_MAX_X
        self.position_y = self.position_y if self.position_y <= SCREEN_MAX_Y else SCREEN_MAX_Y

    def get_img(self):
        return self.img

    def get_middle_lower(self):
        x = round(self.position_x + self.img.get_width()/2.)
        y = self.position_y + self.img.get_height()
        return x,y

    def random_move(self):
        moves = {
            'left': random.randint(0, self.MOVE_RANGE),
            'right': random.randint(0, self.MOVE_RANGE),
            'up': random.randint(0, self.MOVE_RANGE),
            'down': random.randint(0, self.MOVE_RANGE),
        }
        self.move(**moves)

    def die(self):
        super().die()
        self.set_img(self.DRAGON_DEAD_PNG)

    def draw(self, surface):
        surface.blit(self.get_img(), self.get_position())
        self.update_life_info()
        self.life_info.draw(surface)

    def update_life_info(self):
        self.life_info.set_text(f'{self.name}: {round(self.hit_points)}/{self.start_hit_points}')
        self.life_info.set_position(self.position_x, self.position_y)

    def set_img(self, png: str):
        img = pygame.image.load(png).convert_alpha()
        self.img = pygame.transform.scale(
            img,
            (int(self.DRAGON_PIC_SIZE_X * self.DRAGON_SIZE), int(self.DRAGON_PIC_SIZE_Y * self.DRAGON_SIZE))
        )

