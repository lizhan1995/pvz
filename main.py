import pygame

from plants.peashooter import Peashooter
from plants.sunFlower import SunFlower
from plants.wallNut import WallNut
from sun import Sun
from zone import Zone
from zombie import Zombie

pygame.init()

# 定义下窗体的大小
screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF)

# 定义下窗体
pygame.display.set_caption('pvz')

# 定义背景图地址
bg_path = 'images/Background.jpg'
backgroup = pygame.image.load(bg_path).convert()
# 定义卡槽
card_slot = pygame.image.load('images/cardSlot.png').convert()
# 定义卡片
scale = 0.78
card = pygame.image.load('images/cards/card_peashooter.png').convert()
card_rect = card.get_rect()
card = pygame.transform.scale(card, (int(card_rect.width * scale), (card_rect.height * scale)))
cardTwo = pygame.image.load('images/cards/card_sunflower.png').convert()
card_rect_two = cardTwo.get_rect()
cardTwo = pygame.transform.scale(cardTwo, (int(card_rect_two.width * scale), (card_rect_two.height * scale)))
cardThree = pygame.image.load('images/cards/card_wallnut.png').convert()
card_rect_three = cardThree.get_rect()
cardThree = pygame.transform.scale(cardThree, (int(card_rect_three.width * scale), (card_rect_three.height * scale)))
# 阳光初始化数量
sun_num = '300'
font = pygame.font.SysFont('arial', 20)
fontImg = font.render(sun_num, True, (0, 0, 0))


def main():
    # 选择的卡片
    click_images = []
    # 豌豆集合
    pea_list = []
    # 向日葵集合
    flower_list = []
    # 坚果集合
    nut_list = []
    # 太阳集合
    sun_list = []
    click_type = None
    block = pygame.time.Clock()
    index = 0
    # 是否点击卡片
    is_pick = False
    # 太阳下落时间
    sun_event_time = pygame.USEREVENT + 1
    pygame.time.set_timer(sun_event_time, 3000)
    # 区域
    zone = Zone()
    # 子弹集合
    bullet_list = []
    # 僵尸集合
    zombie_list = []
    # 僵尸能攻击的集合（种植的植物）
    zombie_enemy_list = []
    # 僵尸产生的时间
    zombie_event_time = pygame.USEREVENT + 2
    pygame.time.set_timer(zombie_event_time, 10000)

    while 1:

        press = pygame.mouse.get_pressed()

        x, y = pygame.mouse.get_pos()

        # 监听鼠标操作事件
        for event in pygame.event.get():
            # 写个事件，点击右上角关闭按钮，可以退出窗口
            if event.type == pygame.QUIT:
                raise SystemExit

            # 随机产生太阳
            if event.type == sun_event_time:
                sun_list.append(Sun())

            # 随机产生僵尸
            if event.type == zombie_event_time:
                zombie_list.append(Zombie())

            # 加载太阳
            for sun in sun_list:
                # 点击太阳，进行积分累计
                if press[0] and sun.rect.collidepoint((x, y)):
                    sun_list.remove(sun)
                    global sun_num, font, fontImg
                    sun_num = str(int(sun_num) + 25)
                    fontImg = font.render(sun_num, True, (0, 0, 0))

            # 鼠标按钮按下事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if event.button == 1 and not is_pick:
                    if 329 <= x <= 329 + card.get_rect().width and 7 <= y <= 7 + card.get_rect().height:
                        click_type = 'pea'
                        pr = Peashooter()
                        if int(sun_num) > 0 and int(sun_num) >= pr.money:
                            click_images.append(pr)
                            is_pick = True
                    if 383 <= x <= 383 + card.get_rect().width and 8 <= y <= 8 + card.get_rect().height:
                        click_type = 'flower'
                        sf = SunFlower()
                        if int(sun_num) > 0 and int(sun_num) >= sf.money:
                            click_images.append(sf)
                            is_pick = True
                    if 436 <= x <= 436 + card.get_rect().width and 7 <= y <= 7 + card.get_rect().height:
                        click_type = 'nut'
                        wn = WallNut()
                        if int(sun_num) > 0 and int(sun_num) >= wn.money:
                            click_images.append(wn)
                            is_pick = True
                else:
                    # 判断鼠标点击位置，并且给对应位置添加对应植物
                    if event.button == 1 and zone.is_plant_zone(x, y) and zone.getIndex(x, y):
                        index_x, index_y = zone.getIndex(x, y)
                        if not zone.plant_info[index_y][index_x]:
                            zone.plant_info[index_y][index_x] = 1
                            if click_type == 'pea':
                                pr = Peashooter()
                                sun_num = str(int(sun_num) - pr.money)
                                fontImg = font.render(sun_num, True, (0, 0, 0))
                                pr.zone = zone.getGridPos(index_x, index_y)
                                pea_list.append(pr)
                                zombie_enemy_list.append(pr)
                                click_images.clear()
                            if click_type == 'flower':
                                flower = SunFlower()
                                sun_num = str(int(sun_num) - flower.money)
                                fontImg = font.render(sun_num, True, (0, 0, 0))
                                flower.zone = zone.getGridPos(index_x, index_y)
                                flower_list.append(flower)
                                zombie_enemy_list.append(flower)
                                click_images.clear()
                            if click_type == 'nut':
                                nut = WallNut()
                                sun_num = str(int(sun_num) - nut.money)
                                fontImg = font.render(sun_num, True, (0, 0, 0))
                                nut.zone = zone.getGridPos(index_x, index_y)
                                nut_list.append(nut)
                                zombie_enemy_list.append(nut)
                                click_images.clear()
                            is_pick = False
                    # 判断鼠标右击时，清楚选中的植物
                    if event.button == 3:
                        click_images.clear()
                        is_pick = False
        # 绘制背景
        screen.blit(backgroup, (0, 0))
        # 卡槽
        screen.blit(card_slot, (250, 0))
        # 卡片
        screen.blit(card, (329, 7))
        screen.blit(cardTwo, (383, 8))
        screen.blit(cardThree, (436, 7))
        # 阳光数量
        screen.blit(fontImg, (280, 60))
        # 设置图片循环的最大下标
        if index > 15:
            index = 0

        # 加载
        for click in click_images:
            screen.blit(click.images[0], (x, y))
        # 加载豌豆
        for per in pea_list:
            per_x = per.zone[0]
            per_y = per.zone[1]
            index_x, index_y = zone.getIndex(per_x, per_y)
            if index % 99 == 1:
                # 判断是否需要生产子弹，当僵尸位置在对应豌豆后，或者不在同一行时，不需要产生子弹
                is_bullet = False
                for zombie in zombie_list:
                    if zombie.is_live and zombie.rect.centerx > per_x:
                        zm_x, zm_y = zone.getIndex(zombie.rect.centerx, zombie.rect.centery)
                        if zm_y == index_y:
                            is_bullet = True
                            break
                if is_bullet:
                    bullet_list.append(per.shot())
                elif per.bullet:
                    per.bullet.status = False
            if per.is_live:
                screen.blit(per.images[index % per.size], per.zone)
            else:
                zone.plant_info[index_y][index_x] = 0
                pea_list.remove(per)
        # 加载向日葵
        for flower in flower_list:
            if flower.is_live:
                screen.blit(flower.images[index % flower.size], flower.zone)
            else:
                index_x, index_y = zone.getIndex(flower.zone[0], flower.zone[1])
                zone.plant_info[index_y][index_x] = 0
                flower_list.remove(flower)

        # 加载坚果
        for nut in nut_list:
            if nut.is_live:
                screen.blit(nut.images[index % nut.size], nut.zone)
            else:
                index_x, index_y = zone.getIndex(nut.zone[0], nut.zone[1])
                zone.plant_info[index_y][index_x] = 0
                nut_list.remove(nut)
        # 加载僵尸
        for zombie in zombie_list:
            if zombie.is_live:
                zombie.change_zombie()
                screen.blit(zombie.images[index % zombie.size], zombie.rect)
                zombie.move()
                zombie.eat(zombie_enemy_list)
            else:
                zombie_list.remove(zombie)

        # 加载子弹
        for bullet in bullet_list:
            if bullet.status:
                screen.blit(bullet.image, bullet.rect)
                bullet.move()
                bullet.hit(zombie_list)
            else:
                bullet_list.remove(bullet)

        # 加载太阳
        for sun in sun_list:
            if sun.status:
                screen.blit(sun.images[index % sun.size], sun.rect)
                sun.down()
            else:
                sun_list.remove(sun)

        pygame.display.flip()
        # 刷新率
        block.tick(15)
        index += 1


if __name__ == '__main__':
    main()
