import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.scaled_width = 35
        self.scaled_height = 50
        self.scaledimage = pygame.transform.scale(self.image, (self.scaled_width, self.scaled_height))
        self.rect = self.scaledimage.get_rect()

        # 每膄新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.scaledimage, self.rect)