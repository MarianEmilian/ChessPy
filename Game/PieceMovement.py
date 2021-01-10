from Utils.Constants import ROWS, COLS
from Utils.Constants import SQUARE_SIZE, BOARD_BUFFER
from Game.Piece import Piece


def in_bounds(row, col):
    if row in range(ROWS) and col in range(COLS):
        return True
    return False


def KTK_check(board, row, col):
    # verifies if a king puts in check another one
    # get the other king row col
    for row2 in range(ROWS):
        for col2 in range(COLS):
            if board[row][col] != 0 and board[row2][col2] != 0 \
                    and board[row][col].color != board[row2][col2].color and board[row2][col2].name == "king":
                break
    row_dist = row2 - row
    col_dist = col2 - col
    if abs(row_dist) <= 1 and abs(col_dist) <= 1:
        return True
    return False


def pawn_moves(board, piece):
    moves = []
    if piece.color == "black":
        # moves downwards
        # eat piece diagonally to the left or right
        if in_bounds(piece.row + 1, piece.col + 1) \
                and board[piece.row + 1][piece.col + 1] != 0 \
                and board[piece.row + 1][piece.col + 1].color == "white":
            moves.append((piece.row + 1, piece.col + 1))
        if in_bounds(piece.row + 1, piece.col - 1) \
                and board[piece.row + 1][piece.col - 1] != 0 \
                and board[piece.row + 1][piece.col - 1].color == "white":
            moves.append((piece.row + 1, piece.col - 1))
        # move downwards if space is free
        if board[piece.row + 1][piece.col] == 0:
            moves.append((piece.row + 1, piece.col))
    if piece.color == "white":
        # moves upwards
        # eat piece diagonally to the left or right
        if in_bounds(piece.row - 1, piece.col + 1) \
                and board[piece.row - 1][piece.col + 1] != 0 \
                and board[piece.row - 1][piece.col + 1].color == "black":
            moves.append((piece.row - 1, piece.col + 1))
        if in_bounds(piece.row - 1, piece.col - 1) \
                and board[piece.row - 1][piece.col - 1] != 0 \
                and board[piece.row - 1][piece.col - 1].color == "black":
            moves.append((piece.row - 1, piece.col - 1))
        # move upwards if space is free
        if board[piece.row - 1][piece.col] == 0:
            moves.append((piece.row - 1, piece.col))
    return moves


def rook_moves(board, piece):
    # horizontal/vertical in line. The space must be free/ occupied by
    # opposite color
    # black and white rooks move the same
    moves = []
    # simulating direction, left right for horizontal movement, up down for vertical
    directions = [-1, 1]
    i = 1
    # moving horizontal
    for direction in directions:
        while in_bounds(piece.row, piece.col + i * direction) \
                and board[piece.row][piece.col + i * direction] == 0:
            moves.append((piece.row, piece.col + i * direction))
            if board[piece.row][piece.col + i * direction] != 0 \
                    and piece.color != board[piece.row][piece.col + i * direction].color:
                moves.append((piece.row, piece.col + i * direction))
            i = i + 1
    i = 1
    # moving vertically
    for direction in directions:
        while in_bounds(piece.row + i * direction, piece.col) \
                and board[piece.row + i * direction][piece.col] == 0:
            moves.append((piece.row + i * direction, piece.col))
            if board[piece.row + i * direction][piece.col] != 0 \
                    and piece.color != board[piece.row + i * direction][piece.col].color:
                moves.append((piece.row + i * direction, piece.col))
            i = i + 1
    return moves


def knight_moves(board, piece):
    # moves in L shape
    moves = []
    # Up/Down left/right as seen on the matrix
    # 2 up 1 right
    if in_bounds(piece.row + 2, piece.col + 1) \
            and (board[piece.row + 2][piece.col + 1] == 0
                 or piece.color != board[piece.row + 1][piece.col + 1]):
        moves.append(board[piece.row + 2][piece.col + 1])

    # 2 up 1 left
    if in_bounds(piece.row + 2, piece.col - 1) \
            and (board[piece.row + 2][piece.col - 1] == 0
                 or piece.color != board[piece.row + 2][piece.col - 1]):
        moves.append(board[piece.row + 2][piece.col - 1])

    # 2 down 1 left
    if in_bounds(piece.row - 2, piece.col - 1) \
            and (board[piece.row - 2][piece.col - 1] == 0
                 or piece.color != board[piece.row - 2][piece.col - 1]):
        moves.append(board[piece.row - 2][piece.col - 1])

    # 2 down 1 right
    if in_bounds(piece.row - 2, piece.col + 1) \
            and (board[piece.row - 2][piece.col + 1] == 0
                 or piece.color != board[piece.row - 2][piece.col + 1]):
        moves.append(board[piece.row - 2][piece.col + 1])

    # 1 up 2 left
    if in_bounds(piece.row + 1, piece.col - 2) \
            and (board[piece.row + 1][piece.col - 2] == 0
                 or piece.color != board[piece.row + 1][piece.col - 2]):
        moves.append(board[piece.row + 1][piece.col - 2])

    # 1 up 2 right
    if in_bounds(piece.row + 1, piece.col + 2) \
            and (board[piece.row + 1][piece.col + 2] == 0
                 or piece.color != board[piece.row + 1][piece.col + 2]):
        moves.append(board[piece.row + 1][piece.col + 2])

    # 1 down 2 left
    if in_bounds(piece.row - 1, piece.col - 2) \
            and (board[piece.row - 1][piece.col - 2] == 0
                 or piece.color != board[piece.row - 1][piece.col - 2]):
        moves.append(board[piece.row - 1][piece.col - 2])

    # 1 down 2 right
    if in_bounds(piece.row - 1, piece.col + 2) \
            and (board[piece.row - 1][piece.col + 2] == 0
                 or piece.color != board[piece.row - 1][piece.col + 2]):
        moves.append(board[piece.row - 1][piece.col + 2])
    return moves


def bishop_moves(board, piece):
    # a bishop can move diagonally in 4 directions The space must be free/ occupied by
    # opposite color
    # black and white bishops move the same

    moves = []

    # Up/Down left/right as seen on the chess table
    # moving down to the left / right
    directions1 = [-1, 1]
    directions2 = [-1, 1]
    i = 1
    for direction1 in directions1:
        for direction2 in directions2:
            while in_bounds(piece.row + i * direction1, piece.col + i * direction2) \
                    and board[piece.row + i * direction1][piece.col + i * direction2] == 0:
                moves.append((piece.row + i * direction1, piece.col + i * direction2))
                if board[piece.row + i * direction1][piece.col + i * direction2] != 0 \
                        and piece.color != board[piece.row + i * direction1][piece.col + i * direction2].color:
                    moves.append((piece.row + i * direction1, piece.col + i * direction2))
                i = i + 1
    return moves


def queen_moves(board, piece):
    # a queen can move both like a rook and a bishop
    moves = rook_moves(board, piece)
    for move in bishop_moves(board, piece):
        moves.append(move)
    return moves


def king_moves(board, piece):
    # can move 1 space in any direction. If a move puts the other king in check it is not valid
    moves = []
    if in_bounds(piece.row, piece.col + 1) and not KTK_check(board, piece.row, piece.col + 1):
        moves.append((piece.row, piece.col + 1))
    if in_bounds(piece.row - 1, piece.col + 1) and not KTK_check(board, piece.row - 1, piece.col + 1):
        moves.append((piece.row - 1, piece.col + 1))
    if in_bounds(piece.row - 1, piece.col) and not KTK_check(board, piece.row - 1, piece.col):
        moves.append((piece.row - 1, piece.col))
    if in_bounds(piece.row - 1, piece.col - 1) and not KTK_check(board, piece.row - 1, piece.col - 1):
        moves.append((piece.row - 1, piece.col - 1))
    if in_bounds(piece.row, piece.col - 1) and not KTK_check(board, piece.row, piece.col - 1):
        moves.append((piece.row, piece.col - 1))
    if in_bounds(piece.row + 1, piece.col - 1) and not KTK_check(board, piece.row + 1, piece.col - 1):
        moves.append((piece.row + 1, piece.col - 1))
    if in_bounds(piece.row + 1, piece.col) and not KTK_check(board, piece.row + 1, piece.col):
        moves.append((piece.row + 1, piece.col))
    if in_bounds(piece.row + 1, piece.col + 1) and not KTK_check(board, piece.row + 1, piece.col + 1):
        moves.append((piece.row + 1, piece.col + 1))

    return moves
