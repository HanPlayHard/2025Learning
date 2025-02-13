import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # 全屏模式
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # 设置背景色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            self._check_events()
            self.ship.update()
            # self.bullets.update()
            # 每次循环时都重绘屏幕
            # self.screen.fill(self.bg_color)

            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme

            # 让最近绘制的屏幕可见
            # pygame.display.flip()

            #             # 删除已消失的子弹
            #             """
            # ! 在使用 for 循环遍历列表（或 Pygame 编组）时，Python 要求该列表的
            # 长度在整个循环中保持不变。这意味着不能从 for 循环遍历的列表或编
            # 组中删除元素，因此必须遍历编组的副本。
            # When you use a for loop to loop through a list (or Pygame group),
            # Python requires the list's
            # The length remains the same throughout the cycle.
            # This means you can't loop over a list or compile from a for loop
            # Elements are removed from a group,
            # so a copy of the group must be iterated.
            #             """
            #             for bullet in self.bullets.copy():  # !
            #                 if bullet.rect.bottom <= 0:
            #                     self.bullets.remove(bullet)
            #             # print(len(self.bullets))
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RIGHT:
                #     # 向右移动飞船
                #     # self.ship.rect.x += 1
                #     self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = True
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = False
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建新子弹，并将其加入编组 bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置，并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():  # !
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        """检查是否有外星人位于屏幕边缘，并更新整个外星舰队的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """创建一个外星舰队"""
        # # 创建一个外星人
        # alien = Alien(self)
        # self.aliens.add(alien)
        # 创建一个外星人, 再不断添加，直到没有空间为止
        # 外星人的间距为外星人的宽度 和 高度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        # while current_x < (self.settings.screen_width - alien_width * 2):
        #     new_alien = Alien(self)
        #     new_alien.x = current_x
        #     new_alien.rect.x = current_x
        #     self.aliens.add(new_alien)
        #     current_x += alien_width * 2
        while current_y < (self.settings.screen_height - alien_height * 3):
            while current_x < (self.settings.screen_width - alien_width * 2):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
            # 添加一行外星人后，重置x值并递增y值
            current_x = alien_width
            current_y += alien_height * 2

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并将其放在当前行中"""
        """创建一个外星人并将其加入外星舰队"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队下移，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
