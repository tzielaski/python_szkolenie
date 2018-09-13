import random
from dataclasses import dataclass

import pygame
from oop_dragon_game_config import SCREEN_MAX_Y, SCREEN_MAX_X, SCREEN_MIN_Y, SCREEN_MIN_X


@dataclass
class Gold:
    position_x: int
    position_y: int
    img: pygame.Surface = None
    GOLD_PNG = r'res\coing.png'
    PIC_SIZE_X = 200
    PIX_SIZE_Y = 200
    PIC_SIZE = 0.1
    MOVE_RANGE = 30

    def draw(self, surface):
        img = pygame.image.load(self.GOLD_PNG).convert_alpha()
        self.img = pygame.transform.scale(
            img,
            (int(self.PIC_SIZE_X * self.PIC_SIZE), int(self.PIX_SIZE_Y * self.PIC_SIZE))
        )
        surface.blit(self.get_img(), self.get_position())

    def set_position(self, x, y):
        self.position_x = x if x >= SCREEN_MIN_X else SCREEN_MIN_X
        self.position_y = y if y >= SCREEN_MIN_Y else SCREEN_MIN_Y

        self.position_x = self.position_x if self.position_x <= SCREEN_MAX_X else SCREEN_MAX_X
        self.position_y = self.position_y if self.position_y <= SCREEN_MAX_Y else SCREEN_MAX_Y

    def random_move(self):
        moves = {
            'left': random.randint(0, self.MOVE_RANGE),
            'right': random.randint(0, self.MOVE_RANGE),
            'up': random.randint(0, self.MOVE_RANGE),
            'down': random.randint(0, self.MOVE_RANGE),
        }
        self.move(**moves)


class GoldGenerator:
    @classmethod
    def generate(cls, number, position):
        gold = []
        for i in range(0, number):
            gold.append(Gold(*position).random_move())
        return gold
