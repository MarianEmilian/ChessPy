"""
A board is a space with 64 spaces, conventionally alternating black and white. For visual purposes i replaced black with
light blue.
Each space can either contain a piece at a time, or be empty.
"""

import pygame
# used colors
from Utils.Constants import WHITE, BLUE
# board dimensions
from Utils.Constants import ROWS, COLS
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER
from Game.Piece import Piece


def draw_board(window):
    # drawing the chess board pattern
    for row in range(ROWS):
        start = row % 2
        # white rectangles
        for col in range(start, COLS, 2):
            pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE + BOARD_BUFFER,  # the place of the tile
                                             col * SQUARE_SIZE + BOARD_BUFFER,
                                             SQUARE_SIZE,  # the size of the tile
                                             SQUARE_SIZE)
                             )
        # cyan rectangles
        # an artifice to alternate the squares
        if start == 0:
            start = start + 1
        else:
            start = start - 1
        for col in range(start, ROWS, 2):
            pygame.draw.rect(window, BLUE, (row * SQUARE_SIZE + BOARD_BUFFER,  # the place of the tile
                                            col * SQUARE_SIZE + BOARD_BUFFER,
                                            SQUARE_SIZE,  # the size of the tile
                                            SQUARE_SIZE)
                             )


class Board:
    def __init__(self):
        self.board = [[0 for i in range(ROWS)] for j in range(COLS)]

    def draw_pieces(self, window):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].calc_coord()
                    self.board[row][col].draw(window)

    def hardcode_pieces(self):

        # pawn placement. 8 pawns for each player
        for col in range(COLS):
            # 2nd row in matrix = 7th row on actual board => black pawns
            row = 1
            self.board[row][col] = Piece("Pawn", "black", row, col)
            # 6th row = 1st row on board
            row = row + 5
            self.board[row][col] = Piece("Pawn", "white", row, col)

        # black pieces placement
        # rook placement
        self.board[0][0] = Piece("Rook", "black", 0, 0)
        self.board[0][7] = Piece("Rook", "black", 0, 7)
        # knight placement
        self.board[0][1] = Piece("Knight", "black", 0, 1)
        self.board[0][6] = Piece("Knight", "black", 0, 6)
        # bishop placement
        self.board[0][2] = Piece("Bishop", "black", 0, 2)
        self.board[0][5] = Piece("Bishop", "black", 0, 5)
        # queen placement
        self.board[0][3] = Piece("Queen", "black", 0, 3)
        # king placement
        self.board[0][4] = Piece("King", "black", 0, 4)

        # white pieces placement
        # rook placement
        self.board[7][0] = Piece("Rook", "white", 7, 0)
        self.board[7][7] = Piece("Rook", "white", 7, 7)
        # knight placement
        self.board[7][1] = Piece("Knight", "white", 7, 1)
        self.board[7][6] = Piece("Knight", "white", 7, 6)
        # bishop placement
        self.board[7][2] = Piece("Bishop", "white", 7, 2)
        self.board[7][5] = Piece("Bishop", "white", 7, 5)
        # queen placement
        self.board[7][4] = Piece("Queen", "white", 7, 3)
        # king placement
        self.board[7][3] = Piece("King", "white", 7, 4)
