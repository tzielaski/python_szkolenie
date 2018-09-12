import random
from enum import Enum
from time import sleep

from oop_dragon_easy import Dragon, Status

DRAGON_PNG = 'dragon.png'
DRAGON_DEAD_PNG = 'dragon-dead.png'
SCREEN_MIN_X = 0
SCREEN_MAX_X = 1024
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 768


class SuperDragon(Dragon):
    def move(self, left=0, right=0, down=0, up=0):
        """
        >>> drag = SuperDragon(name='test'); drag.move(right=SCREEN_MAX_X+1, down=SCREEN_MAX_Y+1); drag.get_position()
        (1024, 768)

        """
        self.set_position(
            self.position_x + right - left,
            self.position_y + down - up
        )

    def set_position(self, x, y):
        self.position_x = max([x, SCREEN_MIN_X])
        self.position_y = max([y, SCREEN_MIN_Y])

        self.position_x = min([self.position_x, SCREEN_MAX_X])
        self.position_y = min([self.position_y, SCREEN_MAX_Y])


class Hero:
    HIT_POINTS_MIN = 100
    HIT_POINTS_MAX = 150
    ATTACK_MIN = 1
    ATTACK_MAX = 15

    def __init__(self, name):
        self.name = name
        self.hit_points = random.randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
        self.status = Status.ALIVE

    def take_damage(self, damage):
        if self.is_alive():
            self.hit_points -= damage
            print(f'{self.name} hero received {damage} dmg.')
            if self.hit_points < 0:
                self.die()
            else:
                print(f'{self.name} hero HP left: {self.hit_points}\n')
            return True
        return False

    def make_damage(self):
        return random.randint(self.ATTACK_MIN, self.ATTACK_MAX)

    def die(self):
        self.status = Status.DEAD
        print(f'{self.name} hero is dead')

    def is_dead(self):
        return True if self.status == Status.DEAD else False

    def is_alive(self):
        return True if self.status != Status.DEAD else False


wawelski = SuperDragon(name='Wawelski', position_x=0, position_y=0)

wawelski.set_position(x=10, y=20)
jose = Hero(name='José Jiménez')

while wawelski.is_alive() and jose.is_alive():
    jose.take_damage(wawelski.make_damage())
    sleep(0.5)
    if jose.is_dead():
        break
    wawelski.take_damage(jose.make_damage())
    sleep(0.5)
