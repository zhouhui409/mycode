import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    	(ai_settings.screen_width, ai_settings.screen_heigt))
    pygame.display.set_caption("星球大战")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    bullets = Group()

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        # screen.fill(ai_settings.bg_color)
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
        # pygame.display.flip()


run_game()
