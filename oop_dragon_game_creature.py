from math import sqrt

import pygame
import random

from oop_dragon_game_config import Status, SCREEN_MIN_X, SCREEN_MIN_Y, SCREEN_MAX_X, SCREEN_MAX_Y
from oop_dragon_game_interface_objects import InfoRectangle


class Creature:
    HIT_POINTS_MIN: int
    HIT_POINTS_MAX: int
    ATTACK_MIN: int
    ATTACK_MAX: int
    GOLD_MIN: int
    GOLD_MAX: int
    ALIVE_PNG = r'res/....png'
    DEAD_PNG = r'res/....png'
    ATTACK_PNG = r'res/....png'
    MOVE_PNG = r'res/....png'
    SIZE: int = 0.7
    PNG_SIZE_X = 200
    PNG_SIZE_Y = 200
    MOVE_RANGE: int
    ATTACK_RANGE: int
    img: pygame.Surface
    STATUS_DURATION = 2

    def __init__(self, name, position_x=0, position_y=0):
        self.name = name
        self.hit_points = random.randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
        self.position_x = position_x
        self.position_y = position_y
        self.texture = self.ALIVE_PNG
        self.status_counter = 0
        self.status = Status.ALIVE
        self.set_img(self.status_png_dict[self.status])
        self.gold = random.randint(self.GOLD_MIN, self.GOLD_MAX)
        self.life_info = InfoRectangle(position_x=self.position_x, position_y=self.position_y)
        self.start_hit_points = self.hit_points

    def set_status(self, status: Status):
        self.status = status
        self.status_counter = 0
        self.set_img(self.status_png_dict[status])

    def set_img(self, png: str):
        img = pygame.image.load(png).convert_alpha()
        self.img = pygame.transform.scale(
            img,
            (int(self.PNG_SIZE_X * self.SIZE), int(self.PNG_SIZE_Y * self.SIZE))
        )

    @property
    def status_png_dict(self):
        status_dict = {
            Status.ALIVE: self.ALIVE_PNG,
            Status.DEAD: self.DEAD_PNG,
            Status.ATTACK: self.ATTACK_PNG,
            Status.MOVE: self.MOVE_PNG
        }
        return status_dict

    def take_damage(self, damage):
        if self.is_dead():
            return False
        self.hit_points -= damage
        print(f'{self.name} hero received {damage} dmg.')
        if self.hit_points <= 0:
            self.hit_points = 0
            self.die()
        return True

    def make_damage(self, position):
        if self.is_dead():
            return 0
        self.set_status(Status.ATTACK)
        range_x = self.position_x - position[0]
        range_y = self.position_y - position[1]
        range_xy = sqrt(range_x ** 2 + range_y ** 2)
        if range_xy > self.ATTACK_RANGE:
            return 0
        return random.randint(self.ATTACK_MIN, self.ATTACK_MAX)

    def set_status(self, status: Status):
        self.status = status
        self.status_counter = 0
        self.set_img(self.status_png_dict[status])

    def die(self):
        self.set_status(Status.DEAD)

    def is_dead(self):
        return self.status == Status.DEAD

    def is_alive(self):
        return self.status != Status.DEAD

    def update_life_info(self):
        self.life_info.set_text(f'{self.name}: {round(self.hit_points)}/{self.start_hit_points}')
        self.life_info.set_position(self.position_x, self.position_y)

    def draw(self, surface: pygame.Surface):
        if self.status in (Status.ATTACK, Status.MOVE):
            self.status_counter += 1
            if self.status_counter >= self.STATUS_DURATION:
                new_status = Status.ALIVE if self.hit_points > 0 else Status.DEAD
                self.set_status(new_status)
        surface.blit(self.get_img(), self.get_position())
        self.update_life_info()
        self.life_info.draw(surface)

    def get_img(self):
        return self.img

    def get_position(self):
        return self.position_x, self.position_y

    def set_position(self, x, y):
        self.position_x = x if x >= SCREEN_MIN_X else SCREEN_MIN_X
        self.position_y = y if y >= SCREEN_MIN_Y else SCREEN_MIN_Y

        max_x = SCREEN_MAX_X - self.img.get_bounding_rect().width
        max_y = SCREEN_MAX_Y - self.img.get_bounding_rect().height

        self.position_x = self.position_x if self.position_x <= max_x else max_x
        self.position_y = self.position_y if self.position_y <= max_y else max_y

    def get_middle_lower(self):
        x = round(self.position_x + self.img.get_width() / 2.)
        y = self.position_y + self.img.get_height()
        return x, y

    def collides(self, position):
        """
        >>> import oop_dragon_game_config as conf
        >>> msg = pygame.init(); screen = pygame.display.set_mode((conf.SCREEN_MAX_X, conf.SCREEN_MAX_Y)); hero = Hero("TEST_HERO")
        >>> center = hero.img.get_bounding_rect().center
        >>> hero_pos = hero.get_position()
        >>> hero.collides((center[0] + hero_pos[0], center[1] + hero_pos[1]))
        1
        >>> hero.collides((0,0))
        0
        """
        rectangle = self.img.get_bounding_rect().move(self.position_x, self.position_y)
        return rectangle.collidepoint(position)

    def drop_possessions(self):
        gold = self.gold
        self.gold = 0
        return gold

    def has_possessions(self):
        if self.gold > 0:
            return True
        else:
            return False
