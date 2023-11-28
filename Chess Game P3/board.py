from constants import *
from square import Square
from pieces import *

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for column in range(columns)]

        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def calulate_moves(self, piece, row, column):

         def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, column+1),
                (row-1, column+2),
                (row+1, column+2),
                (row+2, column+1),
                (row+2, column-1),
                (row+1, column-2),
                (row-1, column-2),
                (row-2, column-1),
            ]

    for possble_move in possible_moves:
            possible_move_row, possible_move_column = possible_move

            if isinstance(piece, Pawn): 
                pawn_moves()

            elif isinstance(piece, Knight): 
                knight_moves()

            elif isinstance(piece, Bishop): 
                straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])

            elif isinstance(piece, Rook): 
                straightline_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])

            elif isinstance(piece, Queen): 
                straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ])

            elif isinstance(piece, King): 
                king_moves()

    def _create(self):
        for row in range(rows):
            for column in range(columns):
                self.squares[row][column] = Square(row, column)
    
    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        for column in range(columns):
            self.squares[row_pawn][column] = Square(row_pawn, column, Pawn(color))

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
