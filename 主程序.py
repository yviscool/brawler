import pygame

# 从玩家的文件夹里面导入玩家类
from 玩家 import 玩家

# pygame 初始化
pygame.init()

时钟 = pygame.time.Clock()

帧数 = 60

宽度 = 1000
高度 = 600

# 通过 display(显示) 模块创建屏幕对象
屏幕 = pygame.display.set_mode((宽度, 高度))


背景图片 = pygame.image.load(
    'assets/images/background/background.jpg').convert_alpha()


战士大小 = 162
战士缩放 = 4
战士偏移量 = [72, 56]
战士数据 = [战士大小, 战士缩放, 战士偏移量]
巫师大小 = 250
巫师缩放 = 3
巫师偏移量 = [112, 107]
巫师数据 = [巫师大小, 巫师缩放, 巫师偏移量]


# 加载精灵地图
# warrior 战士
战士序列图 = pygame.image.load(
    "assets/images/warrior/Sprites/warrior.png").convert_alpha()
# wizard 巫师
巫师序列图 = pygame.image.load(
    "assets/images/wizard/Sprites/wizard.png").convert_alpha()


战士动画步骤 = [10, 8, 1, 7, 7, 3, 7]
巫师动画步骤 = [8, 8, 1, 8, 8, 3, 7]


运行 = True

绿色 = (0, 255, 0)
红色 = (255, 0, 0)
白色 = (255, 255, 255)


def 绘制背景():
    缩放的图片 = pygame.transform.scale(背景图片, (宽度, 高度))
    屏幕.blit(缩放的图片, (0, 0))


def 绘制血量(生命值, x, y):
    比例 = 生命值 / 10000
    pygame.draw.rect(屏幕, 白色, (x - 2, y - 3, 404, 36))
    pygame.draw.rect(屏幕, 红色, (x, y, 400, 30))
    pygame.draw.rect(屏幕, 绿色, (x, y, 400 * 比例, 30))


# 类的实例化
玩家1 = 玩家(100, 310, False, 战士数据, 战士序列图, 战士动画步骤)
玩家2 = 玩家(600, 310, True, 巫师数据, 巫师序列图, 巫师动画步骤)


while 运行:

    时钟.tick(帧数)

    绘制背景()

    绘制血量(玩家1.生命值, 20, 20)
    绘制血量(玩家2.生命值, 570, 20)

    玩家1.移动(宽度, 高度, 屏幕, 玩家2)

    玩家1.更新()
    玩家2.更新()

    # 使用玩家1的绘制方法
    玩家1.绘制(屏幕)
    玩家2.绘制(屏幕)
    # 玩家2.移动(宽度, 高度, 屏幕, 玩家1)

    # 获取游戏里面的事件, 包括键盘, 鼠标, 关闭等等事件
    for 事件 in pygame.event.get():
        # 如果事件的类型等于关闭的话, 执行
        if 事件.type == pygame.QUIT:

            运行 = False
    # 刷新事件
    pygame.display.update()

# 退出游戏
pygame.quit()
