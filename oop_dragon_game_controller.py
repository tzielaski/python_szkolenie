import os
import sys
from dataclasses import dataclass
from time import sleep

import pygame

import oop_dragon_game_config as conf
from oop_dragon_game_gold import GoldGenerator, Gold
from oop_dragon_game_hero import Hero
from oop_dragon_medium_game import Dragon


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
        pygame.mixer.init()
        pygame.mixer.music.load(conf.HIT_SOUND)
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
            if isinstance(drawable, Dragon):
                self.check_death(drawable)
            if isinstance(drawable, Hero):
                self.check_death(drawable)
                self.check_hero_coin_collection(drawable)

    def check_hero_coin_collection(self, hero):
        for i, collision_candidate in enumerate(self.drawable_objects):
            if isinstance(collision_candidate, Gold):
                coin = collision_candidate
                if hero.collides(coin.get_center()):
                    self.drawable_objects.remove(collision_candidate)
                    hero.add_gold(1)

    def check_death(self, creature):
        if creature.is_dead() and creature.has_possessions():
            gold = creature.drop_possessions()
            for coin in GoldGenerator.generate(gold, creature.get_middle_lower()):
                self.add_drawable(coin)

    def resolve_pressed_keys(self, key_pressed):
        if key_pressed == pygame.K_a:
            self.hero_attack()
            pygame.mixer.music.play(0)
        else:
            pressed = pygame.key.get_pressed()
            jose.move(
                up=pressed[pygame.K_UP],
                left=pressed[pygame.K_LEFT],
                right=pressed[pygame.K_RIGHT],
                down=pressed[pygame.K_DOWN]
            )

    @staticmethod
    def is_hero(object):
        return isinstance(object, Hero)

    @staticmethod
    def is_super_dragon(object):
        return isinstance(object, Dragon)

    def move_dragons(self):
        for dragon in self.drawable_objects:
            if isinstance(dragon, Dragon):
                dragon.random_move()

    def hero_attack(self):
        for hero in self.drawable_objects:
            if GameController.is_hero(hero):
                hero_dmg = 0
                for dragon in self.drawable_objects:
                    if GameController.is_super_dragon(dragon):
                        dragon_dmg = hero.make_damage(dragon.get_position())
                        dragon.take_damage(dragon_dmg)
                        hero_dmg += dragon.make_damage(hero.get_position())
                hero.take_damage(hero_dmg)


if __name__ == '__main__':
    game_controller = GameController()
    wawelski = Dragon(name='Wawelski', position_x=0, position_y=0)
    wawelski.set_position(x=300, y=300)
    game_controller.add_drawable(wawelski)

    ancalagon = Dragon(name='Ancalagon', position_x=500, position_y=200)
    game_controller.add_drawable(ancalagon)

    jose = Hero(name='José Jiménez')
    game_controller.add_drawable(jose)

    while 1:
        game_controller.check_objects_state()
        game_controller.update_display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_controller.resolve_pressed_keys(event.key)
        sleep(0.025)