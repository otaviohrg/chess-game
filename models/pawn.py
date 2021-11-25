from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.symbol = 'p'

    def generate_moves(self, board):
        return