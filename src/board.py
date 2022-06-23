from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0]for col in range(COLS)]
        self.create()
        self.last_move = None
        self.add_pieces('white')
        self.add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        piece.moved = True

        piece.clear_moves()

        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.moves

    def calc_moves(self, piece, row, col):
        def pawn_moves():
            steps = 1 if piece.moved else 2

            # Vertical
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].is_empty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        move = Move(initial, final)
                        piece.add_move(move)
                    else:
                        break
                else:
                    break

            # Diagonal
            possible_move_row = row+piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_opp(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def knight_moves():
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for move in possible_moves:
                possible_move_row, possible_move_col = move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].empty_or_opp(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def straight_line_moves(incrs):
            for inc in incrs:
                row_inc, col_inc = inc
                possible_move_row = row+row_inc
                possible_move_col = col+col_inc
                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        inital = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(inital, final)

                        if self.squares[possible_move_row][possible_move_col].is_empty():
                            piece.add_move(move)
                        if self.squares[possible_move_row][possible_move_col].is_opp(piece.color):
                            piece.add_move(move)
                            break
                        if self.squares[possible_move_row][possible_move_col].is_team(piece.color):
                            break
                    else:
                        break
                    possible_move_row, possible_move_col = possible_move_row + \
                        row_inc, possible_move_col+col_inc

        def king_moves():
            adjs = [
                (row-1, col),
                (row-1, col+1),
                (row, col+1),
                (row+1, col+1),
                (row+1, col),
                (row+1, col-1),
                (row, col-1),
                (row-1, col-1),
            ]

            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].empty_or_opp(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            straight_line_moves([
                (-1, 1),
                (-1, -1),
                (1, 1),
                (1, -1)
            ])
        elif isinstance(piece, Rook):
            straight_line_moves([
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1)
            ])
        elif isinstance(piece, Queen):
            straight_line_moves([
                (-1, 1),
                (-1, -1),
                (1, 1),
                (1, -1),
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1)
            ])
        elif isinstance(piece, King):
            king_moves()

    def create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        # Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
