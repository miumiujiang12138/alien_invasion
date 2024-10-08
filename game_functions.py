import sys
import pygame
import bullet
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
       fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings,screen,ship,bullets):
     # 创建一颗子弹并且将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
       new_bullet = bullet.Bullet(ai_settings,screen,ship)
       bullets.add(new_bullet)
    
def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
def  update_bullets(bullets):
    """更新子弹位置，并且删除已经消失的子弹"""   
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():    # 遍历是用的bullet编组的副本，删除是在bullet编组中进行的
                                        # 如果在for循环中从列表或者编组中删除条目会导致混乱和出错
        if bullet.rect.bottom <= 0:
         bullets.remove(bullet)
        # print(len(bullets))   
            

def update_screen(ai_settings,screen,ship,alien,bullets):
    """更新屏幕上的图像，并且切换到新屏幕"""
   
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()