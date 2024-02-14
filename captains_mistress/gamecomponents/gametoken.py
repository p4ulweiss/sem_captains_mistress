from enum import Enum

class GameToken(Enum):
    """
    Enum representing game tokens for Connect Four.

    This enum defines the tokens used in the Connect Four game: RED, YELLOW, and EMPTY.

    Attributes
    ----------
    RED : str
        Represents the red token on the game board.
    YELLOW : str
        Represents the yellow token on the game board.
    EMPTY : str
        Represents an empty space on the game board.

    Methods
    -------
    __str__()
        Returns a string representation of the token.

    """

    RED = 'X'
    YELLOW = '0'
    EMPTY = ' '

    def __str__(self):
        """
        Returns a string representation of the token.

        Returns
        -------
        str
            A string representation of the token.
        """
        if self == GameToken.RED:
            return "RED"
        elif self == GameToken.YELLOW:
            return "YELLOW"
        else:
            return "EMPTY"
