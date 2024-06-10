import pygame


# 坚果实体
class WallNut:
    def __init__(self):
        self.size = 16
        self.images = [pygame.image.load('images/plants/WallNut/WallNut_{:d}.png'.format(i)).convert_alpha()
                       for i in range(self.size)]
        self.rect = self.images[0].get_rect()
        self.rect.left, self.rect.top = 300, 85
        self.zone = (0, 0)
        self.blood = 1000
        self.is_live = True
        self.money = 50
