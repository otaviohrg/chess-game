from .piece import Piece
from sample.models import piece

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.symbol = 'n'

    def generate_moves(self, board):
        self.written_moves = []
        self.moves = []
        vectors = [(1,2),(2,1),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]
        for (a,b) in vectors:
            if self.x+a <= 7 and self.x+a >= 0 and self.y+b <= 7 and self.y+b >= 0:
                if not board[self.x+a][self.y+b].occupied:
                    self.written_moves.append("N"+chr(ord('`')+self.y+b+1)+str(self.x+a+1))
                    self.moves.append((self.x+a,self.y+b))
                elif board[self.x+a][self.y+b].piece.color != self.color:
                    self.written_moves.append("Nx"+chr(ord('`')+self.y+b+1)+str(self.x+a+1))
                    self.moves.append((self.x+a,self.y+b))
