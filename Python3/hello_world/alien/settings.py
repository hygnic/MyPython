class Settings():
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
        """"初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 200)
        # 飞船设置
        self.ship_speed = 2
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 70
        self.bullet_speed = 3
        self.bullet_allowed = 3
        # 外星人设置
        self.alien_speed = 1
        self.alien_drop_speed = 50
        # 表示外星人移动方向，1表示向右移动，-1向左
        self.a_direction = 1