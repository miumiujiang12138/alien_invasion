import sys
import pygame
import bullet
from time import sleep
from alien import Alien
import ship
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
        
def  update_bullets(ai_settings,screen,ship,aliens,bullets):
    """更新子弹位置，并且删除已经消失的子弹"""   
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():    # 遍历是用的bullet编组的副本，删除是在bullet编组中进行的
                                        # 如果在for循环中从列表或者编组中删除条目会导致混乱和出错
        if bullet.rect.bottom <= 0:
         bullets.remove(bullet)
        # print(len(bullets)) 
        check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)  
    if len(aliens)==0:
        #删除现有的子弹并且新建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
            

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并且切换到新屏幕"""
   
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)           # 对编组调用draw()时，Pygame自动绘制编组里的每个元素，绘制的位置由
                                  # 元素的属性rect决定
    # 让最近绘制的屏幕可见
    pygame.display.flip()



def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可以容纳多少人"""
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并把它放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

"""添加行"""
def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少外星人"""
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows
def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
     for alien_number in range(number_aliens_x):
        create_alien(ai_settings,screen,aliens,alien_number,row_number)
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        # print("Ship hit!!!")
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets) 
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """响应飞船被外星人撞到"""
    if stats.ships_left >0:
        # 将ships_left减1
        stats.ships_left -= 1
        
        #暂停一会儿
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

    

