import arcade
import east_euro_city_sprite
import east_pacific_city_sprite
import random
import text_adventure_files
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SPRITE_SCALING = 0.5

"""Movement variable is open-ended just so that user can go their own speed"""
question = False
while not question:
    try:
        MOVEMENT_SPEED = int(input("How fast would you like to move?: "))
        question = True
    except:
        print("You are supposed to input a Number!!!!!")

class GeorgyZhukov():
    def __init__(self):
        self.health = 500
        self.energy = 100
        self.hunger = 0
        self.thirst = 0
        self.scorecard = 0
        self.armada = []
        self.locations = []

class WorldWarTwo(arcade.Window):
    def __init__(self, width, height):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "World War Two")





