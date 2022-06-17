import pygame


class 玩家:

	# 构造函数
	def __init__(self, x, y, 翻转, 数据, 精灵序列图, 动画步骤列表):

		self.矩形 = pygame.Rect(x, y, 80, 180)
		self.y速度 = 0
		self.跳跃 = False
		self.攻击类型 = 0
		self.攻击中 = False
		self.生命值 = 10000
		self.图片翻转 = 翻转

		# 图片相关
		self.大小 = 数据[0]
		self.缩放 = 数据[1]
		self.偏移 = 数据[2]
		self.动画列表 = self.加载图片(精灵序列图, 动画步骤列表)
		self.动作 = 0 # 0 站立 1 奔跑 2 跳跃 3 进攻1 4 进攻2 5 受伤 6 死亡
		self.帧索引  = 0
		self.图片 = self.动画列表[self.动作][self.帧索引]


	def 加载图片(self, 精灵序列图, 动画步骤列表):

		动画列表 = []

		for y, 动画步骤 in enumerate(动画步骤列表):

			临时图片列表 = []

			for x in range(动画步骤):

				临时图片 = 精灵序列图.subsurface(x * self.大小,  y * self.大小, self.大小, self.大小)
				临时图片 = pygame.transform.scale(临时图片, (self.大小 * self.缩放, self.大小 * self.缩放))
				临时图片列表.append(临时图片)

			动画列表.append(临时图片列表)

		return 动画列表


	def 移动(self, 宽度, 高度, 屏幕, 敌人):

		重力 = 2

		速度 = 10
		x增量 = 0
		y增量 = 0

		键盘 = pygame.key.get_pressed()

		# if self.攻击中 == False:
		if 键盘[pygame.K_a]:
			x增量 = -速度
		if 键盘[pygame.K_d]:
			x增量 = 速度
		if 键盘[pygame.K_w] and self.跳跃 == False:
			self.y速度 = -30
			self.跳跃 = True

		# 发动攻击
		if 键盘[pygame.K_j] or 键盘[pygame.K_k]:
			self.攻击(屏幕, 敌人)
			if 键盘[pygame.K_j]:
				self.攻击类型 = 1
			if 键盘[pygame.K_k]:
				self.攻击类型 = 2


		self.y速度 += 重力
		y增量 += self.y速度


		# 左右移动  左边界
		if self.矩形.left + x增量 < 0:
			x增量 = 0 - self.矩形.left
		# 左右移动  右边界
		if self.矩形.right + x增量 > 宽度:
			x增量 = 0

		# 下方判断
		if self.矩形.bottom + y增量 > 高度 - 110:
			self.y速度 = 0
			y增量 = 0
			self.跳跃 = False

		if 敌人.矩形.centerx >  self.矩形.centerx:
			self.图片翻转 = False
		else:
			self.图片翻转 = True

		self.矩形.x += x增量
		self.矩形.y += y增量

	def 攻击(self, 屏幕, 敌人):

		self.攻击中 = True

		攻击矩形 = pygame.Rect(
			self.矩形.centerx - (2 * self.矩形.width * self.图片翻转),
			self.矩形.y,
			2 * self.矩形.width,
			self.矩形.height
		)

		if 攻击矩形.colliderect(敌人.矩形):
			敌人.生命值 -= 100

		pygame.draw.rect(屏幕, (0, 255, 0), 攻击矩形)

	def 绘制(self, 屏幕):
		图片 = pygame.transform.flip(self.图片, self.图片翻转, False)
		pygame.draw.rect(屏幕, (100, 100, 100), self.矩形)
		屏幕.blit(图片,
			(
				self.矩形.x - int(self.偏移[0] * self.缩放),
				self.矩形.y - int(self.偏移[1] * self.缩放),
				# self.矩形.x,
				# self.矩形.y,
			)
		)
