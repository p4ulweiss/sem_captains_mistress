class ColumnFullError(Exception):
    """
    Exception raised when attempting to drop a token into a full column.

    This exception is raised when a player tries to drop a token into a column
    that is already full in the Connect Four game.

    Attributes
    ----------
    message : str
        A message describing the error.
    """

    def __init__(self, message="Column is full of tokens"):
        """
        Initializes a new instance of the ColumnFullError class.

        Parameters
        ----------
        message : str, optional
            A message describing the error. Default is "Column is full of tokens".
        """
        self.message = message
        super().__init__(self.message)
