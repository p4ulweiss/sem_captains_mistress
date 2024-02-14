import unittest

from captains_mistress.gamecomponents.gametoken import GameToken
from captains_mistress.gamelogics.game_engine import GameEngine


class TestGameLogic(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.game_engine = GameEngine()

    def test_switch_player(self):
        self.game_engine.current_player = GameToken.RED
        self.game_engine.switch_player()
        self.assertEqual(self.game_engine.current_player, GameToken.YELLOW)
        self.game_engine.switch_player()
        self.assertEqual(self.game_engine.current_player, GameToken.RED)

if __name__ == '__main__':
    unittest.main()
