import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """"表示单个外星人的类"""
    def __init__(self, make_settings, screen):
        super().__init__()
        self.screen = screen
        self.make_settings = make_settings
        # 获取图像
        self.image = pygame.image.load(r'images\alien1.bmp')
        self.rect = self.image.get_rect()
        # 设置外星人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    # def blitme(self):
    #     """绘制外星人"""
    #     # 根据self.rect指定的位置信息将外星人绘制在屏幕上
    #     self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += (self.make_settings.alien_speed *
                        self.make_settings.a_direction)

    def alien_check_edge(self):
        """监测外星人是否到达屏幕边缘,如果到达边缘，返回TRUE"""
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True

