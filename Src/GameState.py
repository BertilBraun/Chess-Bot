from Board import *
from Player import *
from Widgets import *

import pyglet
from pyglet.window import mouse

class State:
    def render(self):
        pass

    def onKeyPress(self, symbol, modifiers):
        pass

    def onMousePress(self, x, y, button, modifiers):
        pass
    
    def onMouseRelease(self, x, y, button, modifiers):
        pass
    
    def onMouseDrag(self, x, y, dx, dy, buttons, modifiers):
        pass
      
def playClick():
    setActiveScene(PLAYING)
    with open("Res/GameLog.txt", "w") as f:
        pass

def loadClick():
    setActiveScene(PLAYING)
    activeScene().board.load("Res/GameLog.txt")

class MainMenu(State):
    def __init__(self):
        self.button = Button("Play", 320, 240, 200, 60, on_click=playClick)
        self.load = Button("Load", 320, 170, 200, 60, on_click=loadClick)
        self.label = Button('Welcome to Chess', 320, 360, 400, 80)

    def render(self):
        gameStateDict[PLAYING].render()
        self.button.draw()
        self.load.draw()
        self.label.draw()
      
    def onMousePress(self, x, y, button, modifiers):
        self.button.onMouseClick(x, y, button)
        self.load.onMouseClick(x, y, button)

class Playing(State):
    def __init__(self):
        self.board = Board(User('w'), User('b'))
        self.boarderOfSelectables = []

    def render(self):
        self.board.draw()

        for border in self.boarderOfSelectables:
            border.draw()   

    def onMousePress(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.boarderOfSelectables.clear()

            if not self.board.activePlayer().trySelectAt(x // 80, y // 80, self.board):
                return
        
            for px, py in self.board.activePlayer().positions:
                self.Rect(px * 80, py * 80, 4, (0, 0, 0))
        
            self.Rect((x // 80) * 80, (y // 80) * 80, 3, (100, 100, 100))
    
    def onMouseRelease(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.board.activePlayer().selected != None:           

            gx = x // 80
            gy = y // 80
            ox = self.board.activePlayer().selected.x
            oy = self.board.activePlayer().selected.y

            if (gx, gy) in self.board.activePlayer().positions:   
                self.board.moveFromTo(ox, oy, gx, gy)                
            
            if self.board.board[ox][oy] != None:
                self.board.board[ox][oy].drawAt = None
            if self.board.board[gx][gy] != None:
                self.board.board[gx][gy].drawAt = None
            self.board.activePlayer().selected = None
            self.boarderOfSelectables.clear()   
            
    def onMouseDrag(self, x, y, dx, dy, buttons, modifiers):
        if self.board.activePlayer().selected != None:
            self.board.activePlayer().selected.drawAt = (x - 40, y - 40)

    def Rect(self, x, y, width, color):
        self.boarderOfSelectables.append(pyglet.shapes.Line(x, y, x + 80, y, width, color))
        self.boarderOfSelectables.append(pyglet.shapes.Line(x, y, x, y + 80, width, color))
        self.boarderOfSelectables.append(pyglet.shapes.Line(x, y + 80, x + 80, y + 80, width, color))
        self.boarderOfSelectables.append(pyglet.shapes.Line(x + 80, y, x + 80, y + 80, width, color))

class Win(State):
    def __init__(self):
        self.button = Button("Play", 320, 240, 200, 70, on_click=playClick)
        self.label = pyglet.text.Label('You Won',
                          font_name='Times New Roman',
                          font_size=36,
                          x=320, y=360,
                          anchor_x='center', anchor_y='center')

    def render(self):
        gameStateDict[PLAYING].render()
        self.button.draw()
        self.label.draw()
      
    def onMousePress(self, x, y, button, modifiers):
        self.button.onMouseClick(x, y, button)

class Lose(State):
    def __init__(self):
        self.button = Button("Play", 320, 240, 200, 70, on_click=playClick)
        self.label = pyglet.text.Label('You Lost',
                          font_name='Times New Roman',
                          font_size=36,
                          x=320, y=360,
                          anchor_x='center', anchor_y='center')

    def render(self):
        gameStateDict[PLAYING].render()
        self.button.draw()
        self.label.draw()
      
    def onMousePress(self, x, y, button, modifiers):
        self.button.onMouseClick(x, y, button)

MAIN_MENU = 1
PLAYING = 2
WIN = 3
LOSE = 4

CURRENT_STATE = MAIN_MENU

gameStateDict = {    
    MAIN_MENU: MainMenu(),
    PLAYING: Playing(),
    WIN: Win(),
    LOSE: Lose()    
}

def activeScene():
    return gameStateDict[CURRENT_STATE]

def setActiveScene(number):
    global CURRENT_STATE
    CURRENT_STATE = number