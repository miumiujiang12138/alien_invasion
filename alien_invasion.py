import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()    #初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))  # 创建一个screen窗口(screen对象)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)     # 创建一艘飞船
    bullets = Group()                   # 创建一个用于存储子弹的编组
    alien = Alien(ai_settings,screen)
    #开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        """ for event in pygame.event.get():       #监测事件函数    
             if event.type == pygame.QUIT:
                sys.exit() """
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,alien,bullets)
    """ screen.fill(ai_settings.bg_color)
        # 在指定位置绘制飞船
          ship.blitme()  
        # 让最近绘制的屏幕可见,刷新屏幕显示
           pygame.display.flip()"""
run_game()
