from captains_mistress.gamecomponents.gametoken import GameToken


class GameBoard:
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

