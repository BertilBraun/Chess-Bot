
class Player:
    def __init__(self, color):
        self.color = color
        self.caputred = []

    def move(self, board):
        pass
    
class User(Player):
    def __init__(self, color):
        super().__init__(color)
        self.selected = None
        self.positions = []
    
    def trySelectAt(self, x, y, board):
        
        selected = board.board[x][y]

        if selected == None or selected.color != board.currentTurn:
            return False

        self.selected = selected
        self.positions = self.selected.getPossiblePositions(board.board)
        return True

    def move(self, board):
        # user input and move a piece
        pass


class Bot(Player):
    def __init__(self, color, board):
        super().__init__(color, board)
    
    def move(self, board):
        # calculate next step
        pass

    def evaluate(self, board):
        # evaluate board state
        pass