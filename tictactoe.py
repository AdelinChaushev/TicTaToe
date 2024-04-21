"""
Tic Tac Toe Player
"""
import copy
import math

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
    XCount = 0
    OCount = 0
    for row in board:
        for col in row:
            if col == X:
                XCount += 1
            elif col == O:
                OCount += 1
    if XCount == OCount:
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == EMPTY:
                actions.append((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if all(action != currAction for currAction in actions(board)):
        raise Exception("Invalid Action")
    boardCopy = copy.deepcopy(board)
    boardCopy[action[0]][action[1]] = player(board)
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    """
    if winner(board) != None:
        return True
    else:
        # Check if the board is full
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:

        v = -math.inf
        optimalMove = None
        for action in actions(board):
            newv = minValue(result(board, action), -math.inf, math.inf)
            if newv > v:
                v = newv
                optimalMove = action
        return optimalMove
    elif player(board) == O:

        v = math.inf
        optimalMove = None
        for action in actions(board):
            newv = maxValue(result(board, action), -math.inf, math.inf)
            if v > newv:
                v = newv
                optimalMove = action
        return optimalMove


def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action), alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v


def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v
