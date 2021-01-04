"""
A piece is either a pawn, knight, bishop, rook, or queen.
It belongs to a player or another, fact represented by its color.
The piece has a place on the board represented by its row and column
"""
import os
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER
from Utils.Constants import IMG_PATH
from pygame.image import load
from pygame.transform import scale


class Piece:
    def __init__(self, name: str, color: str, row: int, col: int):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.valid_moves = {}

        # the name of the images is the first letter of the color + the piece name
        # Example: wPawn/bKing/bRook/wQueen
        self.img_path = IMG_PATH + self.color[0] + name + ".png"

        # variables for the position in space of the image
        self.x = 0
        self.y = 0

        self.calc_coord()

    def pawn_to_other(self, name: str):
        # Updates pawn
        self.name = name
        self.img_path = IMG_PATH + self.color[0] + name + ".png"

    def calc_coord(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 + BOARD_BUFFER // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 + BOARD_BUFFER // 2

    def draw(self, window):
        piece_img = load(self.img_path)
        # downsizing img. Rotate by 0 deg, multiply by 0,5
        piece_img = scale(piece_img, (92, 92))
        window.blit(piece_img, (self.x, self.y))

    def update_piece(self, row, col):
        # update row and col
        self.row = row
        self.col = col
        # update coordinates
        self.calc_coord()

