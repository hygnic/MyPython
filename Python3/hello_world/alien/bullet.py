import pygame
from pygame.sprite import Sprite


# 继承了模块pygame中的Sprite类，可将相关元素编组，进而同时操作编组中的全部元素
class Bullet(Sprite):
    """对飞船发射的子弹进行管理的类"""
    def __init__(self, make_settings, screen, ship):
        super().__init__()
        self.screen = screen
        # pygame.Rect()方法是从无到有创建一个矩形，通过该方法我们获得实例的图像属性
            # 我们在坐标（0,0）处生成子弹矩形图形
        self.rect = pygame.Rect(0, 0, make_settings.bullet_width,
            make_settings.bullet_height)
        # 将子弹的位置放到飞机那里
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # self.rect.centery == ship.rect.centery
        # 子弹颜色和速度设置
        self.color = make_settings.bullet_color
        self.b_speed = make_settings.bullet_speed
        # 子弹位置E?
        self.y = float(self.rect.y)

    def update(self):
        """"向上移动子弹"""
        self.rect.y -= self.b_speed

    def draw_bullet(self):
        """屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
