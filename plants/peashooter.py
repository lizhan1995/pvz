import pygame

from bullet import Bullet


# 豌豆实体
class Peashooter:
    def __init__(self):
        self.size = 13
        self.images = [pygame.image.load('images/plants/Peashooter/Peashooter_{:d}.png'.format(i)).convert_alpha()
                       for i in range(self.size)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 300, 260
        self.zone = (0, 0)
        self.blood = 100
        self.is_live = True
        self.money = 100
        self.bullet = None

    def shot(self):
        self.bullet = Bullet(self)
        return self.bullet
