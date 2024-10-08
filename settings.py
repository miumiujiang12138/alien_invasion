class Settings():
    """存储Alien Invasion的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5   # 设置飞船的速度
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
