import sys
from dataclasses import dataclass

import pygame

import oop_dragon_game_config as conf
from oop_dragon_game_gold import GoldGenerator
from oop_dragon_game_hero import Hero
from oop_dragon_medium_game import SuperDragon


def resolve_pressed_keys(key_pressed):
    if key_pressed == pygame.K_a:

        wawelski.random_move()
        dmg = wawelski.make_damage(jose.get_position())
        jose.take_damage(dmg)

        dmg = jose.make_damage(wawelski.get_position())
        wawelski.take_damage(dmg)

    else:
        pressed = pygame.key.get_pressed()
        jose.move(
            up=pressed[pygame.K_UP],
            left=pressed[pygame.K_LEFT],
            right=pressed[pygame.K_RIGHT],
            down=pressed[pygame.K_DOWN]
        )


@dataclass
class GameController:
    screen: pygame.Surface
    background: pygame.Surface
    drawable_objects = []

    def __init__(self):
        self.prepare_screen()

    def add_drawable(self, object):
        self.drawable_objects.append(object)

    def get_drawables(self):
        return self.drawable_objects

    def prepare_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((conf.SCREEN_MAX_X, conf.SCREEN_MAX_Y))
        self.background = pygame.image.load(r'res\background.jpg').convert()

    def update_display(self):
        for i in range(conf.SCREEN_MIN_X, conf.SCREEN_MAX_X, conf.BACKGROUND_SIZE_X):
            for j in range(conf.SCREEN_MIN_Y, conf.SCREEN_MAX_Y, conf.BACKGROUND_SIZE_Y):
                self.screen.blit(self.background, (i, j))
        for drawable in self.drawable_objects:
            drawable.draw(self.screen)
        pygame.display.update()

    def check_objects_state(self):
        for drawable in self.drawable_objects:
            if isinstance(drawable, SuperDragon):
                super_dragon = drawable
                if super_dragon.is_dead() and super_dragon.has_possessions():
                    gold = super_dragon.drop_possessions()
                    for coin in GoldGenerator.generate(gold, super_dragon.get_middle_lower()):
                        self.add_drawable(coin)


if __name__ == '__main__':
    game_controller = GameController()
    wawelski = SuperDragon(name='Wawelski', position_x=0, position_y=0)
    wawelski.set_position(x=100, y=200)
    game_controller.add_drawable(wawelski)

    jose = Hero(name='José Jiménez')
    game_controller.add_drawable(jose)

    while 1:
        game_controller.check_objects_state()
        game_controller.update_display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                resolve_pressed_keys(event.key)
