import text_adventure_files.adolf_hitler
import adolf_sprite_ai
import arcade
import east_euro_city_sprite
import random

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 850
SPRITE_SCALING = 0.5

"""Movement variable is open-ended just so that user can go their own speed"""
question = False
while not question:
    try:
        MOVEMENT_SPEED = int(input("How fast would you like to move?: "))
        question = True
    except:
        print("You are supposed to input a Number!!!!!")

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
        self.zhukov = None
        self.hitler = adolf_sprite_ai.AdolfHitler("zombie_idle.png", SPRITE_SCALING)
        #self.city = east_euro_city_sprite.Europa()
        self.player_list = arcade.SpriteList()
        self.physics_engine = None
        self.cities = []
        self.current_location = 0

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.zhukov = GeorgyZhukov("georgy_zhukov.png", SPRITE_SCALING)
        self.zhukov.center_x = SCREEN_WIDTH // 2
        self.zhukov.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.zhukov)
        """beginning of appending the list of european cities to the game"""
        self.city = east_euro_city_sprite.city_one()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_two()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_three()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_four()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_five()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_six()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_seven()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_eight()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_nine()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_ten()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_eleven()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_twelve()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_thirteen()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_fourteen()
        self.cities.append(self.city)

        self.city = east_euro_city_sprite.city_fifteen()
        self.cities.append(self.city)

        """Create individual cities for city object"""
        self.physics_engine = arcade.PhysicsEngineSimple(self.zhukov, self.cities[self.current_location].floor_list)
        """add city ground list to second parameter of physics engine"""

    def on_draw(self):
        """Drawing method"""
        arcade.start_render()
        if len(self.hitler.german_list) > 0 or self.zhukov.health > 0:
            """Create a constraint based off of the amount of germans at hitler's disposal"""
            arcade.draw_lrwh_rectangle_textured(0, 200, SCREEN_WIDTH, SCREEN_HEIGHT, self.cities[self.current_location].background)

        """Start drawing the cities and their backgrounds here"""
        self.player_list.draw()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 200, 0, arcade.csscolor.BLACK)
        arcade.draw_text(f"Zhukov Score: {self.zhukov.scorecard}", 25, 100, arcade.csscolor.RED)
        arcade.draw_text(f"Zhukov health: {self.zhukov.health}", 25, 150, arcade.csscolor.GOLD)
        arcade.draw_text(f"Remaining germans: {len(self.hitler.german_list)}", 700, 100, arcade.csscolor.GOLD)
        arcade.draw_text(f"Remaining soviets: {len(self.zhukov.armada)}", 700, 150)
        arcade.draw_text(f"Hitler's score: {self.hitler.score}", 1325, 100, arcade.csscolor.RED)
        arcade.draw_text(f"Hitler's health: {self.hitler.health}", 1325, 150, arcade.csscolor.WHITE)

    def on_update(self, delta_time: float):
        self.player_list.update()
        if self.zhukov.bottom <= 200:
            self.zhukov.bottom = 200
            """So that Zhukov does not go out of screen with the scoreboard"""
        if self.zhukov.top >= SCREEN_HEIGHT:
            self.zhukov.top = SCREEN_HEIGHT
        self.hitler.update()
        self.physics_engine.update()
        self.city.germans.update()

        """Beginning of checks to see if Zhukov is about to transfer to different city"""
        if self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 0:
            self.current_location = 1
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 1:
            self.current_location = 2
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 2:
            self.current_location = 3
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 3:
            self.current_location = 4
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 4:
            self.current_location = 5
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 5:
            self.current_location = 6
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 6:
            self.current_location = 7
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 7:
            self.current_location = 8
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 8:
            self.current_location = 9
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 9:
            self.current_location = 10
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 10:
            self.current_location = 11
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 11:
            self.current_location = 12
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 12:
            self.current_location = 13
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 13:
            self.current_location = 14
        elif self.zhukov.center_x > SCREEN_WIDTH and self.current_location == 14:
            self.current_location = 15
        """Beginning of checks to see if Zhukov's center is less than zero"""

        if self.zhukov.center_x < 0 and self.current_location == 15:
            self.current_location = 14
        if self.zhukov.center_x < 0 and self.current_location == 14:
            self.current_location = 13
        if self.zhukov.center_x < 0 and self.current_location == 13:
            self.current_location = 12
        if self.zhukov.center_x < 0 and self.current_location == 12:
            self.current_location = 11
        if self.zhukov.center_x < 0 and self.current_location == 11:
            self.current_location = 10
        if self.zhukov.center_x < 0 and self.current_location == 10:
            self.current_location = 9
        if self.zhukov.center_x < 0 and self.current_location == 9:
            self.current_location = 8
        if self.zhukov.center_x < 0 and self.current_location == 8:
            self.current_location = 7
        if self.zhukov.center_x < 0 and self.current_location == 7:
            self.current_location = 6
        if self.zhukov.center_x < 0 and self.current_location == 6:
            self.current_location = 5
        if self.zhukov.center_x < 0 and self.current_location == 5:
            self.current_location = 4
        if self.zhukov.center_x < 0 and self.current_location == 4:
            self.current_location = 3
        if self.zhukov.center_x < 0 and self.current_location == 3:
            self.current_location = 2
        if self.zhukov.center_x < 0 and self.current_location == 2:
            self.current_location = 1
        if self.zhukov.center_x < 0 and self.current_location == 1:
            self.current_location = 0

        """add the logic for any scoring for both sides"""

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.zhukov.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.zhukov.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.zhukov.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.zhukov.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.zhukov.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.zhukov.change_y = 0

def main():
    """main method
    placed outside of game's scope, so it can call to game
    """
    game = WorldWarTwo(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()