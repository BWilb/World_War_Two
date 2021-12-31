import text_adventure_files.adolf_hitler
import arcade
import east_euro_city_sprite
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SPRITE_SCALING = 0.25

"""Movement variable is open-ended just so that user can go their own speed"""
"""question = False
while not question:
    try:
        MOVEMENT_SPEED = int(input("How fast would you like to move?: "))
        question = True
    except:
        print("You are supposed to input a Number!!!!!")"""

class GeorgyZhukov(arcade.Sprite):
    def __init__(self, file, sprite_scaling):
        super().__init__(file, sprite_scaling)
        self.health = 500
        self.energy = 100
        self.hunger = 0
        self.thirst = 0
        self.scorecard = 0
        self.armada = []
        self.locations = []

class WorldWarTwo(arcade.Window):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """initialization method"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "World War Two")
        """self.zhukov = None
        #self.hitler = text_adventure_files.adolf_hitler.AdolfHitler()
        #self.city = east_euro_city_sprite.Europa()
        self.player_list = None
        self.physics_engine = None"""

    """def setup(self):
        self.player_list = arcade.SpriteList()
        self.zhukov = GeorgyZhukov("marshal-zhukov.png", SPRITE_SCALING)
        self.zhukov.center_x = SCREEN_WIDTH // 2
        self.zhukov.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.zhukov)"""

    """Create individual cities for city object"""
    #self.physics_engine = arcade.PhysicsEngineSimple(self.zhukov)
    """add city ground list to second parameter of physics engine"""

    def on_draw(self):
        """Drawing method"""
        arcade.start_render()
        """Create a constraint based off of the amount of germans at hitler's disposal"""
        arcade.draw_lrtb_rectangle_filled(0,
                                          SCREEN_WIDTH,
                                          SCREEN_HEIGHT,
                                          0,
                                          arcade.csscolor.GOLD)


        """Start drawing the cities and their backgrounds here"""
        #self.player_list.draw()

"""def on_update(self, delta_time: float):
        self.player_list.update()
        self.zhukov.update()
        #self.hitler.update()
        add the logic for any scoring for both sides"""


def main():
    """main method
    placed outside of game's scope, so it can call to game
    """
    game = WorldWarTwo(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.on_draw()
    arcade.run()

if __name__ == "__main__":
    main()