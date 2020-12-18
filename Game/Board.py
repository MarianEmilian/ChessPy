"""
A board is a space with 64 spaces, conventionally alternating black and white. For visual purposes i replaced black with
light blue.
Each space can either contain a piece at a time, or be empty.

"""
import pygame
# used colors
from Utils.Constants import BLACK, WHITE, BLUE
# board dimensions
from Utils.Constants import ROWS, COLS
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER

from Game.Piece import Piece



def draw_board(window):
    window.fill(BLACK)

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

    def hardcode_pieces(self):
        # white pieces
        w_pawn = Piece("Pawn", "white")
        w_rook = Piece("Rook", "white")
        w_knight = Piece("Knight", "white")
        w_queen = Piece("Queen", "white")
        w_bishop = Piece("Bishop", "white")
        w_king = Piece("King", "white")

        # black pieces
        b_pawn = Piece("Pawn", "black")
        b_rook = Piece("Rook", "black")
        b_knight = Piece("Knight", "black")
        b_queen = Piece("Queen", "black")
        b_bishop = Piece("Bishop", "black")
        b_king = Piece("King", "black")

        # pawn placement. 8 pawns for each player
        for col in COLS:
            # 2nd row in matrix = 7th row on actual board => black pawns
            row = 1
            b_pawn.row = row
            b_pawn.col = col
            self.board[row][col] = b_pawn
            # 6th row in matrix = 2nd row on actual board => white pawns
            w_pawn.row = row
            w_pawn.col = col
            self.board[row + 5][col] = w_pawn

        # rook placement. 2 for each player
        # black rooks
        self.board[0][0] = self.board[0][7] = b_rook
        self.board[0][0].row = self.board[0][7].row = 0
        self.board[0][0].col = 0
        self.board[0][7].col = 7

        # white rooks
        self.board[7][0] = self.board[7][7] = w_rook
        self.board[7][0].row = self.board[7][7].row = 7
        self.board[7][0].col = 7
        self.board[7][7].col = 7

        # knight placement. 2 for each player
        # black knights
        self.board[0][1] = self.board[0][6] = b_knight
        self.board[0][1].row = self.board[0][6].row = 0
        self.board[0][1].col = 1
        self.board[0][6].col = 6

        # white knights
        self.board[7][1] = self.board[7][6] = w_knight
        self.board[7][0].row = self.board[7][7].row = 7
        self.board[7][1].col = 1
        self.board[7][6].col = 6

        # bishop placement. 2 for each player
        # black bishop
        self.board[0][2] = self.board[0][5] = b_bishop
        self.board[0][2].row = self.board[0][5].row = 0
        self.board[0][2].col = 2
        self.board[0][5].col = 5

        # black bishop
        self.board[7][2] = self.board[7][5] = w_bishop
        self.board[7][2].row = self.board[7][5].row = 7
        self.board[7][2].col = 2
        self.board[7][5].col = 5

        # queen and king placement. 1 for each player
        # black queen and king
        self.board[0][3] = b_king
        self.board[0][4] = b_queen
        self.board[0][3].row = self.board[0][4].row = 0
        self.board[0][3].col = 3
        self.board[0][4].col = 4

        # white queen and king. Positions are mirrored
        self.board[7][3] = w_queen
        self.board[7][4] = w_king
        self.board[7][3].row = self.board[7][4].row = 7
        self.board[7][3].col = 3
        self.board[7][4].col = 4
