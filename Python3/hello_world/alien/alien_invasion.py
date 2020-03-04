import pygame
# 将模块导入，不是函数，出于简化所以设置别名
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # 初始化游戏,创建一个屏幕对象,设置其屏幕属性
    pygame.init()
    make_settings = Settings()
    screen = pygame.display.set_mode(
        (make_settings.screen_width, make_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船实例
    ship = Ship(make_settings, screen)
    # 将飞船置于下方中间
    ship.ship_center()
    # 创建一个用于存储统计信息的实例
    stats = GameStats(make_settings)
    # 创建一个Group类的实例，并将其命名为bullet，就是子弹组
    bullets = Group()
    # 创建一个实例，外星人组
    aliens = Group()
    # 在一行中创建多个外星人
    gf.create_fleets(make_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(make_settings, screen, ship, bullets)
        if stats.game_activity:
            gf.update_bullets(make_settings, screen, ship, bullets, aliens)
            gf.update_alien(make_settings, screen, stats, ship, bullets, aliens)
            # 每次循环都重新绘制更新背景屏幕，并将屏幕显示出来
            gf.update_screen(make_settings, screen, ship, aliens, bullets)


run_game()
