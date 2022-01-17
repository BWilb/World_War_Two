class WinstonChurchill:
    def __init__(self):
        self.health = 1000
        self.troop_list = []
        self.tank_list = []
        self.locations = []
        self.current_location = 0

class FDR:
    def __init__(self):
        self.health = 450
        """FDR has lowest health, due to him being crippled"""
        self.troop_list = []
        self.tank_list = []
        self.locations = []
        self.current_location = 0
        self.nukes = ["nuke",
                      "nuke"]

class CharlesDeGaulle:
    def __init__(self):
        self.health = 500
        self.troop_list = []
        self.tank_list = []
        self.locations = []
        self.current_location = 0