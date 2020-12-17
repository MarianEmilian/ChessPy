"""
A board is a space with 64 spaces, conventionally alternating black and white. For visual purposes i replaced black with
light blue.
Each space can either contain a piece at a time, or be empty.

"""
import pygame
from pygame import Color
# used colors
from Utils.Constants import BLACK, WHITE, BLUE
# board dimensions
from Utils.Constants import ROWS, COLS
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER


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
        self.board = []
