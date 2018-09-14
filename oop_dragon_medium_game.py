import random
from oop_dragon_game_config import SCREEN_MIN_X, SCREEN_MAX_X, SCREEN_MIN_Y, SCREEN_MAX_Y, Status
from oop_dragon_game_creature import Creature
from oop_dragon_game_interface_objects import InfoRectangle


class Dragon(Creature):
    HIT_POINTS_MIN = 20
    HIT_POINTS_MAX = 50
    ATTACK_MIN = 10
    ATTACK_MAX = 40
    GOLD_MIN = 10
    GOLD_MAX = 40
    ALIVE_PNG = r'res/dragon.png'
    DEAD_PNG = r'res/dead-dragon.png'
    ATTACK_PNG = r'res/dragon.png'
    MOVE_PNG = r'res/dragon_move.png'
    DRAGON_SIZE = 0.7
    PNG_SIZE_X = 200
    PNG_SIZE_Y = 200
    MOVE_RANGE = 30
    ATTACK_RANGE = 120
    MOVE_INTERVAL = 100

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_hit_points = self.hit_points
        self.set_img(self.ALIVE_PNG)
        self.life_info = InfoRectangle(position_x=self.position_x, position_y=self.position_y)
        self.move_counter = 0

    def move(self, left=0, right=0, down=0, up=0):
        """
        >>> drag = Dragon(name='test'); drag.move(right=SCREEN_MAX_X+1, down=SCREEN_MAX_Y+1);
        >>> (x,y) = drag.get_position()
        >>> (x,y) == (SCREEN_MAX_X, SCREEN_MAX_Y)
        True

        >>> drag = Dragon(name='test'); drag.move(left=SCREEN_MAX_X+1, right=SCREEN_MAX_Y+1);
        >>> (x,y) = drag.get_position()
        >>> (x,y) == (SCREEN_MIN_X, SCREEN_MIN_Y)
        True

        """
        if self.is_alive():
            self.set_position(
                self.position_x + right - left,
                self.position_y + down - up
            )
            self.set_status(Status.MOVE)

    def random_move(self):
        moves = {
            'left': random.randint(0, self.MOVE_RANGE),
            'right': random.randint(0, self.MOVE_RANGE),
            'up': random.randint(0, self.MOVE_RANGE),
            'down': random.randint(0, self.MOVE_RANGE),
        }
        self.move(**moves)

    def draw(self, surface):
        super().draw(surface)
        self.increase_move_counter()

    def increase_move_counter(self):
        self.move_counter += 1
        if self.move_counter >= self.MOVE_INTERVAL:
            self.move_counter = 0
            self.random_move()
