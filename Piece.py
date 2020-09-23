import pyglet

def insideBoard(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

class Piece:
    def __init__(self, color, x, y, image):
        self.color = color
        self.x = x
        self.y = y
        self.sprite = pyglet.sprite.Sprite(img=image, x=x * 80, y=y * 80)
        self.sprite.scale = 0.08
        self.drawAt = None
        self.moved = False

    def draw(self):
        if self.drawAt != None:
            self.sprite.position = self.drawAt
        else:
            self.sprite.position = (self.x * 80, self.y * 80)
        self.sprite.draw();

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.moved = True

    def getPossiblePositions(self):
        pass

    def possiblePos(self, x, y, board):
        if not insideBoard(x, y):
            return False
        return board[x][y] == None or board[x][y].color != self.color

    def tryAddPosition(self, x, y, board, positions):
        if self.possiblePos(x, y, board):
            positions.append((x, y))
            return board[x][y] == None
        else:
            return False

    def otherColor(self):
        return 'w' if self.color == 'w' else 'b'

class Pawn(Piece):
    def __init__(self, color, x, y, image, board):
        super().__init__(color, x, y, image)
        self.board = board
        
    def moveTo(self, x, y):
        super().moveTo(x, y)

        if self.color == 'w' and y == 7:
            self.board.board[x][y] = Queen(self.color, x, y, pyglet.image.load("Res/WQueen.png"))
            self.drawAt = (-100, -100)
        elif self.color == 'b' and y == 0:
            self.board.board[x][y] = Queen(self.color, x, y, pyglet.image.load("Res/BQueen.png"))
            self.drawAt = (-100, -100)

    def isEnemy(self, x, y, board):
        if not insideBoard(x, y):
            return False
        return board[x][y] != None and board[x][y].color != self.color
    
    def isEmpty(self, x, y, board):
        if not insideBoard(x, y):
            return False
        return board[x][y] == None

    def getPossiblePositions(self, board):
        positions = []

        directrion = 1 if self.color == 'w' else -1

        if self.isEmpty(self.x, self.y + directrion, board):
            positions.append((self.x, self.y + directrion))
            if self.isEmpty(self.x, self.y + 2 * directrion, board) and not self.moved:
                positions.append((self.x, self.y + 2 * directrion))
                
        if self.isEnemy(self.x - 1, self.y + directrion, board):
            positions.append((self.x - 1, self.y + directrion))
            
        if self.isEnemy(self.x + 1, self.y + directrion, board):
            positions.append((self.x + 1, self.y + directrion))

        return positions

class Rook(Piece):
    def __init__(self, color, x, y, image):
        super().__init__(color, x, y, image)
        
    def getPossiblePositions(self, board):
        positions = []

        x = self.x + 1
        while self.tryAddPosition(x, self.y, board, positions):
            x += 1
            
        x = self.x - 1
        while self.tryAddPosition(x, self.y, board, positions):
            x -= 1

        y = self.y + 1
        while self.tryAddPosition(self.x, y, board, positions):
            y += 1
            
        y = self.y - 1
        while self.tryAddPosition(self.x, y, board, positions):
            y -= 1

        return positions
    
class Knight(Piece):
    def __init__(self, color, x, y, image):
        super().__init__(color, x, y, image)
        
    def getPossiblePositions(self, board):
        positions = []

        if self.possiblePos(self.x + 1, self.y + 2, board):
            positions.append((self.x + 1, self.y + 2))
        if self.possiblePos(self.x + 2, self.y + 1, board):
            positions.append((self.x + 2, self.y + 1))
        if self.possiblePos(self.x + 2, self.y - 1, board):
            positions.append((self.x + 2, self.y - 1))
        if self.possiblePos(self.x + 1, self.y - 2, board):
            positions.append((self.x + 1, self.y - 2))
        if self.possiblePos(self.x - 1, self.y - 2, board):
            positions.append((self.x - 1, self.y - 2))
        if self.possiblePos(self.x - 2, self.y - 1, board):
            positions.append((self.x - 2, self.y - 1))
        if self.possiblePos(self.x - 2, self.y + 1, board):
            positions.append((self.x - 2, self.y + 1))
        if self.possiblePos(self.x - 1, self.y + 2, board):
            positions.append((self.x - 1, self.y + 2))

        return positions
    
class Bishop(Piece):
    def __init__(self, color, x, y, image):
        super().__init__(color, x, y, image)
        
    def getPossiblePositions(self, board):
        positions = []

        offset = 1
        while self.tryAddPosition(self.x + offset, self.y + offset, board, positions):
            offset += 1
            
        offset = 1
        while self.tryAddPosition(self.x - offset, self.y + offset, board, positions):
            offset += 1

        offset = 1
        while self.tryAddPosition(self.x + offset, self.y - offset, board, positions):
            offset += 1

        offset = 1
        while self.tryAddPosition(self.x - offset, self.y - offset, board, positions):
            offset += 1

        return positions
    
class Queen(Piece):
    def __init__(self, color, x, y, image):
        super().__init__(color, x, y, image)
        
    def getPossiblePositions(self, board):
        positions = []

        
        offset = 1
        while self.tryAddPosition(self.x + offset, self.y + offset, board, positions):
            offset += 1
            
        offset = 1
        while self.tryAddPosition(self.x - offset, self.y + offset, board, positions):
            offset += 1

        offset = 1
        while self.tryAddPosition(self.x + offset, self.y - offset, board, positions):
            offset += 1

        offset = 1
        while self.tryAddPosition(self.x - offset, self.y - offset, board, positions):
            offset += 1

        x = self.x + 1
        while self.tryAddPosition(x, self.y, board, positions):
            x += 1
            
        x = self.x - 1
        while self.tryAddPosition(x, self.y, board, positions):
            x -= 1

        y = self.y + 1
        while self.tryAddPosition(self.x, y, board, positions):
            y += 1
            
        y = self.y - 1
        while self.tryAddPosition(self.x, y, board, positions):
            y -= 1

        return positions

class King(Piece):
    def __init__(self, color, x, y, image, board):
        super().__init__(color, x, y, image)
        self.board = board
        
    def moveTo(self, x, y):

        if not self.moved:
            if x == 2:
                self.board.board[3][y] = self.board.board[0][y]
                self.board.board[3][y].moveTo(3, y)
                self.board.board[0][y] = None
            elif x == 6:
                self.board.board[5][y] = self.board.board[7][y]
                self.board.board[5][y].moveTo(5, y)
                self.board.board[7][y] = None

        super().moveTo(x, y)

    def emptyPos(self, xoff):
        if not insideBoard(self.x + xoff, self.y):
            return False
        return self.board.board[self.x + xoff][self.y] == None
    
    def notMoved(self, xoff):
        if not insideBoard(self.x + xoff, self.y):
            return False
        if self.board.board[self.x + xoff][self.y] == None:
            return False
        return not self.board.board[self.x + xoff][self.y].moved

    def getPossiblePositions(self, board):
        positions = []
        
        if self.possiblePos(self.x + 1, self.y + 0, board):
            positions.append((self.x + 1, self.y + 0))
        if self.possiblePos(self.x + 1, self.y + 1, board):
            positions.append((self.x + 1, self.y + 1))
        if self.possiblePos(self.x + 0, self.y + 1, board):
            positions.append((self.x + 0, self.y + 1))
        if self.possiblePos(self.x - 1, self.y + 1, board):
            positions.append((self.x - 1, self.y + 1))
        if self.possiblePos(self.x - 1, self.y + 0, board):
            positions.append((self.x - 1, self.y + 0))
        if self.possiblePos(self.x - 1, self.y - 1, board):
            positions.append((self.x - 1, self.y - 1))
        if self.possiblePos(self.x + 0, self.y - 1, board):
            positions.append((self.x + 0, self.y - 1))
        if self.possiblePos(self.x + 1, self.y - 1, board):
            positions.append((self.x + 1, self.y - 1))
            
        if not self.moved:
            if self.emptyPos(1) and self.emptyPos(2) and self.notMoved(3):
                positions.append((self.x + 2, self.y))
            if self.emptyPos(-1) and self.emptyPos(-2) and self.emptyPos(-3) and self.notMoved(-4):
                positions.append((self.x - 2, self.y))

        return positions