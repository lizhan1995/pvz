import pygame

from zone import Zone


# 子弹实体
class Bullet(pygame.sprite.Sprite):
    zone = Zone()

    def __init__(self, plant):
        self.image = pygame.image.load('images/bullets/peaBullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = plant.zone[0] + 20
        self.rect.top = plant.zone[1]
        self.speed = 15
        self.status = True
        self.attact = 1

    # 子弹发射
    def move(self):
        if self.rect.left < 1200:
            self.rect.left += self.speed
        else:
            self.status = False

    # 子弹打中僵尸的事件
    def hit(self, enemy_list):
        for enemy in enemy_list:
            if pygame.sprite.collide_circle_ratio(0.5)(enemy, self):
                index_x, index_y = Bullet.zone.getIndex(enemy.rect.centerx, enemy.rect.centery)
                bt_x, bt_y = Bullet.zone.getIndex(self.rect.left, self.rect.top)
                if index_x == bt_x and index_y == bt_y:
                    enemy.blood -= self.attact
                    if enemy.blood <= 0:
                        enemy.is_live = False
                    self.status = False
