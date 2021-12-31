import arcade
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

class Main_Menu(arcade.Window):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, title):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title)
        self.options = ["Main Menu",
                        "1. continue",
                           "2. pause",
                           "3. quit",
                           "4. options"]

    def on_draw(self):
        self.size = 1000
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2,
                                     SCREEN_HEIGHT / 2,
                                     1000,
                                     1000,
                                     arcade.csscolor.GOLD)
        for i in range(len(self.options)):
            if self.options[i].lower() == "main menu":
                arcade.draw_text(self.options[0], (SCREEN_WIDTH / 2 - 100), self.size / 1.25, arcade.csscolor.BLACK, 32)
            else:
                arcade.draw_text(self.options[i], (SCREEN_WIDTH / 2 - 50), self.size / 1.25, arcade.csscolor.BLACK, 16)
            self.size -= 100

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            arcade.finish_render()

def main():
    window = Main_Menu(SCREEN_WIDTH, SCREEN_HEIGHT, "Main Menu")

    arcade.run()