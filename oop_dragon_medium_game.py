import pygame
import random
from time import sleep

from oop_dragon_easy import Dragon, Status

SCREEN_MIN_X = 0
SCREEN_MAX_X = 1024
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 768
BACKGROUND_SIZE_X = 470
BACKGROUND_SIZE_Y = 403


class SuperDragon(Dragon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.img = pygame.image.load(self.DRAGON_PNG).convert_alpha()
        self.img = pygame.transform.scale(
            self.img,
            (int(self.DRAGON_PIC_SIZE_X * self.DRAGON_SIZE), int(self.DRAGON_PIC_SIZE_Y * self.DRAGON_SIZE))
        )

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
        self.img = pygame.transform.rotate(self.img, 180)

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
        if self.is_dead():
            return False
        self.hit_points -= damage
        print(f'{self.name} hero received {damage} dmg.')
        if self.hit_points < 0:
            self.die()
        else:
            print(f'{self.name} hero HP left: {self.hit_points}\n')
        return True

    def make_damage(self):
        return random.randint(self.ATTACK_MIN, self.ATTACK_MAX)

    def die(self):
        self.status = Status.DEAD
        print(f'{self.name} hero is dead')

    def is_dead(self):
        return self.status == Status.DEAD

    def is_alive(self):
        return self.status != Status.DEAD


def update_display(background, dragon: SuperDragon):
    for i in range(SCREEN_MIN_X, SCREEN_MAX_X, BACKGROUND_SIZE_X):
        for j in range(SCREEN_MIN_Y, SCREEN_MAX_Y, BACKGROUND_SIZE_Y):
            screen.blit(background, (i, j))
    screen.blit(dragon.get_img(), dragon.get_position())
    pygame.display.update()


def prepare_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_MAX_X, SCREEN_MAX_Y))
    background = pygame.image.load(r'res\background.jpg').convert()
    return screen, background


if __name__ == '__main__':
    screen, background = prepare_screen()

    wawelski = SuperDragon(name='Wawelski', position_x=0, position_y=0)
    wawelski.set_position(x=10, y=20)
    jose = Hero(name='José Jiménez')

    update_display(background, wawelski)
    sleep(0.5)
    # for

    while wawelski.is_alive() and jose.is_alive():
        wawelski.random_move()
        dmg = wawelski.make_damage()
        jose.take_damage(dmg)
        sleep(0.5)
        update_display(background, wawelski)
        if jose.is_dead():
            break
        dmg = jose.make_damage()
        wawelski.take_damage(dmg)
        wawelski.random_move()
        sleep(0.5)
        update_display(background, wawelski)
    input()
