import unittest

from captains_mistress.exceptions.columnfullerror import ColumnFullError
from captains_mistress.gamecomponents.gameboard import GameBoard
from captains_mistress.gamecomponents.gametoken import GameToken


class TestGameBoard(unittest.TestCase):
    """
    Test case for the Connect Four game board.

    This class contains unit tests for the methods of the GameBoard class.

    Methods
    -------
    setUp()
        Set up the test case with a new instance of the GameBoard.
    test_reset_gameboard()
        Test the reset_gameboard method of the GameBoard class.
    test_drop_token_valid_column()
        Test the drop_token method with a valid column index.
    test_drop_token_full_column()
        Test the drop_token method with a full column.
    test_drop_token_invalid_column_index()
        Test the drop_token method with an invalid column index.
    test_no_winner()
        Test the check_winner method when there is no winner.
    test_horizontal_winner()
        Test the check_winner method for a horizontal winner.
    test_vertical_winner()
        Test the check_winner method for a vertical winner.
    test_diagonal_winner()
        Test the check_winner method for a diagonal winner.
    test_no_winner_partial_board()
        Test the check_winner method when the game is not over.

    """

    @classmethod
    def setUp(self):
        """
        Set up the test case with a new instance of the GameBoard.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.game_board = GameBoard(6, 7)

    def test_reset_gameboard(self):
        """
        Test the reset_gameboard method of the GameBoard class.

        This method checks if the game board is reset to all empty tokens.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.game_board.reset_gameboard()
        # Check if the board is reset to all empty tokens
        for row in self.game_board.board:
            for token in row:
                self.assertEqual(token, GameToken.EMPTY)

    def test_drop_token_valid_column(self):
        """
        Test the drop_token method with a valid column index.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.assertTrue(self.game_board.drop_token(0, GameToken.RED))

    def test_drop_token_full_column(self):
        """
        Test the drop_token method with a full column.

        Returns
        -------
        None
            This method does not return anything.
        """
        # Fill a column with tokens
        for _ in range(self.game_board.rows):
            self.game_board.drop_token(0, GameToken.YELLOW)
        with self.assertRaises(ColumnFullError):
            self.game_board.drop_token(0, GameToken.RED)

    def test_drop_token_invalid_column_index(self):
        """
        Test the drop_token method with an invalid column index.

        Returns
        -------
        None
            This method does not return anything.
        """
        # Test dropping a token into an invalid column index
        with self.assertRaises(IndexError):
            self.game_board.drop_token(7, GameToken.RED)

    def test_no_winner(self):
        """
        Test the check_winner method when there is no winner.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.assertFalse(self.game_board.check_winner())

    def test_horizontal_winner(self):
        """
        Test the check_winner method for a horizontal winner.

        Returns
        -------
        None
            This method does not return anything.
        """
        # Test horizontal winner
        for col in range(4):
            self.game_board.drop_token(col, GameToken.RED)
        self.assertTrue(self.game_board.check_winner())

    def test_vertical_winner(self):
        """
        Test the check_winner method for a vertical winner.

        Returns
        -------
        None
            This method does not return anything.
        """
        # Test vertical winner
        for _ in range(4):
            self.game_board.drop_token(0, GameToken.YELLOW)
        self.assertTrue(self.game_board.check_winner())

    def test_diagonal_winner(self):
        """
        Test the check_winner method for a diagonal winner.

        Returns
        -------
        None
            This method does not return anything.
        """
        # Test diagonal winner
        for i in range(4):
            for j in range(4):
                if i == j:
                    self.game_board.drop_token(j, GameToken.RED)
        self.assertTrue(self.game_board.check_winner())

    def test_no_winner_partial_board(self):
        """
        Test the check_winner method when the game is not over.

        Returns
        -------
        None
            This method does not return anything.
        """
        # Test when the game is not over and there is no winner yet
        self.game_board.drop_token(0, GameToken.RED)
        self.game_board.drop_token(1, GameToken.YELLOW)
        self.assertFalse(self.game_board.check_winner())


if __name__ == '__main__':
    unittest.main()
