import random
from enum import Enum

DRAGON_PNG = 'dragon.png'
DRAGON_DEAD_PNG = 'dragon-dead.png'


class Status(Enum):
    ALIVE = 1
    DEAD = 0


class Dragon:
    HIT_POINTS_MIN = 50
    HIT_POINTS_MAX = 100
    ATTACK_MIN = 5
    ATTACK_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, position_x=0, position_y=0):
        self.name = name
        self.hit_points = random.randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
        self.position_x = position_x
        self.position_y = position_y
        self.texture = DRAGON_PNG
        self.status = Status.ALIVE

    def take_damage(self, damage):
        if self.is_alive():
            self.hit_points -= damage
            print(f'{self.name} dragon received {damage} dmg.')
            if self.hit_points < 0:
                self.die()
            else:
                print(f'{self.name} dragon HP left: {self.hit_points}\n')
            return True
        return False

    def make_damage(self):
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
        self.texture = DRAGON_DEAD_PNG
        print(f'{self.name} dragon is dead')
        self.drop_possessions()

    def is_dead(self):
        return self.status == Status.DEAD

    def is_alive(self):
        return self.status != Status.DEAD

    def drop_possessions(self):
        gold_amt_left = random.randint(self.GOLD_MIN, self.GOLD_MAX)
        print(f'{self.name} dragon left {gold_amt_left} gold at {(self.get_position())}')


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
