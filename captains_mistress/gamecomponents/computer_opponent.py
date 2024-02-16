import copy

from captains_mistress.exceptions.columnfullerror import ColumnFullError
from captains_mistress.gamecomponents.gameboard import GameBoard
from captains_mistress.gamecomponents.gametoken import GameToken


def find_best_move(board: GameBoard, player: GameToken) -> int:
    """
    Finds the best move for the player using the minimax algorithm.

    Parameters
    ----------
    board : GameBoard
        The current state of the game board.
    player : GameToken
        The token of the player for whom the best move is to be found.

    Returns
    -------
    int
        The column representing the best move for the player.
    """
    best_score = float('-inf')
    best_move_col = 0
    for col in range(board.cols):
        try:
            new_board = copy.deepcopy(board)
            new_board.drop_token(col, player)
            score = minimax(new_board, 3, False, player)
            if score > best_score:
                best_score = score
                best_move_col = col
        except ColumnFullError:
            continue
    return best_move_col


def evaluate_board(board: GameBoard, player: GameToken) -> int:
    """
    Evaluate the score of the board.

    Parameters
    ----------
    board : GameBoard
        The current state of the game board.
    player : GameToken
        The token of the player for whom the board is to be evaluated.

    Returns
    -------
    int
        The score of the board for the given player.
    """

    total_score = 0

    # Check rows
    for row in range(board.rows):
        for col in range(board.cols - 3):
            window = [board.board[row][col + i] for i in range(4)]
            total_score += evaluate_window(window, player)

    # Check columns
    for col in range(board.cols):
        for row in range(board.rows - 3):
            window = [board.board[row + i][col] for i in range(4)]
            total_score += evaluate_window(window, player)

    # Check diagonals (positive slope)
    for row in range(board.rows - 3):
        for col in range(board.cols - 3):
            window = [board.board[row + i][col + i] for i in range(4)]
            total_score += evaluate_window(window, player)

    # Check diagonals (negative slope)
    for row in range(3, board.rows):
        for col in range(board.cols - 3):
            window = [board.board[row - i][col + i] for i in range(4)]
            total_score += evaluate_window(window, player)

    return total_score


def evaluate_window(window: list, player: GameToken) -> int:
    """
    Evaluate a window of tokens.

    Parameters
    ----------
    window : list
        A window of tokens to be evaluated.
    player : GameToken
        The token of the player for whom the window is to be evaluated.

    Returns
    -------
    int
        The score of the window for the given player.
    """

    opponent = GameToken.RED if player == GameToken.YELLOW else GameToken.YELLOW
    # Define the scores for different patterns
    scores = {
        1: 1,  # One token in a row
        2: 5,  # Two tokens in a row
        3: 50,  # Three tokens in a row
        4: 500,  # Four tokens in a row (winning move)
    }
    player_count = window.count(player)
    opponent_count = window.count(opponent)

    if player_count == 4:
        return scores[4]
    elif opponent_count == 4:
        return -scores[4]
    elif player_count == 3 and window.count(GameToken.EMPTY) == 1:
        return scores[3]
    elif opponent_count == 3 and window.count(GameToken.EMPTY) == 1:
        return -scores[3]
    elif player_count == 2 and window.count(GameToken.EMPTY) == 2:
        return scores[2]
    elif opponent_count == 2 and window.count(GameToken.EMPTY) == 2:
        return -scores[2]
    else:
        return 0


def minimax(board: GameBoard, depth: int, maximizing_player: bool, player: GameToken) -> int:
    """
    Minimax algorithm for finding the best move.

    Parameters
    ----------
    board : GameBoard
        The current state of the game board.
    depth : int
        The depth of the search tree.
    maximizing_player : bool
        A boolean indicating whether the current player is maximizing or not.
    player : GameToken
        The token of the player for whom the best move is to be found.

    Returns
    -------
    int
        The score of the best move.
    """

    if depth == 0 or board.check_winner():
        return evaluate_board(board, player)

    if maximizing_player:
        max_score = float('-inf')
        for col in range(board.cols):
            try:
                new_board = copy.deepcopy(board)
                new_board.drop_token(col, player)
                score = minimax(new_board, depth - 1, False, player)
                max_score = max(max_score, score)
            except ColumnFullError:
                continue
        return max_score
    else:
        min_score = float('inf')
        for col in range(board.cols):
            try:
                new_board = copy.deepcopy(board)
                new_board.drop_token(col, GameToken.RED if player == GameToken.YELLOW else GameToken.YELLOW)
                score = minimax(new_board, depth - 1, True, player)
                min_score = min(min_score, score)
            except ColumnFullError:
                continue
        return min_score
