import pygame
import random

from zone import Zone


# 丧尸实体
class Zombie:

    zone = Zone()


    def __init__(self):
        self.size = 22
        self.images = [pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha()
                       for i in range(self.size)]
        self.rect = self.images[0].get_rect()
        self.rect.left = 1150
        # 随机产生的位置
        y = random.choice(range(5))
        self.rect.top = (y + 1) * Zone.Y_GRID_SIZE + Zone.Y_OFFSET_MAP - 150

        self.speed = 1
        self.blood = 30
        self.attact = 1
        self.old = 0
        self.is_live = True
        self.stop = False

    # 移动形态
    def move(self):
        if not self.stop:
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.is_live = False

    # 干饭的时候要改变形象
    def change_zombie(self):
        if self.old == 0:
            self.size = 22
            self.images = [pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha()
                           for i in range(self.size)]
        elif self.old == 1:
            self.size = 21
            self.images = [pygame.image.load('images/ZombieAttack/ZombieAttack_{:d}.png'.format(i)).convert_alpha()
                           for i in range(self.size)]

    # 干饭
    def eat(self, enemy_list):
        for enemy in enemy_list:
            enemy.rect.left, enemy.rect.top = enemy.zone
            if pygame.sprite.collide_circle_ratio(0.5)(enemy, self):
                index_x, index_y = Zombie.zone.getIndex(enemy.zone[0], enemy.zone[1])
                zm_x, zm_y = Zombie.zone.getIndex(self.rect.centerx, self.rect.centery)
                if index_x == zm_x and index_y == zm_y:
                    self.old = 1
                    # 丧尸碰到物体了，停止行动
                    self.stop = True
                    enemy.blood -= self.attact
                    # 吃完就开心的走了
                    if enemy.blood <= 0:
                        enemy.is_live = False
                        self.stop = False
                        self.old = 0
