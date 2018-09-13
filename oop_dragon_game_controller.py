import sys

import pygame

import oop_dragon_game_config as conf
from oop_dragon_game_hero import Hero
from oop_dragon_medium_game import SuperDragon


def update_display(screen, background, drawable_objects: list):
    for i in range(conf.SCREEN_MIN_X, conf.SCREEN_MAX_X, conf.BACKGROUND_SIZE_X):
        for j in range(conf.SCREEN_MIN_Y, conf.SCREEN_MAX_Y, conf.BACKGROUND_SIZE_Y):
            screen.blit(background, (i, j))
    for drawable in drawable_objects:
        drawable.draw(screen)
    pygame.display.update()


def prepare_screen():
    pygame.init()
    screen = pygame.display.set_mode((conf.SCREEN_MAX_X, conf.SCREEN_MAX_Y))
    background = pygame.image.load(r'res\background.jpg').convert()

    return screen, background


def resolve_pressed_keys():
    if pygame.key.get_pressed()[pygame.K_a]:
        wawelski.random_move()
        dmg = wawelski.make_damage()
        jose.take_damage(dmg)

        dmg = jose.make_damage()
        wawelski.take_damage(dmg)

    else:
        pressed = pygame.key.get_pressed()
        jose.move(
            up=pressed[pygame.K_UP],
            left=pressed[pygame.K_LEFT],
            right=pressed[pygame.K_RIGHT],
            down=pressed[pygame.K_DOWN]
        )


if __name__ == '__main__':
    screen, background = prepare_screen()
    objects = []
    wawelski = SuperDragon(name='Wawelski', position_x=0, position_y=0)
    wawelski.set_position(x=100, y=200)
    objects.append(wawelski)

    jose = Hero(name='José Jiménez')
    objects.append(jose)
    update_display(screen, background, objects)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            update_display(screen, background, objects)
            if event.type == pygame.KEYDOWN:
                resolve_pressed_keys()
