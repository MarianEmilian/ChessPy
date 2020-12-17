import pygame
from Utils.Constants import WINDOW_HEIGHT, WINDOW_WIDTH
from Game.Board import draw_board

pygame.display.set_caption('ChessPy')

FPS = 60
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def game():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        draw_board(WINDOW)
        pygame.display.update()

    pygame.quit()


game()