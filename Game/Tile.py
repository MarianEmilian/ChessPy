"""
A tile is a single space on the board, white or black,
which can be occupied by a piece
"""


class Tile:
    def __init__(self, color, occupied, piece):
        self.color = color
        self.occupied = occupied
        self.piece = piece
