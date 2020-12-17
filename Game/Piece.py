"""
A piece is either a pawn, knight, bishop, rook, or queen.
It belongs to a player or another, fact represented by its color.
The piece has a place on the board represented by its row and column
"""
from Utils.Constants import SQUARE_SIZE


class Piece:
    def __init__(self, name, color, row, col):
        self.name = name
        self.color = color
        self.row = row
        self.col = col

        self.x = 0
        self.y = 0

    def calc_xy(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2