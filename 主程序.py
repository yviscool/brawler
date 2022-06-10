import pygame
from 玩家 import 玩家

pygame.init()

# create game window
宽度 = 1000
高度 = 600

屏幕 = pygame.display.set_mode((宽度, 高度))
pygame.display.set_caption("Brawler")

# set framerate
时钟 = pygame.time.Clock()
帧数 = 60

# define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


背景图片 = pygame.image.load(
    "assets/images/background/background.jpg").convert_alpha()


def 绘制背景():
    缩放后的图片 = pygame.transform.scale(背景图片, (宽度, 高度))
    屏幕.blit(缩放后的图片, (0, 0))


def 绘制血量(生命值, x, y):
    比例 = 生命值 / 100
    pygame.draw.rect(屏幕, WHITE, (x, y, 400, 30), 40)
    pygame.draw.rect(屏幕, RED, (x, y, 400, 30))
    pygame.draw.rect(屏幕, YELLOW, (x, y, 400 * 比例, 30))


# create two instances of fighters
玩家1 = 玩家(200, 310)
玩家2 = 玩家(700, 310)

# game loop
运行 = True

while 运行:

    时钟.tick(帧数)

    # draw background
    绘制背景()

    玩家1.移动(宽度, 高度, 屏幕, 玩家2)
    # 玩家2.移动()

    绘制血量(玩家1.生命值, 20, 20)
    绘制血量(玩家2.生命值, 580, 20)

    玩家1.绘制(屏幕)
    玩家2.绘制(屏幕)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            运行 = False

    # update display
    pygame.display.update()

# exit pygame
pygame.quit()
