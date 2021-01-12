import pygame
from Utils.Constants import WINDOW_HEIGHT, WINDOW_WIDTH, BOARD_BUFFER, SQUARE_SIZE
from Utils.Constants import BLACK
from Game.Game import Game
from random import choice
from Game.PieceMovement import get_blacks

pygame.display.set_caption('ChessPy')

FPS = 60
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WINDOW.fill(BLACK)


def get_rc_from_mouse(pos):
    """Returns board coordinates from mouse position"""
    x, y = pos
    # compensate for padding
    x = x - BOARD_BUFFER
    y = y - BOARD_BUFFER

    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    if row in range(8) and col in range(8):
        return row, col
    return -1, -1


def game_main():
    """Runs game"""
    clock = pygame.time.Clock()
    game = Game(WINDOW)
    p_vs = input("Choose who to play with. Player/AI: ")

    while game.run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # player action
                    if game.turn == "white":
                        row, col = get_rc_from_mouse(pygame.mouse.get_pos())
                        game.select(row, col)
                    if p_vs == "AI" and game.turn == "black":
                        # AI random moves
                        piece = choice(get_blacks(game.board.board))
                        moves = piece.get_valid_moves()
                        while not moves:
                            piece = choice(get_blacks(game.board.board))
                            moves = piece.get_valid_moves()
                        game.selected_piece = piece
                        move = choice(moves)
                        row, col = move[0], move[1]
                        game.select(row, col)
                    elif p_vs == "Player" and game.turn == "black":
                        row, col = get_rc_from_mouse(pygame.mouse.get_pos())
                        game.select(row, col)
        game.update()
    pygame.quit()


game_main()
