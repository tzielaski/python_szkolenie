import pygame
import random

from oop_dragon_easy import Status
from oop_dragon_game_config import SCREEN_MAX_Y, SCREEN_MAX_X, SCREEN_MIN_Y, SCREEN_MIN_X
from oop_interface_objects import InfoRectangle


class Hero:
    HIT_POINTS_MIN = 100
    HIT_POINTS_MAX = 150
    ATTACK_MIN = 1
    ATTACK_MAX = 15
    ALIVE_PNG = r'res\hero_alive.png'
    DEAD_PNG = r'res\hero_dead.png'
    PNG_SIZE_X = 200
    PNG_SIZE_Y = 200
    SIZE = 1
    POSITION_DEFAULT = (SCREEN_MAX_X - PNG_SIZE_X, SCREEN_MAX_Y - PNG_SIZE_Y)

    def __init__(self, name):
        self.position_x, self.position_y = self.POSITION_DEFAULT
        self.name = name
        self.hit_points = random.randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
        self.start_hit_points = self.hit_points
        self.status = Status.ALIVE
        self.life_info = InfoRectangle(position=(0, SCREEN_MAX_Y - 32))
        self.set_img(self.ALIVE_PNG)

    def take_damage(self, damage):
        if self.is_dead():
            return False
        self.hit_points -= damage
        print(f'{self.name} hero received {damage} dmg.')
        if self.hit_points < 0:
            self.hit_points = 0
            self.die()
        return True

    def make_damage(self):
        return random.randint(self.ATTACK_MIN, self.ATTACK_MAX)

    def die(self):
        self.status = Status.DEAD
        print(f'{self.name} hero is dead')
        self.set_img(self.DEAD_PNG)

    def is_dead(self):
        return self.status == Status.DEAD

    def is_alive(self):
        return self.status != Status.DEAD

    def update_life_info(self):
        self.life_info.set_text(f'{self.name}: {self.hit_points}/{self.start_hit_points}')

    def draw(self, surface: pygame.Surface):
        surface.blit(self.get_img(), self.get_position())
        self.update_life_info()
        self.life_info.draw(surface)

    def set_img(self, png: str):
        img = pygame.image.load(png).convert_alpha()
        self.img = pygame.transform.scale(
            img,
            (int(self.PNG_SIZE_X * self.SIZE), int(self.PNG_SIZE_Y * self.SIZE))
        )

    def get_img(self):
        return self.img

    def get_position(self):
        return self.position_x, self.position_y

    def move(self, up, left, right, down):
        step = 10
        x, y = self.get_position()
        if up:
            y -= step
        if down:
            y += step
        if left:
            x -= step
        if right:
            x += step
        self.set_position(x, y)

    def set_position(self, x, y):
        self.position_x = x if x >= SCREEN_MIN_X else SCREEN_MIN_X
        self.position_y = y if y >= SCREEN_MIN_Y else SCREEN_MIN_Y

        self.position_x = self.position_x if self.position_x <= SCREEN_MAX_X else SCREEN_MAX_X
        self.position_y = self.position_y if self.position_y <= SCREEN_MAX_Y else SCREEN_MAX_Y