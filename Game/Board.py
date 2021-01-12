"""
A board is composed from 64 spaces, conventionally alternating black and white. For visual purposes i replaced black with
light blue.
Each space can either contain a piece at a time, or be empty.
"""

import pygame
# used colors
from Utils.Constants import WHITE, BLUE
# board dimensions
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER
from Game.Piece import Piece
from Game.PieceMovement import *


class Board:
    def __init__(self):
        self.board = [[0 for i in range(ROWS)] for j in range(COLS)]
        self._hardcode_pieces()
        self.update_moves()

    def get_piece(self, row, col):
        print(self.board[row][col])
        return self.board[row][col]

    def _draw_pieces(self, window):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].calc_coord()
                    self.board[row][col].draw(window)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.update_piece(row, col)

    def draw(self, window):
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
        self._draw_pieces(window)

    def update_valid_moves(self, piece):
        # pawn moves
        if piece.name == "Pawn":
            piece.valid_moves = pawn_moves(self.board, piece)
        # rook moves
        if piece.name == "Rook":
            piece.valid_moves = rook_moves(self.board, piece)
        # knight moves
        if piece.name == "Knight":
            piece.valid_moves = knight_moves(self.board, piece)
        # bishop moves
        if piece.name == "Bishop":
            piece.valid_moves = bishop_moves(self.board, piece)
        # queen moves
        if piece.name == "Queen":
            piece.valid_moves = queen_moves(self.board, piece)
        # king moves
        if piece.name == "King":
            piece.valid_moves = king_moves(self.board, piece)

    def update_moves(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.update_valid_moves(self.board[row][col])

    def _hardcode_pieces(self):

        # pawn placement. 8 pawns for each player
        for col in range(COLS):
            # black pawns
            row = 1
            self.board[row][col] = Piece("Pawn", "black", row, col)
            # white pawns
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
        # black queen placement
        self.board[0][3] = Piece("Queen", "black", 0, 3)
        # black king placement
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
        # white queen placement
        self.board[7][3] = Piece("Queen", "white", 7, 3)
        # white king placement
        self.board[7][4] = Piece("King", "white", 7, 4)

    def print_board(self):
        board_str = ""
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] != 0:
                    board_str = board_str + self.board[i][j].name + " "
                else:
                    board_str = board_str + "0 "
            board_str = board_str + "\n"
        print(board_str)
