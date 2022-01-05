class AdolfHitler:
    def __init__(self):
        self.health = 400
        self.troop_list = []
        self.tank_list = []
        self.population = []
        self.jews = []
        self.locations = []
        self.score_card = 0
        self.current_city = 0
        self.possible_locations = ["moscow",
                                   "london",
                                   "paris",
                                   "washington",
                                   "liverpool",
                                   "stalingrad",
                                   "leningrad",
                                   "glasgow"]

        self.nuclear_arsenal = ["nuke",
                                "nuke",
                                "nuke",
                                "nuke"]

class GermanSoldier:
    def __init__(self):
        self.heatlh = 400
        self.hunger = 100
        self.thirst = 50
        self.energy = 400

class GermanCivilian:
    def __init__(self):
        self.health = 250