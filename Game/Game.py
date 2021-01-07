import pygame

from Game.Board import Board
from Utils.Draw import highlight_square
from Game.Piece import Piece


def highlight_valid_moves(window, valid_moves):
    for move in valid_moves:
        print(move[0])
        print(move[1])
        highlight_square(window, move[0], move[1])
    pygame.display.update()


class Game:
    def __init__(self, window):
        self.selectedPiece: Piece = None
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        if self.selectedPiece is not None:
            highlight_valid_moves(self.window, self.selectedPiece.get_valid_moves())
        pygame.display.update()

    def _init(self):
        self.board = Board()
        self.turn = "white"  # white player always starts

    def reset(self):
        self._init()

    def deselect(self):
        print("Piesa a fost deselectata")
        self.selectedPiece = None

    def select(self, row, col):
        if self.selectedPiece:
            # try to move
            move = self._move(row, col)
            print(move)
            if not move:
                # reselect the piece
                self.selectedPiece = None
                self.select(row, col)
                print("Nu poti muta acolo")
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selectedPiece = piece
                print("Urmatoarele mutari sunt pos: ")
                highlight_valid_moves(self.window, piece.get_valid_moves())
                print(piece.valid_moves)
                return True
        return False

    def _move(self, row, col):
        if self.selectedPiece is not None:
            if not self.selectedPiece.get_valid_moves():
                print("There are no valid moves")
                self.deselect()
            if (row, col) in self.selectedPiece.valid_moves:
                if self.board.board[row][col] != 0:
                    self.board.board[row][col] = 0
                self.board.move(self.selectedPiece, row, col)
                self.board.update_moves()
                self.deselect()

                self.change_turn()
            else:
                return False
        return True

    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
