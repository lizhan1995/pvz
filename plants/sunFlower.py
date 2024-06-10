import pygame


# 太阳花实体
class SunFlower(pygame.sprite.Sprite):
    def __init__(self):
        super(SunFlower, self).__init__()
        self.size = 18
        self.images = [pygame.image.load('images/plants/SunFlower/SunFlower_{:d}.png'.format(i)).convert_alpha()
                       for i in range(self.size)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 300, 170
        self.zone = (0, 0)
        self.blood = 100
        self.is_live = True
        self.money = 50
