import pygame

from Game.Board import Board


class Game:
    def __init__(self, window):
        self.selected = None
        self.board = Board()
