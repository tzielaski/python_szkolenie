import random
from enum import Enum
from math import sqrt


class Status(Enum):
    ALIVE = 1
    DEAD = 0
    ATTACK = 2


class Dragon:
    HIT_POINTS_MIN = 30
    HIT_POINTS_MAX = 40
    ATTACK_MIN = 5
    ATTACK_MAX = 50
    GOLD_MIN = 1
    GOLD_MAX = 100
    DRAGON_PNG = r'res/dragon.png'
    DRAGON_DEAD_PNG = r'res/dead-dragon.png'
    DRAGON_SIZE = 0.7
    DRAGON_PIC_SIZE_X = 200
    DRAGON_PIC_SIZE_Y = 200
    MOVE_RANGE = 150
    ATTACK_RANGE = 120

    def __init__(self, name, position_x=0, position_y=0):
        self.name = name
        self.hit_points = random.randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
        self.position_x = position_x
        self.position_y = position_y
        self.texture = self.DRAGON_PNG
        self.status = Status.ALIVE
        self.gold = random.randint(self.GOLD_MIN, self.GOLD_MAX)

    def take_damage(self, damage):
        if self.is_dead():
            return False
        self.hit_points -= damage
        print(f'{self.name} dragon received {damage} dmg.')
        if self.hit_points <= 0:
            self.hit_points = 0
            self.die()
        else:
            print(f'{self.name} dragon HP left: {self.hit_points}\n')
        return True

    def make_damage(self, position):
        if self.is_dead():
            return 0
        range_x = self.position_x - position[0]
        range_y = self.position_y - position[1]
        range_xy = sqrt(range_x ** 2 + range_y ** 2)
        if range_xy > self.ATTACK_RANGE:
            return 0
        return random.randint(self.ATTACK_MIN, self.ATTACK_MAX)

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y
        return True

    def get_position(self):
        return self.position_x, self.position_y

    def move(self, left=0, right=0, down=0, up=0):
        self.position_x += right - left
        self.position_y += down - up

    def die(self):
        self.status = Status.DEAD
        self.texture = self.DRAGON_DEAD_PNG

    def is_dead(self):
        return self.status == Status.DEAD

    def is_alive(self):
        return self.status != Status.DEAD

    def drop_possessions(self):
        gold = self.gold
        self.gold = 0
        return gold

    def has_possessions(self):
        if self.gold > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    wawelski = Dragon(name='Wawelski', position_x=0, position_y=0)

    wawelski.set_position(x=10, y=20)
    print(f'{wawelski.name}: {wawelski.get_position()}')
    wawelski.move(left=10, down=20)
    print(f'{wawelski.name}: {wawelski.get_position()}')
    wawelski.move(right=15, up=5)
    print(f'{wawelski.name}: {wawelski.get_position()}')

    wawelski.take_damage(10)
    wawelski.take_damage(50)
    wawelski.take_damage(35)
    wawelski.take_damage(20)
