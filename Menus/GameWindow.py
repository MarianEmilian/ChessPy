import pygame
from Utils.Constants import WINDOW_HEIGHT, WINDOW_WIDTH, BOARD_BUFFER, SQUARE_SIZE
from Utils.Constants import BLACK
from Game.Game import Game

pygame.display.set_caption('ChessPy')

FPS = 60
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WINDOW.fill(BLACK)


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


def game_main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    row, col = get_rc_from_mouse(pygame.mouse.get_pos())
                    print(game.turn)
                    game.select(row, col)
        game.update()
    pygame.quit()


game_main()
