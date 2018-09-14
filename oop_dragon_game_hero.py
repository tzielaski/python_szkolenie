import pygame

from oop_dragon_game_config import SCREEN_MAX_Y, SCREEN_MAX_X, Color, Status
from oop_dragon_game_creature import Creature
from oop_dragon_game_interface_objects import InfoRectangle


class Hero(Creature):
    HIT_POINTS_MIN = 150
    HIT_POINTS_MAX = 200
    ATTACK_MIN = 1
    ATTACK_MAX = 15
    ALIVE_PNG = r'res\hero_alive.png'
    DEAD_PNG = r'res\hero_dead.png'
    ATTACK_PNG = r'res\hero_attack.png'
    MOVE_PNG = r'res\hero_walk.png'
    PNG_SIZE_X = 200
    PNG_SIZE_Y = 200
    SIZE = 1
    POSITION_DEFAULT = (SCREEN_MAX_X - PNG_SIZE_X, SCREEN_MAX_Y - PNG_SIZE_Y)
    STEP = 30
    ATTACK_RANGE = 150
    GOLD_MIN = 0
    GOLD_MAX = 0
    GOLD_INFO_POSITION = 0, 0
    status_png_dict = {
        Status.ALIVE: ALIVE_PNG,
        Status.DEAD: DEAD_PNG,
        Status.ATTACK: ATTACK_PNG,
        Status.MOVE: MOVE_PNG
    }

    def __init__(self, name):
        super().__init__(name)
        self.gold_info = InfoRectangle(*self.GOLD_INFO_POSITION, color=Color.GOLD)
        self.status_counter = 0
        self.set_position(*self.POSITION_DEFAULT)

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        self.update_gold_info()
        self.gold_info.draw(surface)

    def move(self, up, left, right, down):
        if self.is_dead():
            step = 0
        else:
            step = self.STEP
            self.set_status(Status.MOVE)

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

    def add_gold(self, number):
        self.gold += number

    def update_gold_info(self):
        self.gold_info.set_text(f'{self.name} gold: {self.gold}')

    def make_damage(self, position):
        range_x = self.position_x - position[0]
        if range_x < 0:
            return 0
        return super().make_damage(position)
