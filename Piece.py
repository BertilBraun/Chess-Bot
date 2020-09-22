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

    def draw(self):
        if self.drawAt != None:
            self.sprite.position = self.drawAt
        else:
            self.sprite.position = (self.x * 80, self.y * 80)
        self.sprite.draw();

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def getPossiblePositions(self):
        pass

    def possiblePos(self, x, y, board):
        if not insideBoard(x, y):
            return False
        return board[x][y] == None or board[x][y].color != self.color

    def otherColor(self):
        return 'w' if self.color == 'w' else 'b'

class Pawn(Piece):
    def __init__(self, color, x, y, image, board):
        super().__init__(color, x, y, image)
        self.moved = False
        self.board = board
        
    def moveTo(self, x, y):
        super().moveTo(x, y)
        self.moved = True

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

    def getPossiblePositions(self, board):
        positions = []

        directrion = 1 if self.color == 'w' else -1

        if self.possiblePos(self.x, self.y + directrion, board):
            positions.append((self.x, self.y + directrion))
            if self.possiblePos(self.x, self.y + 2 * directrion, board) and not self.moved:
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
        while self.possiblePos(x, self.y, board):
            positions.append((x, self.y))
            x += 1
            
        x = self.x - 1
        while self.possiblePos(x, self.y, board):
            positions.append((x, self.y))
            x -= 1

        y = self.y + 1
        while self.possiblePos(self.x, y, board):
            positions.append((self.x, y))
            y += 1
            
        y = self.y - 1
        while self.possiblePos(self.x, y, board):
            positions.append((self.x, y))
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
        while self.possiblePos(self.x + offset, self.y + offset, board):
            positions.append((self.x + offset, self.y + offset))
            offset += 1
            
        offset = 1
        while self.possiblePos(self.x - offset, self.y + offset, board):
            positions.append((self.x - offset, self.y + offset))
            offset += 1

        offset = 1
        while self.possiblePos(self.x + offset, self.y - offset, board):
            positions.append((self.x + offset, self.y - offset))
            offset += 1

        offset = 1
        while self.possiblePos(self.x - offset, self.y - offset, board):
            positions.append((self.x - offset, self.y - offset))
            offset += 1

        return positions
    
class Queen(Piece):
    def __init__(self, color, x, y, image):
        super().__init__(color, x, y, image)
        
    def getPossiblePositions(self, board):
        positions = []

        x = self.x + 1
        while self.possiblePos(x, self.y, board):
            positions.append((x, self.y))
            x += 1
            
        x = self.x - 1
        while self.possiblePos(x, self.y, board):
            positions.append((x, self.y))
            x -= 1

        y = self.y + 1
        while self.possiblePos(self.x, y, board):
            positions.append((self.x, y))
            y += 1
            
        y = self.y - 1
        while self.possiblePos(self.x, y, board):
            positions.append((self.x, y))
            y -= 1
            
        offset = 1
        while self.possiblePos(self.x + offset, self.y + offset, board):
            positions.append((self.x + offset, self.y + offset))
            offset += 1
            
        offset = 1
        while self.possiblePos(self.x - offset, self.y + offset, board):
            positions.append((self.x - offset, self.y + offset))
            offset += 1

        offset = 1
        while self.possiblePos(self.x + offset, self.y - offset, board):
            positions.append((self.x + offset, self.y - offset))
            offset += 1

        offset = 1
        while self.possiblePos(self.x - offset, self.y - offset, board):
            positions.append((self.x - offset, self.y - offset))
            offset += 1

        return positions

class King(Piece):
    def __init__(self, color, x, y, image):
        super().__init__(color, x, y, image)
        
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

        return positions