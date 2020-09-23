import copy

import pyglet
from pyglet import shapes

import GameState
from Piece import *


def getLocationName(x, y):
    return (chr(x + ord('a'))) + chr(y + ord('0'))

def getCoordinates(name):
    return (ord(name[0]) - ord('a')), (ord(name[1]) - ord('0')), (ord(name[2]) - ord('a')), (ord(name[3]) - ord('0'))


class Board:
    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

        self.currentTurn = 'w'

        self.tiles = []
        darkColor = (209, 139, 71)
        lightColor = (255, 206, 158)

        for x in range(8):
            for y in range(8):
                color = darkColor if (y + x * 8 + x) % 2 == 0 else lightColor
                self.tiles.append(shapes.Rectangle(x * 80, y * 80, 80, 80, color))

        self.initBoard()

    def initBoard(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
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
        self.board[4][0] = King('w', 4, 0, pyglet.image.load("Res/WKing.png"), self)
        

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
        self.board[4][7] = King('b', 4, 7, pyglet.image.load("Res/BKing.png"), self)

    def load(self, path):
        self.initBoard()

        with open("Res/GameLog.txt", "r") as f:
            lines = f.readlines()
        with open("Res/GameLog.txt", "w") as f:
            pass

        for line in lines:
            if len(line) == 5:
                fx, fy, tx, ty = getCoordinates(line)
                self.moveFromTo(fx, fy, tx, ty)

    def testIfInCheckAfterMove(self, fx, fy, tx, ty):
        tcopy = copy.copy(self.board[tx][ty])
        fcopy = copy.copy(self.board[fx][fy])
        self.board[tx][ty] = self.board[fx][fy]
        self.board[tx][ty].moveTo(tx, ty)
        self.board[fx][fy] = None

        kingIsInCheck = self.kingInCheck(self.currentTurn)
            
        self.board[tx][ty] = tcopy 
        self.board[fx][fy] = fcopy 

        return kingIsInCheck

    def moveFromTo(self, fx, fy, tx, ty):
        
        # Only allow if king not in check or move will block
        if self.kingInCheck(self.currentTurn):
            pass
            # TODO if self.testIfInCheckAfterMove(tx, ty, fx, ty):
            # TODO    return False

        typeofeaten = type(self.board[tx][ty])
        
        # player stores a list of all captured pieces -> possibly display?
        self.activePlayer().caputred.append(self.board[tx][ty])

        self.board[tx][ty] = self.board[fx][fy]
        self.board[tx][ty].moveTo(tx, ty)
        self.board[fx][fy] = None

        # store moves to log file -> can be loaded in menu
        with open("Res/GameLog.txt", "a") as f:
            f.write(getLocationName(fx, fy) + getLocationName(tx, ty) + "\n")

        self.nextTurn(typeofeaten)
        
        return True

    def nextTurn(self, typeofeaten):
        if typeofeaten == King: # TODO or self.isCheckmate(self.currentTurn):
            self.initBoard()
            GameState.setActiveScene(3)

        self.currentTurn = 'w' if self.currentTurn == 'b' else 'b'

    def isCheckmate(self, color):
        if not self.kingInCheck(color):
            return False

        kx, ky = (-1, -1)
        for row in self.board:
            for piece in row:
                if piece != None:
                    if piece.color == color and type(piece) == King:
                        kx = piece.x
                        ky = piece.y

        for x, y in self.board[kx][ky].getPossiblePositions(self.board):
            if not self.testIfInCheckAfterMove(tx, ty, fx, ty):
                return False
        return True

    def kingInCheck(self, color):
        threatened = [[False for _ in range(8)] for _ in range(8)]
        kx, ky = (-1, -1)
        for row in self.board:
            for piece in row:
                if piece != None:
                    if piece.color == color and type(piece) == King:
                        kx = piece.x
                        ky = piece.y
                    elif piece.color != color:
                        for pos in piece.getPossiblePositions(self.board):
                            threatened[pos[0]][pos[1]] = True
        
        return threatened[kx][ky]

    def activePlayer(self):
        if self.currentTurn == self.player1.color:
            return self.player1
        return self.player2

    def draw(self):
        for tile in self.tiles:
            tile.draw()

        for row in self.board:
            for piece in row:
                if piece != None:
                    piece.draw()