import unittest
from captains_mistress.game_engine import GameEngine
from captains_mistress.gamecomponents.gametoken import GameToken

class TestGameEngine(unittest.TestCase):
    """
    Test case for the Connect Four game engine.

    This class contains unit tests for the methods of the GameEngine class.

    Methods
    -------
    setUp()
        Set up the test case with a new instance of the GameEngine.
    test_switch_player()
        Test the switch_player method of the GameEngine class.
    """

    @classmethod
    def setUp(self):
        """
        Set up the test case with a new instance of the GameEngine.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.game_engine = GameEngine()

    def test_switch_player(self):
        """
        Test the switch_player method of the GameEngine class.

        This method tests the behavior of switching players.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.game_engine.current_player = GameToken.RED
        self.game_engine.switch_player()
        self.assertEqual(self.game_engine.current_player, GameToken.YELLOW)
        self.game_engine.switch_player()
        self.assertEqual(self.game_engine.current_player, GameToken.RED)

if __name__ == '__main__':
    unittest.main()
