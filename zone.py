# 区域
class Zone:
    # 种植区域初始x坐标
    X_OFFSET_MAP = 235

    # 种植区域初始y坐标
    Y_OFFSET_MAP = 87

    # 每个种植格子的宽度
    X_GRID_SIZE = 82

    # 每个种植格子的高度
    Y_GRID_SIZE = 96

    # 一共9列
    X_GRID_LEN = 9

    # 一共5行
    Y_GRID_LEN = 5

    # 地图不规则，偏移量
    plant_y = [80, 80, 80, 80, 80]
    plant_x = [60, 60, 60, 60, 65, 60, 65, 70, 65]

    def __init__(self):
        # 定义坐标被占用的情况
        self.plant_info = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    # 鼠标点击区域
    def getIndex(self, x, y):
        x -= Zone.X_OFFSET_MAP
        y -= Zone.Y_OFFSET_MAP
        return x // Zone.X_GRID_SIZE, y // Zone.Y_GRID_SIZE


    # 区域的坐标点
    def getGridPos(self, x, y):
        index_x = (x + 1) * Zone.X_GRID_SIZE + Zone.X_OFFSET_MAP - Zone.plant_x[x]
        index_y = (y + 1) * Zone.Y_GRID_SIZE + Zone.Y_OFFSET_MAP - Zone.plant_y[y]
        return index_x, index_y

    # 卡槽区域
    def is_card_slot_zone(self, x, y, width, height):
        if 250 <= x <= 250 + width and 0 <= y <= 0 + height:
            return True
        else:
            return False

    # 种植区域
    def is_plant_zone(self, x, y):
        if (Zone.X_OFFSET_MAP <= x <= (Zone.X_GRID_SIZE * Zone.X_GRID_LEN + Zone.X_OFFSET_MAP)
                and Zone.Y_OFFSET_MAP <= y <= (Zone.Y_GRID_SIZE * Zone.Y_GRID_LEN + Zone.Y_OFFSET_MAP)):
            return True
        else:
            return False


if __name__ == '__main__':
    z = Zone()

