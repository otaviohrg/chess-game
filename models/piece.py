class Piece():
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.moves = []
        self.written_moves = []

    def print_moves(self):
        for i in self.written_moves:
            print(i, end="\n")
