import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船图像并设置其初始位置"""
        
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('ship.bmp') # 返回一个surface对象，在Pygame中，Surface对象用于
                                                    # 表示屏幕或图像中的一个矩形区域，可以在这个区域内绘制图形、图片、文字等。
                                                    # 它可以看作是一张“画布”或“纸张”，上面可以进行各种绘图操作
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)    #将位置信息存储在浮点数变量中
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center         # 更新完self.center后再更新self.rect.centerx
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)