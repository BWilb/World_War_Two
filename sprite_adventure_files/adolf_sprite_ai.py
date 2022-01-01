import arcade
class AdolfHitler(arcade.Sprite):
    def __init__(self, file, sizing):
        super().__init__(file, sizing)
        self.health = 600
        self.german_list = []
        self.location = 0
        self.score = 0

class Germans(arcade.Sprite):
    def __init__(self, file, scale):
        super().__init__(file, scale)
        self.health = 250