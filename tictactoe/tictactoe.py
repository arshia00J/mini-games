"""
Tic Tac Toe Player
"""

import math
from copy import *
from random import *

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count X and O on board
    X_count = 0
    O_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                X_count += 1
            elif board[i][j] == O:
                O_count += 1

    if X_count <= O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()

    # Find empty places on board
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    result = deepcopy(board)
    result[action[0]][action[1]] = player(board)

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                pass
    # Vertical

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                pass

    # Diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O
        else:
            pass
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O
        else:
            pass

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True

    for i in board:
        if EMPTY in i:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        plays = []

        for action in actions(board):
            plays.append([min_val(result(board, action)), action])

        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_val(result(board, action)), action])

        return sorted(plays, key=lambda x: x[0])[0][1]


def max_val(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v


def min_val(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v
