import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()  # 创建时钟对象
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # 创建游戏窗口
        pygame.display.set_caption("Alien Invasion")  # 设置窗口标题
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 侦听键盘和鼠标事件
            for event in pygame.event.get():  # 获取事件
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)  # 每次循环时都重绘屏幕
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            """
            更新屏幕内容
            Pygame 使用了一个双缓冲系统，在这个系统中，
            所有的绘制操作首先在一个后台缓冲区（也称为"back buffer"）上进行。
            只有当调用 pygame.display.flip() 或 pygame.display.update() 函数时，
            后台缓冲区的内容才会被送到前台缓冲区（也就是你的屏幕），从而更新屏幕上的显示。
            pygame.display.flip() 更新整个屏幕。
            这意味着它会将后台缓冲区中的所有内容一次性复制到前台缓冲区，包括所有的图形、文本和颜色变化。
            pygame.display.update() 允许你提供一个可选的矩形区域作为参数，
            这样你可以只更新屏幕上的这个特定区域。如果你不提供任何参数，update() 会默认更新整个屏幕，就像 flip() 一样。
            """
            pygame.display.flip()
            self.clock.tick(60)  # 每秒运行60次


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
