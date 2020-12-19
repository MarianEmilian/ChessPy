import pygame
from Utils.Constants import WINDOW_HEIGHT, WINDOW_WIDTH
from Game.Board import *
from Utils.Constants import BLACK

pygame.display.set_caption('ChessPy')

FPS = 60
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WINDOW.fill(BLACK)


def init_board(board):
    board.hardcode_pieces()
    draw_board(WINDOW)
    board.draw_pieces(WINDOW)
    pygame.display.update()


def get_rc_from_mouse(pos):
    x, y = pos
    # compensate for padding
    x = x - BOARD_BUFFER
    y = y - BOARD_BUFFER

    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    if row in range(8) and col in range(8):
        return row, col
    return -1, -1


def game():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    init_board(board)
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_rc_from_mouse(pygame.mouse.get_pos())
                piece = board.get_piece(row, col)


    pygame.quit()


game()
