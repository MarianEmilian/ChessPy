import pygame

from Game.Board import Board
from Utils.Constants import WHITE


class Game:
    def __init__(self, window):
        self.selectedPiece = None
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

    def deselect(self):
        self.selectedPiece = None

    def select(self, row, col):
        if self.selectedPiece:
            # try to move
            move = self._move(row, col)
            if not move:
                # reselect the piece
                self.selectedPiece = None
                self.select(row, col)
                print("Hei")
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selectedPiece = piece
                print("Woo")
                return True
        return False

    def _move(self, row, col):
        if self.selectedPiece:
            if not self.selectedPiece.valid_moves:
                print("There are no valid moves")
                self.deselect()
            if self.board.board[row][col] != 0:
                if (row, col) in self.selectedPiece.valid_moves:
                    self.board.move(self.selectedPiece, row, col)
                    self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        if self.turn == "white":
            self.turn == "black"
        else:
            self.turn == "white"
