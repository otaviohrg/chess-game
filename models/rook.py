from .piece import Piece

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.symbol = 'r'

    def generate_moves(self, board):
        self.written_moves = []
        self.moves = []
        vectors = [(1,0),(0,1),(-1,0),(0,-1)]
        for (a,b) in vectors:
            collide = False
            v = [self.x,self.y]
            while not collide:
                v[0] += a
                v[1] += b
                if v[0] > 7 or v[0] < 0 or v[1] > 7 or v[1] < 0:
                    collide = True
                elif not board[v[0]][v[1]].occupied:
                    self.written_moves.append("R"+chr(ord('`')+v[1]+1)+str(v[0]+1))
                    self.moves.append(v)
                elif board[v[0]][v[1]].piece.color != self.color:
                    self.written_moves.append("Rx"+chr(ord('`')+v[1]+1)+str(v[0]+1))
                    self.moves.append(v)
                    collide = True
                else:
                    collide = True

        