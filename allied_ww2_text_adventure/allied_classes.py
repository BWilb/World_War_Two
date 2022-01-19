class WinstonChurchill:
    def __init__(self):
        self.health = 1000
        self.troop_list = []
        self.tank_list = []
        self.locations = []
        self.current_location = 0

class BritishSoldier:
    def __init__(self):
        self.heatlh = 500

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

class AmericanSoldier:
    def __init__(self):
        self.health = 230

class CharlesDeGaulle:
    def __init__(self):
        self.health = 500
        self.troop_list = []
        self.tank_list = []
        self.locations = []
        self.current_location = 0
class FrenchSoldier:
    def __init__(self):
        self.health = 100