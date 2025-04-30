

class Settings:
    def __init__(self):
        self.screen_width=1920
        self.screen_height=1080
        self.bg_color=(230,230,230)

        #enemy
        self.ai_hp=2000

        #bullet settings
        self.bullet_speed=10
        self.bullet_width=15
        self.bullet_height=3
        self.bullet_color=(60,60,60)
        self.bullet_allowed=5
        self.bullet_2_allowed=5

        #ai bullet speed
        self.ai_bullet_speed=5

        #ship
        self.pl_1_speed=2.5
        self.pl_2_speed=2.5
        self.pl_1_hp=100
        self.pl_2_hp=100
        self.ai_hp=2000