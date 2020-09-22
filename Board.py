import pyglet
from pyglet import shapes

from Piece import *

class Board:
    def __init__(self):

        self.currentTurn = 'w'

        self.tiles = []
        darkColor = (209, 139, 71)
        lightColor = (255, 206, 158)

        for x in range(8):
            for y in range(8):
                color = darkColor if (y + x * 8 + x) % 2 == 0 else lightColor
                self.tiles.append(shapes.Rectangle(x * 80, y * 80, 80, 80, color))

        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initBoard()

    def initBoard(self):
        pawnImg = pyglet.image.load("Res/WPawn.png")
        for i in range(8):
            self.board[i][1] = Pawn('w', i, 1, pawnImg, self)
        rookImg = pyglet.image.load("Res/WRook.png")
        self.board[0][0] = Rook('w', 0, 0, rookImg)
        self.board[7][0] = Rook('w', 7, 0, rookImg)
        knightImg = pyglet.image.load("Res/WKnight.png")
        self.board[1][0] = Knight('w', 1, 0, knightImg)
        self.board[6][0] = Knight('w', 6, 0, knightImg)
        bishopImg = pyglet.image.load("Res/WBishop.png")
        self.board[2][0] = Bishop('w', 2, 0, bishopImg)
        self.board[5][0] = Bishop('w', 5, 0, bishopImg)
        self.board[3][0] = Queen('w', 3, 0, pyglet.image.load("Res/WQueen.png"))
        self.board[4][0] = King('w', 4, 0, pyglet.image.load("Res/WKing.png"))
        

        pawnImg = pyglet.image.load("Res/BPawn.png")
        for i in range(8):
            self.board[i][6] = Pawn('b', i, 6, pawnImg, self)
        rookImg = pyglet.image.load("Res/BRook.png")
        self.board[0][7] = Rook('b', 0, 7, rookImg)
        self.board[7][7] = Rook('b', 7, 7, rookImg)
        knightImg = pyglet.image.load("Res/BKnight.png")
        self.board[1][7] = Knight('b', 1, 7, knightImg)
        self.board[6][7] = Knight('b', 6, 7, knightImg)
        bishopImg = pyglet.image.load("Res/BBishop.png")
        self.board[2][7] = Bishop('b', 2, 7, bishopImg)
        self.board[5][7] = Bishop('b', 5, 7, bishopImg)
        self.board[3][7] = Queen('b', 3, 7, pyglet.image.load("Res/BQueen.png"))
        self.board[4][7] = King('b', 4, 7, pyglet.image.load("Res/BKing.png"))

    def nextTurn(self, typeofeaten):
        self.currentTurn = 'w' if self.currentTurn == 'b' else 'b'

        if typeofeaten == King:
            self.initBoard()

        # TODO Log to file

    def kingInCheck(self, color):
        # TODO Implement
        return False

    def draw(self):
        for tile in self.tiles:
            tile.draw()

        for row in self.board:
            for piece in row:
                if piece != None:
                    piece.draw()