import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from Menus import OptionsMenu

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Main Menu')
screen = pygame.display.set_mode((500, 500), 0, 32, 0, 1)
font = pygame.font.SysFont(None, 20)


def main_menu():
    while True:
        # pune o imagine de background
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        mainClock.tick(60)

main_menu()