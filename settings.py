class Settings():
    # 存储星球大战的所有设置的类

    def __init__(self):
        #初始化游戏的设置
        # 屏幕大小设置
        self.screen_width = 1200
        self.screen_heigt = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 1
        self.bullet_width = 7
        self.bullet_height = 17
        self.bullet_color = (60,60,60)