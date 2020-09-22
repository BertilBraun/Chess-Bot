
class Player:
    def __init__(self, color):
        self.color = color

    def move(self, board):
        pass
    
class User(Player):
    def __init__(self, color):
        super().__init__(color)
    
    def move(self, board):
        # user input and move a piece
        pass


class Bot(Player):
    def __init__(self, color):
        super().__init__(color)
    
    def move(self, board):
        # calculate next step
        pass

    def evaluate(self, board):
        # evaluate board state
        pass