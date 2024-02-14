import unittest

from captains_mistress.exceptions.columnfullerror import ColumnFullError
from captains_mistress.gamecomponents.gameboard import GameBoard
from captains_mistress.gamecomponents.gametoken import GameToken


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.game_board = GameBoard(6, 7)

    def test_reset_gameboard(self):
        self.game_board.reset_gameboard()
        # Check if the board is reset to all empty tokens
        for row in self.game_board.board:
            for token in row:
                self.assertEqual(token, GameToken.EMPTY)

    def test_drop_token_valid_column(self):
        self.assertTrue(self.game_board.drop_token(0, GameToken.RED))

    def test_drop_token_full_column(self):
        # Fill a column with tokens
        for _ in range(self.game_board.rows):
            self.game_board.drop_token(0, GameToken.YELLOW)
        with self.assertRaises(ColumnFullError):
            self.game_board.drop_token(0, GameToken.RED)

    def test_drop_token_invalid_column_index(self):
        # Test dropping a token into an invalid column index
        with self.assertRaises(IndexError):
            self.game_board.drop_token(7, GameToken.RED)

    def test_no_winner(self):
        self.assertFalse(self.game_board.check_winner())

    def test_horizontal_winner(self):
        # Test horizontal winner
        for col in range(4):
            self.game_board.drop_token(col, GameToken.RED)
        self.assertTrue(self.game_board.check_winner())

    def test_vertical_winner(self):
        # Test vertical winner
        for _ in range(4):
            self.game_board.drop_token(0, GameToken.YELLOW)
        self.assertTrue(self.game_board.check_winner())

    def test_diagonal_winner(self):
        # Test diagonal winner
        for i in range(4):
            for j in range(4):
                if i == j:
                    self.game_board.drop_token(j, GameToken.RED)
        self.assertTrue(self.game_board.check_winner())

    def test_no_winner_partial_board(self):
        # Test when the game is not over and there is no winner yet
        self.game_board.drop_token(0, GameToken.RED)
        self.game_board.drop_token(1, GameToken.YELLOW)
        self.assertFalse(self.game_board.check_winner())


if __name__ == '__main__':
    unittest.main()
