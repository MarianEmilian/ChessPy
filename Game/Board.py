"""
A board is composed from 64 spaces, conventionally alternating black and white. For visual purposes i replaced black with
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


def in_bounds(row, col):
    if row in range(ROWS) and col in range(COLS):
        return True
    return False

def KTK_check(board, row, col):
    # verifies if a king puts in check another one

    # get the other king row col
    for row2 in range(ROWS):
        for col2 in range(COLS):
            if board[row][col].color != board[row2][col2].color and board[row2][col2].name == "king":
                    break
    if abs(row2-row) <= 1 and abs(col2, col) <= 1:
        return True
    return False

class Board:
    def __init__(self):
        self.board = [[0 for i in range(ROWS)] for j in range(COLS)]
        self.hardcode_pieces()

    def get_piece(self, row, col):
        return self.board[row][col]

    def _draw_pieces(self, window):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].calc_coord()
                    self.board[row][col].draw(window)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        print(self.board[piece.row][piece.col], self.board[row][col])
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

    def _pawn_moves(self, piece):
        moves = []
        if piece.color == "black":
            # moves downwards
            # eat piece diagonally to the left or right
            if in_bounds(piece.row + 1, piece.col + 1) \
                    and self.board[piece.row + 1][piece.col + 1] != 0 \
                    or self.board[piece.row + 1][piece.col + 1].color == "white":
                moves.append((piece.row + 1, piece.col + 1))
            if in_bounds(piece.row + 1, piece.col - 1) \
                    and self.board[piece.row + 1][piece.col - 1] != 0 \
                    or self.board[piece.row + 1][piece.col - 1].color == "white":
                moves.append((piece.row + 1, piece.col - 1))
            # move downwards if space is free
            if self.board[piece.row + 1][piece.col] == 0:
                moves.append((piece.row + 1, piece.col))
        if piece.color == "white":
            # moves upwards
            # eat piece diagonally to the left or right
            if in_bounds(piece.row - 1, piece.col + 1) \
                    and self.board[piece.row - 1][piece.col + 1] != 0 \
                    or self.board[piece.row - 1][piece.col + 1].color == "black":
                moves.append((piece.row - 1, piece.col + 1))
            if in_bounds(piece.row - 1, piece.col - 1) and \
                    self.board[piece.row - 1][piece.col - 1] != 0 or \
                    self.board[piece.row - 1][piece.col - 1].color == "black":
                moves.append((piece.row - 1, piece.col - 1))
            # move upwards if space is free
            if self.board[piece.row - 1][piece.col] == 0:
                moves.append((piece.row - 1, piece.col))
        return moves

    def _rook_moves(self, piece):
        # horizontal/vertical in line. The space must be free/ occupied by
        # opposite color
        # black and white rooks move the same
        moves = []
        # simulating direction, left right for horizontal movement, up down for vertical
        directions = [-1, 1]
        i = 1
        # moving horizontal
        for direction in directions:
            while in_bounds(piece.row, piece.col + i * direction) \
                    and self.board[piece.row][piece.col + i * direction] == 0:
                moves.append((piece.row, piece.col + i * direction))
                if piece.color != self.board[piece.row][piece.col + i * direction].color:
                    moves.append((piece.row, piece.col + i * direction))
                i = i + 1
        i = 1
        # moving vertically
        for direction in directions:
            while in_bounds(piece.row + i * direction, piece.col) \
                    and self.board[piece.row + i * direction][piece.col] == 0:
                moves.append((piece.row + i * direction, piece.col))
                if piece.color != self.board[piece.row + i * direction][piece.col].color:
                    moves.append((piece.row + i * direction, piece.col))
                i = i + 1
        return moves

    def _knight_moves(self, piece):
        # moves in L shape
        moves = []
        # Up/Down left/right as seen on the matrix
        # 2 up 1 right
        if in_bounds(piece.row + 2, piece.col + 1) \
                and (self.board[piece.row + 2][piece.col + 1] == 0
                     or piece.color != self.board[piece.row + 1][piece.col + 1]):
            moves.append(self.board[piece.row + 2][piece.col + 1])

        # 2 up 1 left
        if in_bounds(piece.row + 2, piece.col - 1) \
                and (self.board[piece.row + 2][piece.col - 1] == 0
                     or piece.color != self.board[piece.row + 2][piece.col - 1]):
            moves.append(self.board[piece.row + 2][piece.col - 1])

        # 2 down 1 left
        if in_bounds(piece.row - 2, piece.col - 1) \
                and (self.board[piece.row - 2][piece.col - 1] == 0
                     or piece.color != self.board[piece.row - 2][piece.col - 1]):
            moves.append(self.board[piece.row - 2][piece.col - 1])

        # 2 down 1 right
        if in_bounds(piece.row - 2, piece.col + 1) \
                and (self.board[piece.row - 2][piece.col + 1] == 0
                     or piece.color != self.board[piece.row - 2][piece.col + 1]):
            moves.append(self.board[piece.row - 2][piece.col + 1])

        # 1 up 2 left
        if in_bounds(piece.row + 1, piece.col - 2) \
                and (self.board[piece.row + 1][piece.col - 2] == 0
                     or piece.color != self.board[piece.row + 1][piece.col - 2]):
            moves.append(self.board[piece.row + 1][piece.col - 2])

        # 1 up 2 right
        if in_bounds(piece.row + 1, piece.col + 2) \
                and (self.board[piece.row + 1][piece.col + 2] == 0
                     or piece.color != self.board[piece.row + 1][piece.col + 2]):
            moves.append(self.board[piece.row + 1][piece.col + 2])

        # 1 down 2 left
        if in_bounds(piece.row - 1, piece.col - 2) \
                and (self.board[piece.row - 1][piece.col - 2] == 0
                     or piece.color != self.board[piece.row - 1][piece.col - 2]):
            moves.append(self.board[piece.row - 1][piece.col - 2])

        # 1 down 2 right
        if in_bounds(piece.row - 1, piece.col + 2) \
                and (self.board[piece.row - 1][piece.col + 2] == 0
                     or piece.color != self.board[piece.row - 1][piece.col + 2]):
            moves.append(self.board[piece.row - 1][piece.col + 2])
        return moves

    def _bishop_moves(self, piece):
        # a bishop can move diagonally in 4 directions The space must be free/ occupied by
        # opposite color
        # black and white bishops move the same

        moves = []

        # Up/Down left/right as seen on the chess table
        # moving down to the left / right
        directions1 = [-1, 1]
        directions2 = [-1, 1]
        i = 1
        for direction1 in directions1:
            for direction2 in directions2:
                while in_bounds(piece.row + i * direction1, piece.col + i * direction2) \
                        and self.board[piece.row + i * direction1][piece.col + i * direction2] == 0:
                    moves.append((piece.row + i * direction1, piece.col + i * direction2))
                    if piece.color != self.board[piece.row + i * direction1][piece.col + i * direction2].color:
                        moves.append((piece.row + i * direction1, piece.col + i * direction2))
        return moves

    def _queen_moves(self, piece):
        # a queen can move both like a rook and a bishop
        moves = self._rook_moves(piece)
        for move in self._bishop_moves(piece):
            moves.append(move)
        return moves

    def _king_moves(self, piece):
        # can move 1 space in any direction. If a move puts the other king in check it is not valid
        moves = []
        if in_bounds(piece.row, piece.col + 1) and not KTK_check(self.board, piece.row, piece.col + 1):
            moves.append((piece.row, piece.col + 1))
        if in_bounds(piece.row - 1, piece.col + 1) and not KTK_check(self.board, piece.row - 1, piece.col + 1):
            moves.append((piece.row - 1, piece.col + 1))
        if in_bounds(piece.row - 1, piece.col) and not KTK_check(self.board, piece.row - 1, piece.col):
            moves.append((piece.row - 1, piece.col))
        if in_bounds(piece.row - 1, piece.col - 1) and not KTK_check(self.board, piece.row - 1, piece.col - 1):
            moves.append((piece.row - 1, piece.col - 1))
        if in_bounds(piece.row, piece.col - 1) and not KTK_check(self.board, piece.row, piece.col - 1):
            moves.append((piece.row, piece.col - 1))
        if in_bounds(piece.row + 1, piece.col - 1) and not KTK_check(self.board, piece.row + 1, piece.col - 1):
            moves.append((piece.row + 1, piece.col - 1))
        if in_bounds(piece.row + 1, piece.col) and not KTK_check(self.board, piece.row + 1, piece.col):
            moves.append((piece.row + 1, piece.col))
        if in_bounds(piece.row + 1, piece.col + 1) and not KTK_check(self.board, piece.row + 1, piece.col + 1):
            moves.append((piece.row + 1, piece.col + 1))

        return moves

    def update_valid_moves(self, piece):
        # pawn moves
        if piece.name == "Pawn":
            piece.valid_moves = self._pawn_moves(piece)
        # knight moves
        if piece.name == "Rook":
            piece.valid_moves = self._rook_moves(piece)
        if piece.name == "Knight":
            piece.valid_moves = self._knight_moves(piece)
        if piece.name == "Bishop":
            piece.valid_moves = self._bishop_moves(piece)
        if piece.name == "Queen":
            piece.valid_moves = self._queen_moves(piece)
        if piece.name == "King":
            piece.valid_moves = self._king_moves(piece)

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
        self.board[7][4] = Piece("Queen", "white", 7, 4)
        # white king placement
        self.board[7][3] = Piece("King", "white", 7, 3)

    def print_board(self):
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] != 0:
                    print(self.board[i][j].name + " ")
                else:
                    print("0 ")
            print("\n")
