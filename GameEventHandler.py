
from GameState import activeScene

import pyglet

class GameEventHandler:
    def on_key_press(self, symbol, modifiers):
        activeScene().onKeyPress(symbol, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        activeScene().onMouseDrag(x, y, dx, dy, buttons, modifiers)


    def on_mouse_release(self, x, y, button, modifiers):
        activeScene().onMouseRelease(x, y, button, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        activeScene().onMousePress(x, y, button, modifiers)
        