from GameState import activeScene
from GameEventHandler import *

import pyglet

window = pyglet.window.Window(8 * 80, 8 * 80, "Chess", False, pyglet.window.Window.WINDOW_STYLE_DIALOG)

gameHandler = GameEventHandler()

@window.event
def on_draw():
    window.clear()
    activeScene().render()
    
def main():
    window.push_handlers(gameHandler)
    pyglet.app.run()


if __name__ == "__main__":
    main()