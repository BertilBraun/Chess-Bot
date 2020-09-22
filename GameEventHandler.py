
import pyglet
from pyglet.window import mouse

class GameEventHandler:
    def __init__(self, board):
        self.boarderOfSelectables = []
        self.board = board
        self.positions = []
        self.selected = None

    def Rect(self, x, y, width, color):
        self.boarderOfSelectables.append(pyglet.shapes.Line(x, y, x + 80, y, width, color))
        self.boarderOfSelectables.append(pyglet.shapes.Line(x, y, x, y + 80, width, color))
        self.boarderOfSelectables.append(pyglet.shapes.Line(x, y + 80, x + 80, y + 80, width, color))
        self.boarderOfSelectables.append(pyglet.shapes.Line(x + 80, y, x + 80, y + 80, width, color))

    def on_key_press(self, symbol, modifiers):
        #print 'Key pressed in game'
        return True

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):

        if self.selected != None:
            self.selected.drawAt = (x - 40, y - 40)

    def on_mouse_release(self, x, y, button, modifiers):

        if button == mouse.LEFT:           

            if self.selected == None:
                return

            gx = x // 80
            gy = y // 80

            if (gx, gy) in self.positions:
                if self.board.board[gx][gy] != None:
                    # TODO destroy board[gx][gy]
                    pass
                # TODO Only allow if king not in check or move will block
                typeofeaten = type(self.board.board[gx][gy])
                self.board.board[self.selected.x][self.selected.y] = None
                self.board.board[gx][gy] = self.selected
                self.selected.moveTo(gx, gy)
                self.board.nextTurn(typeofeaten)
                
            self.selected.drawAt = None
            self.selected = None
            self.boarderOfSelectables.clear()
            

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.boarderOfSelectables.clear()

            self.selected = self.board.board[x // 80][y // 80]
            if self.selected == None:
                return

            if self.selected.color != self.board.currentTurn:
                self.selected = None
                return

            self.positions = self.selected.getPossiblePositions(self.board.board)
        
            for pos in self.positions:
                self.Rect(pos[0] * 80, pos[1] * 80, 4, (0, 0, 0))
        
            self.Rect((x // 80) * 80, (y // 80) * 80, 3, (100, 100, 100))