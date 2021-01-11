import pygame

from Game.Board import Board
from Utils.Draw import highlight_square
from Game.Piece import Piece


def highlight_valid_moves(window, valid_moves):
    for move in valid_moves:
        highlight_square(window, move[0], move[1])
    pygame.display.update()


class Game:
    def __init__(self, window):
        self.selected_piece: Piece = None
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        if self.selected_piece is not None:
            highlight_valid_moves(self.window, self.selected_piece.get_valid_moves())
        pygame.display.update()

    def _init(self):
        self.board = Board()
        self.turn = "white"  # white player always starts
        self.b_king = (0, 4)
        self.w_king = (7, 4)

    def reset(self):
        self._init()

    def deselect(self):
        print("Piesa a fost deselectata")
        self.selected_piece = None

    def select(self, row, col):
        if self.selected_piece:
            if self.selected_piece.color == "white":
                if row == self.b_king[0] and col == self.b_king[1]:
                    move = False
                else:
                    # try to move
                    move = self._move(row, col)
            elif self.selected_piece.color == "black":
                if row == self.w_king[0] and col == self.w_king[1]:
                    move = False
                else:
                    # try to move
                    move = self._move(row, col)

            if not move:
                # reselect the piece
                self.deselect()
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected_piece = piece
                if self.selected_piece.get_valid_moves():
                    print("Urmatoarele mutari sunt pos: ")
                    highlight_valid_moves(self.window, piece.get_valid_moves())
                    print(piece.valid_moves)
                else:
                    self.deselect()
                return True
        return False

    def _move(self, row, col):
        print(self.selected_piece)
        if self.selected_piece is not None:
            if not self.selected_piece.get_valid_moves():
                print("There are no valid moves")
                self.deselect()
            if (row, col) in self.selected_piece.get_valid_moves():
                if self.board.board[row][col] != 0:
                    self.board.board[row][col] = 0
                # update king positions
                if self.selected_piece.name == "King":
                    if self.selected_piece.color == "white":
                        self.w_king = (row, col)
                    else:
                        self.b_king = (row, col)
                self.board.move(self.selected_piece, row, col)
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

