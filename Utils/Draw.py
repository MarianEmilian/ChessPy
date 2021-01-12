"""
A module that focuses on functions for drawing
"""
import pygame
from Utils.Constants import GREEN
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER, SQUARE_PADDING


def highlight_square(window, row, col):
    radius = SQUARE_SIZE // 2 - SQUARE_PADDING
    x = SQUARE_SIZE * col + SQUARE_SIZE // 2 + BOARD_BUFFER
    y = SQUARE_SIZE * row + SQUARE_SIZE // 2 + BOARD_BUFFER
    pygame.draw.circle(window, GREEN, (x, y), radius)
