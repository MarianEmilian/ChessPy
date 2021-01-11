from Utils.Constants import ROWS, COLS


def get_kings_pos(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != 0 and board[row][col].name == "King":
                if board[row][col].color == "white":
                    w_king = (row, col)
                else:
                    b_king = (row, col)
    return w_king, b_king


def get_blacks(board):
    pieces = []
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != 0 and board[row][col].color == "black":
                pieces.append(board[row][col])
    return pieces


def in_bounds(row, col):
    if row in range(0, 7) and col in range(0, 7):
        return True
    return False


def KTK_check(board, color, row, col):
    # verifies if a king puts in check another one
    # get the other king row col
    found = False
    aux_r = 0
    aux_c = 0
    for row2 in range(ROWS):
        for col2 in range(COLS):
            if not found and board[row2][col2] != 0:
                if board[row2][col2].name == "King" and color != board[row2][col2].color:
                    aux_r = row2
                    aux_c = col2
                    found = True
    row_dist = aux_r - row
    col_dist = aux_c - col
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
        if in_bounds(piece.row + 1, piece.col) \
                and board[piece.row + 1][piece.col] == 0:
            moves.append((piece.row + 1, piece.col))
            # move 2 spaces if first move
            if piece.row == 1 and board[piece.row + 2][piece.col] == 0:
                moves.append((piece.row + 2, piece.col))

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
        if in_bounds(piece.row - 1, piece.col) \
                and board[piece.row - 1][piece.col] == 0:
            moves.append((piece.row - 1, piece.col))
            # move 2 spaces if first move
            if piece.row == 6 and board[piece.row - 2][piece.col] == 0:
                moves.append((piece.row - 2, piece.col))

    return moves


def rook_moves(board, piece):
    # horizontal/vertical in line. The space must be free/ occupied by
    # opposite color
    # black and white rooks move the same
    moves = []
    # simulating direction, left right for horizontal movement, up down for vertical
    directions = [-1, 1]

    # moving horizontal
    for direction in directions:
        i = 1
        while in_bounds(piece.row, piece.col + i * direction) \
                and (board[piece.row][piece.col + i * direction] == 0
                     or (board[piece.row][piece.col + i * direction] != 0
                         and piece.color != board[piece.row][piece.col + i * direction].color)):
            moves.append((piece.row, piece.col + i * direction))
            if board[piece.row][piece.col + i * direction] != 0 \
                    and piece.color != board[piece.row][piece.col + i * direction].color:
                break
            i = i + 1

    # moving vertically
    for direction in directions:
        i = 1
        while in_bounds(piece.row + i * direction, piece.col) \
                and (board[piece.row + i * direction][piece.col] == 0
                     or (board[piece.row + i * direction][piece.col] != 0
                         and piece.color != board[piece.row + i * direction][piece.col].color)):
            moves.append((piece.row + i * direction, piece.col))
            if board[piece.row + i * direction][piece.col] != 0 \
                    and piece.color != board[piece.row + i * direction][piece.col].color:
                break
            i = i + 1
    return moves


def knight_moves(board, piece):
    # moves in L shape
    moves = []
    # Up/Down left/right as seen on the matrix
    # 2 up 1 right
    if in_bounds(piece.row + 2, piece.col + 1) \
            and (board[piece.row + 2][piece.col + 1] == 0
                 or piece.color != board[piece.row + 2][piece.col + 1].color):
        moves.append((piece.row + 2, piece.col + 1))

    # 2 up 1 left
    if in_bounds(piece.row + 2, piece.col - 1) \
            and (board[piece.row + 2][piece.col - 1] == 0
                 or piece.color != board[piece.row + 2][piece.col - 1].color):
        moves.append((piece.row + 2, piece.col - 1))

    # 2 down 1 left
    if in_bounds(piece.row - 2, piece.col - 1) \
            and (board[piece.row - 2][piece.col - 1] == 0
                 or piece.color != board[piece.row - 2][piece.col - 1].color):
        moves.append((piece.row - 2, piece.col - 1))

    # 2 down 1 right
    if in_bounds(piece.row - 2, piece.col + 1) \
            and (board[piece.row - 2][piece.col + 1] == 0
                 or piece.color != board[piece.row - 2][piece.col + 1].color):
        moves.append((piece.row - 2, piece.col + 1))

    # 1 up 2 left
    if in_bounds(piece.row + 1, piece.col - 2) \
            and (board[piece.row + 1][piece.col - 2] == 0
                 or piece.color != board[piece.row + 1][piece.col - 2].color):
        moves.append((piece.row + 1, piece.col - 2))

    # 1 up 2 right
    if in_bounds(piece.row + 1, piece.col + 2) \
            and (board[piece.row + 1][piece.col + 2] == 0
                 or piece.color != board[piece.row + 1][piece.col + 2].color):
        moves.append((piece.row + 1, piece.col + 2))

    # 1 down 2 left
    if in_bounds(piece.row - 1, piece.col - 2) \
            and (board[piece.row - 1][piece.col - 2] == 0
                 or piece.color != board[piece.row - 1][piece.col - 2].color):
        moves.append((piece.row - 1, piece.col - 2))

    # 1 down 2 right
    if in_bounds(piece.row - 1, piece.col + 2) \
            and (board[piece.row - 1][piece.col + 2] == 0
                 or piece.color != board[piece.row - 1][piece.col + 2].color):
        moves.append((piece.row - 1, piece.col + 2))
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
    for direction1 in directions1:
        for direction2 in directions2:
            i = 1
            while in_bounds(piece.row + i * direction1, piece.col + i * direction2) \
                    and (board[piece.row + i * direction1][piece.col + i * direction2] == 0
                         or (board[piece.row + i * direction1][piece.col + i * direction2] != 0
                             and piece.color != board[piece.row + i * direction1][piece.col + i * direction2].color)):
                moves.append((piece.row + i * direction1, piece.col + i * direction2))
                if board[piece.row + i * direction1][piece.col + i * direction2] != 0 \
                        and piece.color != board[piece.row + i * direction1][piece.col + i * direction2].color:
                    break
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
    if in_bounds(piece.row, piece.col + 1) \
            and not KTK_check(board, piece.color, piece.row, piece.col + 1):
        if board[piece.row][piece.col + 1] == 0 \
                or (board[piece.row][piece.col + 1] != 0
                    and board[piece.row][piece.col + 1].color != piece.color):
            moves.append((piece.row, piece.col + 1))
            print(piece.color + "1")
    if in_bounds(piece.row - 1, piece.col + 1) \
            and not KTK_check(board, piece.color, piece.row - 1, piece.col + 1):
        if board[piece.row - 1][piece.col + 1] == 0 \
                or (board[piece.row - 1][piece.col + 1] != 0
                    and board[piece.row - 1][piece.col + 1].color != piece.color):
            moves.append((piece.row - 1, piece.col + 1))
            print(piece.color + "2")
    if in_bounds(piece.row - 1, piece.col) \
            and not KTK_check(board, piece.color, piece.row - 1, piece.col):
        if board[piece.row - 1][piece.col] == 0 \
                or (board[piece.row - 1][piece.col] != 0
                    and board[piece.row - 1][piece.col].color != piece.color):
            moves.append((piece.row - 1, piece.col))
            print(piece.color + "3")
    if in_bounds(piece.row - 1, piece.col - 1) \
            and not KTK_check(board, piece.color, piece.row - 1, piece.col - 1):
        if board[piece.row - 1][piece.col - 1] == 0 \
                or (board[piece.row - 1][piece.col - 1] != 0
                    and board[piece.row - 1][piece.col - 1].color != piece.color):
            moves.append((piece.row - 1, piece.col - 1))
            print(piece.color + "4")
    if in_bounds(piece.row, piece.col - 1) \
            and not KTK_check(board, piece.color, piece.row, piece.col - 1):
        if board[piece.row][piece.col - 1] == 0 \
                or (board[piece.row][piece.col - 1] != 0
                    and board[piece.row][piece.col - 1].color != piece.color):
            moves.append((piece.row, piece.col - 1))
            print(piece.color + "5")
    if in_bounds(piece.row + 1, piece.col - 1) \
            and not KTK_check(board, piece.color, piece.row + 1, piece.col - 1):
        if board[piece.row + 1][piece.col - 1] == 0 \
                or (board[piece.row + 1][piece.col - 1] != 0
                    and board[piece.row + 1][piece.col - 1].color != piece.color):
            moves.append((piece.row + 1, piece.col - 1))
            print(piece.color + "6")
    if in_bounds(piece.row + 1, piece.col) \
            and not KTK_check(board, piece.color, piece.row + 1, piece.col):
        if board[piece.row + 1][piece.col] == 0 \
                or (board[piece.row + 1][piece.col] != 0
                    and board[piece.row + 1][piece.col].color != piece.color):
            moves.append((piece.row + 1, piece.col))
            print(piece.color + "7")
    if in_bounds(piece.row + 1, piece.col + 1) \
            and not KTK_check(board, piece.color, piece.row + 1, piece.col + 1):
        if board[piece.row + 1][piece.col + 1] == 0 \
                or (board[piece.row + 1][piece.col + 1] != 0
                    and board[piece.row + 1][piece.col + 1].color != piece.color):
            moves.append((piece.row + 1, piece.col + 1))
            print(piece.color + "8")

    return moves
