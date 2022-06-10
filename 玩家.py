import pygame


class 玩家():

    def __init__(self, x, y):

        self.矩形 = pygame.Rect(x, y, 80, 180)
        self.y速度 = 0
        self.跳跃 = False
        self.攻击类型 = 0
        self.攻击中 = False
        self.生命值 = 100
        self.图片翻转 = False

    def 移动(self, 宽度, 高度, 屏幕, 敌人):

        速度 = 10
        重力 = 2
        x增量 = 0
        y增量 = 0

        # 获取 键盘事件
        key = pygame.key.get_pressed()

        if self.攻击中 == False:

            # 左右移动
            if key[pygame.K_a]:
                x增量 = -速度
            if key[pygame.K_d]:
                x增量 = 速度
            # 跳跃
            if key[pygame.K_w] and not self.跳跃:
                self.y速度 = -30
                self.跳跃 = True

            # 攻击
            if key[pygame.K_r] or key[pygame.K_t]:
                self.攻击(屏幕, 敌人)
                if key[pygame.K_r]:
                    self.攻击类型 = 1
                if key[pygame.K_t]:
                    self.攻击类型 = 2

        # 重力影响
        self.y速度 += 重力
        y增量 += self.y速度

        # 确保玩家待在屏幕
        # 左边判断   5 + (-10) < 0 => x = 0 - 5 = -5
        if self.矩形.left + x增量 < 0:
            x增量 = 0 - self.矩形.left
        # 右边判断   1000 + 10 > 1000 => x = 1000 - 1000 = 0
        if self.矩形.right + x增量 > 宽度:
            x增量 = 宽度 - self.矩形.right
        # 下方判断
        if self.矩形.bottom + y增量 > 高度 - 110:
            self.y速度 = 0
            y增量 = 高度 - 110 - self.矩形.bottom
            self.跳跃 = False
            # y增量 = 0
            # print(高度, 110, self.矩形.bottom, y增量)

        if 敌人.矩形.centerx > self.矩形.centerx:
            self.图片翻转 = False
        else:
            self.图片翻转 = True

        self.矩形.x += x增量
        self.矩形.y += y增量

    def 攻击(self, 屏幕, 敌人):
        self.攻击中 = True
        攻击矩形 = pygame.Rect(self.矩形.centerx - (2 * self.矩形.width * self.图片翻转), self.矩形.y, 2 *
                           self.矩形.width, self.矩形.height)
        if 攻击矩形.colliderect(敌人.矩形):
            敌人.生命值 -= 10
        pygame.draw.rect(屏幕, (0, 255, 0), 攻击矩形)

    def 绘制(self, 屏幕):
        pygame.draw.rect(屏幕, (255, 0, 0), self.矩形)
