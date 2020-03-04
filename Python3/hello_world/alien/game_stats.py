class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, make_settings):
        """创建新实例时，初始化统计信息"""
        self.make_settings = make_settings
        # 函数也可以作为一个属性
        self.reset_stats()
        self.game_activity = True
    def reset_stats(self):
        """在游戏运行期间初始化统计信息"""
        self.ship_left = self.make_settings.ship_limit
