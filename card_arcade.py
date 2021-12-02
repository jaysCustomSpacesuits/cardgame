import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Cardgame"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class MyGame(arcade.Window):
    # Main application class
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.JET)

    def on_draw(self):
        # Render the screen

        # Clears what was drawn last frame back to background color
        # Should be called before drawing to screen
        arcade.start_render()

        arcade.draw_text("Welcome to Cardgame!",
                         0,
                         SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5,
                         arcade.color.CHARTREUSE,
                         DEFAULT_FONT_SIZE * 2,
                         width = SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future Narrow")

        arcade.draw_text()


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()