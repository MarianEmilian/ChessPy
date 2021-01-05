import pygame

from Game.Board import Board
from Utils.Constants import WHITE


class Game:
    def __init__(self, window):
        self.selected = None
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        pygame.display.update()

    def _init(self):
        self.board = Board()
        self.turn = "white"  # white player always starts

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            # try to move
            move = self._move(row, col)
            if not move:
                # reselect the piece
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                return True
        return False

    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in piece.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        if self.turn == "white":
            self.turn == "black"
        else:
            self.turn == "white"
