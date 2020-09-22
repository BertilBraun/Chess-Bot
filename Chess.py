from Piece import *
from Board import *
from GameEventHandler import *

import pyglet

def getLocationName(x, y):
    return (chr(x + ord('a'))) + chr(y + ord('0'))

def getCoordinates(name):
    return ((ord(name[0]) - ord('a')), (ord(name[1]) - ord('0')))

window = pyglet.window.Window(8 * 80, 8 * 80, "Chess", False, pyglet.window.Window.WINDOW_STYLE_DIALOG)

board = Board()
gameHandler = GameEventHandler(board)

@window.event
def on_draw():
    window.clear()
    board.draw()

    for border in gameHandler.boarderOfSelectables:
        border.draw()

def main():

    window.push_handlers(gameHandler)
    pyglet.app.run()

    # print(getLocationName(5, 5))
    # print(getCoordinates("f5"))
    
    # input("Press any key to close...")


if __name__ == "__main__":
    main()