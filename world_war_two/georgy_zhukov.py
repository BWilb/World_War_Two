class GeorgyZhukov:
    def __init__(self):
        self.health = 300
        self.energy = 100
        self.hunger = 0
        self.thirst = 0
        self.score_card = 0
        self.distance = 0
        self.troop_list = []
        self.tank_list = []
        self.food_list = ["food", "food", "food", "food", "food"]
        self.water_list = ["water", "water", "water", "water", "water"]
        self.population = []
        self.jews = []

class SovietSoldier:
    def __init__(self):
        self.health = 100
        self.energy = 50
        self.hunger = 200
        self.thirst = 200

class SovietCivilian:
    def __init__(self):
        self.health = 100