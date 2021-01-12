"""
This module takes care of the player interaction with the board,
ai, or the other player. In other words the game class simulates a game.
"""

import pygame

from Game.Board import Board
from Utils.Draw import highlight_square
from Game.Piece import Piece
from Game.PieceMovement import is_in_check


def highlight_valid_moves(window, valid_moves):
    """Highlights valid moves of a selected piece"""
    for move in valid_moves:
        highlight_square(window, move[0], move[1])
    pygame.display.update()


class Game:
    def __init__(self, window):
        self.selected_piece: Piece = None
        self.board = Board()
        self.b_king = (0, 4)
        self.w_king = (7, 4)
        self.window = window
        self.turn = "white"  # white player always starts
        self.run = True

    def update(self):
        """Updates the game GUI"""
        self.board.draw(self.window)
        if self.selected_piece is not None:
            highlight_valid_moves(self.window, self.selected_piece.get_valid_moves())
        pygame.display.update()
        if self.check_win():
            self.run = False


    def deselect(self):
        """Deselects a piece"""
        self.selected_piece = None

    def select(self, row, col):
        """Selects a piece if none is selected, moves a selected piece"""
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
                    highlight_valid_moves(self.window, piece.get_valid_moves())
                else:
                    self.deselect()
                return True
        return False

    def _move(self, row, col):
        """Moves a selected piece if possible"""
        if self.selected_piece is not None:
            if not self.selected_piece.get_valid_moves():
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
        """Changes turn"""
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def check_win(self):
        """Checks the win condition"""
        white_king = self.board.get_piece(self.w_king[0], self.w_king[1])
        black_king = self.board.get_piece(self.b_king[0], self.b_king[1])
        w_in_check = is_in_check(self.board.board, white_king.color, white_king.row, white_king.col)
        b_in_check = is_in_check(self.board.board, black_king.color, black_king.row, black_king.col)
        if w_in_check and not white_king.get_valid_moves():
            print("Black has won")
            return 1
        if b_in_check and not black_king.get_valid_moves():
            print("White has won")
            return 1
        return 0
