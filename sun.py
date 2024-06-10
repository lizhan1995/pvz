import pygame
import random


# 太阳实体
class Sun(pygame.sprite.Sprite):

    def __init__(self):
        super(Sun, self).__init__()

        self.size = 22
        self.images = [pygame.image.load('images/Sun/Sun_{:d}.png'.format(i)).convert_alpha()
                       for i in range(self.size)]
        self.rect = self.images[0].get_rect()
        # 随机产生的位置
        self.rect.left = random.randint(200, 1000)
        # 下落初始位置
        self.rect.top = 0
        # 随机指定一个太阳下落停止的位置
        self.stop_top = 90 + random.randint(0,  ((500 - 90) // 5) + 1 - 1) * 5
        # 下落速度
        self.speed = 5
        self.zone = (0, 0)
        self.status = True
        self.stop = False
        # 当停止下落后，太阳存在时长
        self.disappear_time = 5000
        # 当停止下落后，太阳开始显示的时间
        self.start_time = None

    # 下落事件
    def down(self):
        if not self.stop:
            if self.rect.top < 600:
                # 当下落到指定位置时，停止下落，设置开始停止的时间
                if self.rect.top == self.stop_top:
                    self.stop = True
                    self.start_time = pygame.time.get_ticks()
                else:
                    self.rect.top += self.speed
            else:
                self.status = False
        if self.stop:
            # 判断停止时间是否超过指定时间，超过时删除操作
            stop_time = pygame.time.get_ticks() - self.start_time
            if stop_time >= self.disappear_time:
                self.status = False
