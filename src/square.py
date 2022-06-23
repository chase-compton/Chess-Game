from piece import *


class Square:
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c',
                 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacols = self.ALPHACOLS[col]

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece != None

    def is_empty(self):
        return not self.has_piece()

    def is_team(self, color):
        return self.has_piece() and self.piece.color == color

    def is_opp(self, color):
        return self.has_piece() and self.piece.color != color

    def empty_or_opp(self, color):
        return self.is_empty() or self.is_opp(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True

    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c',
                     3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col]
