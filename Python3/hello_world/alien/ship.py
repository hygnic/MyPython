import pygame


class Ship():
    def __init__(self, make_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.make_settings = make_settings

        # 加载飞船图像并获取其外接矩形
            # 获取原始图像的位置
        self.image = pygame.image.load(r'C:\Users\hygnic\Desktop\hello_world\alien\images\ship.bmp')
            # 将获取的图像处理后传递给self.rect, self.rect是该类中的一个属性
            # get_rect()是一种矩形形状 图形处理方法
        self.rect = self.image.get_rect()
            # 将屏幕也进行处理
        self.screen_rect = screen.get_rect()

        # 移动标志
        self.move_right = False
        self.move_left = False

    def ship_center(self):
        # 将每艘新飞船放到屏幕底部中央
        # 将屏幕与飞船图像都居中，将下边缘也对齐。注意有赋予的关系在里面哦！！！
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def move(self):
        """根据移动标志决定是否移动"""
        # and连接，两个条件都满足才能运行；也就是说在按下按键并且对象（飞机）在屏幕内时
        # ，对象才能移动。注意right,表示矩形右边
        if self.move_right and self.rect.right < self.screen_rect.right:
                                # 设置对象（飞机）的移动速度
            self.rect.centerx += self.make_settings.ship_speed
        # 坐标轴是左上角开始的
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= self.make_settings.ship_speed

    def blitme(self):
        """在指定位置绘制飞船"""
        # blit（）方法可以根据self.rect指定的位置将图像绘制到屏幕上
        self.screen.blit(self.image, self.rect)
