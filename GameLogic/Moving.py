from Game import Piece
from Game import Board


def get_moves(self, board: Board, piece: Piece):
    # Calculates the positions a piece can occupy from the current position, returns a list
    if piece.name == "Pawn":
        # A pawn c
        row = piece.position[0]
        col = piece.position[1]


