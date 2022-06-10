import pygame
from fighter import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


bg_image = pygame.image.load(
    "assets/images/background/background.jpg").convert_alpha()


def 绘制背景():
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))


# create two instances of fighters
玩家1 = 玩家(200, 310)
玩家2 = 玩家(700, 310)

# game loop
run = True

while run:

  clock.tick(FPS)

  # draw background
  绘制背景()

  # draw fighters
  fighter_1.draw(screen)
  fighter_2.draw(screen)

  # event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # update display
  pygame.display.update()

# exit pygame
pygame.quit()
