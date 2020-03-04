import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import  sleep


def check_keydown_event(event, make_settings, screen, ship, bullets):
    """响应按键"""
    # 对象左右移动时，按键的情况
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        bullet_fire(make_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_event(event, ship):
    """响应松开"""
    # 对象左右移动时，松键的情况
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_event(make_settings, screen, ship, bullets):
    """监测事件"""
    # 当我们按键时，python会注册一个事件，我们通过pygame.event.get()函数取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, make_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def get_number_aliens_x(make_settings, alien):
    """计算每行能容下多少外星人"""
    alien_needed_space = make_settings.screen_width - 2 * alien.rect.width
    x_number = int(alien_needed_space / (2 * alien.rect.width))
    return x_number


def get_number_aliens_y(make_settings, ship, alien):
    """创建多行外星人"""
    # 计算在y方向上能用的空余空间
    alien_needed_space_y = (make_settings.screen_height -
                            (3 * alien.rect.height) - ship.rect.height)
    # 计算获知在y方向上能放置多少行的外星人舰队
    y_number = int(alien_needed_space_y / (2 * alien.rect.height))
    return y_number


def create_alien(make_settings, screen, aliens, alien_number, alien_number_y):
    """创建一个外星人并将其放进当前行"""
    alien = Alien(make_settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * alien_number_y
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleets(make_settings, screen, ship, aliens):
    """创建外星人飞船舰队"""
    alien = Alien(make_settings, screen)
    # 两个嵌套循环
    for alien_number_y in range(get_number_aliens_y(make_settings, ship, alien)):
        for alien_number in range(get_number_aliens_x(make_settings, alien)):
            create_alien(make_settings, screen, aliens, alien_number,
                                                        alien_number_y)



def update_alien(make_settings, screen, stats, ship, bullets, aliens):
    """更新外星人，用于主程序中"""
    check_edge(make_settings, aliens)
    aliens.update()

    check_alien_bottom_screen(make_settings, screen, stats, ship, bullets, aliens)
    # 监测外星人和飞船的碰撞，接受两个实参，一个精灵和一个编组
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit_and_end(make_settings, screen, stats, ship, bullets, aliens)


def check_edge(make_settings, aliens):
    """检测碰撞并让外星人折返、下降"""
    # 遍历字典
    for alien in aliens.sprites():
        # 检查到外星人碰到边缘时才能会启动下面的代码
        if alien.alien_check_edge():
            make_settings.a_direction *= -1
            for alien in aliens.sprites():
                # 外星人变向，下移
                alien.rect.y += make_settings.alien_drop_speed
            break


def check_alien_bottom_screen(make_settings, screen,
                              stats, ship, bullets, aliens):
    """检查外星人与屏幕下方是否碰撞"""
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            ship_hit_and_end(make_settings, screen, stats, ship, bullets, aliens)
            break


def update_screen(make_settings, screen, ship, aliens, bullets):
    """更新屏幕的图像，并且切换到新屏幕"""
    # 每次循环都重新绘制屏幕
        # 调用了方法 screen.fill（），用来充填屏幕，这种方法只能选取一种颜色
    screen.fill(make_settings.bg_color)
    # 飞船移动起来
    ship.move()
    # 在飞船和外星人后面重新绘制所有子弹!!!!可以放到ship.blitme()函数后面吗？！！！
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人, 调用draw()时，自动绘制编组中的每个元素，根据rect来确实绘制的位置。
    # 在这里，aliens.draw(screen)在屏幕上绘制编组中的每个外星人
    aliens.draw(screen)
    # 是最近更新的屏幕可见
    pygame.display.flip()


def bullet_fire(make_settings, screen, ship, bullets):
    # 同屏子弹最多不能超过几颗（settings文件中可以设置）
    if len(bullets) <= make_settings.bullet_allowed:
        # 创建一个子弹并将其加入编组bullets中！！！不明白为何要加入编组！！！
        new_bullet = Bullet(make_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(make_settings, screen, ship, bullets, aliens):
    """更新子弹的位置并删除超过屏幕的无效子弹"""
    # 对Group中的每一个元素调用bullet 文件中的update（）方法，更新子弹的位置
    bullets.update()
    bullets_alien_collisions(make_settings, screen, ship, bullets, aliens)
    delete_bullet(bullets)


def bullets_alien_collisions(make_settings, screen, ship, bullets, aliens):
    """子弹与外星人的碰撞检测"""
    # 碰撞检测，如果设置第一个关键字为false，子弹有贯穿效果,
    # 第二个设置为false可以让外星人被击中不消失
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除为空的外星人编组中余下的精灵
        aliens.empty()
        create_fleets(make_settings, screen, ship, aliens)


def delete_bullet(bullets):
    """删除无效的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def ship_hit_and_end(make_settings, screen, stats, ship, bullets, aliens):
    """处理外星人击中飞船后的情况处理, 并停止游戏在飞船为0时"""
    if stats.ship_left > 1:
        stats.ship_left -= 1
        # 清空子弹列表和外星人列表
        bullets.empty()
        aliens.empty()

        # 重置飞机位置，重新生成外星人
        ship.ship_center()
        create_fleets(make_settings, screen, ship, aliens)

        # 暂停
        sleep(1)
    else:
        stats.game_activity = False

