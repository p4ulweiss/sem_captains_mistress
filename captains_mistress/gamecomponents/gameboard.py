from captains_mistress.gamecomponents.gametoken import GameToken
from captains_mistress.exceptions.columnfullerror import ColumnFullError


class GameBoard:
    """
    Represents the game board.

    This class manages the state of the game board, including its dimensions and contents.

    Attributes
    ----------
    rows : int
        The number of rows in the game board.
    cols : int
        The number of columns in the game board.
    board : List[List[GameToken]]
        A 2D list representing the game board, initialized with GameToken.EMPTY.

    Methods
    -------
    drop_token(col: int, token: GameToken)
        Drops a token into the specified column.
    check_winner() -> bool
        Checks if there is a winner on the game board.
    print_board()
        Prints the current state of the game board.
    colorize(token)
        Colorizes the token for display.
    reset_gameboard()
        Clears gameboard.
    __init__(rows=6, cols=7)
        Initializes a new instance of the Connect Four game board.
    """

    COLOR_RED = '\033[91m'
    COLOR_YELLOW = '\033[93m'
    COLOR_RESET = '\033[0m'

    def __init__(self, rows=6, cols=7):
        """
        Initializes a new instance of the Connect Four game.

        Parameters
        ----------
        rows : int, optional
            The number of rows in the game board. Default is 6.
        cols : int, optional
            The number of columns in the game board. Default is 7.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.rows = rows
        self.cols = cols
        self.board = [[GameToken.EMPTY for _ in range(cols)] for _ in range(rows)]
        pass

    def reset_gameboard(self) -> None:
        self.board = [[GameToken.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        pass

    def drop_token(self, col: int, token: GameToken) -> bool:
        """ Drops a token into the specified column.

        This function drops a token into the given column
        and throws exception if it is not possible

        Parameters
        ----------
        col : int
            The column where the token is to be dropped.
        token : GameToken
            The token to be dropped.

        Returns
        -------
        bool
            True if the token is successfully dropped, False otherwise.

        Raises
        ------
        IndexError
            If the column index is out of range.
        ColumnFullError
            If the specified column is already full.
        """
        if not 0 <= col <= self.cols:
            raise IndexError("Column out of Index")
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == GameToken.EMPTY:
                self.board[row][col] = token
                return True
        raise ColumnFullError("Column is full of tokens!")