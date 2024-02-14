import random
from captains_mistress.gamecomponents.gametoken import GameToken
from captains_mistress.gamecomponents.gameboard import GameBoard

class GameEngine:
    """
    Manages the game logic and flow for Connect Four.

    This class handles the game mechanics, including player turns, moves, and win conditions.

    Attributes
    ----------
    game_board : GameBoard
        The game board object.
    current_player : GameToken
        The current player's token.

    Methods
    -------
    switch_player()
        Switches the current player.
    play_two_players()
        Starts a two-player game.
    play_against_computer()
        Starts a game against the computer.
    game_move(input_column: str) -> bool
        Processes a game move.
    """

    def __init__(self):
        """
        Initializes a new instance of the GameEngine class.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.game_board = GameBoard(6, 7)
        self.current_player = random.choice([GameToken.RED, GameToken.YELLOW])

    def switch_player(self) -> None:
        """
        Switches the current player.

        Returns
        -------
        None
            This method does not return anything.
        """
        if self.current_player == GameToken.RED:
            self.current_player = GameToken.YELLOW
        else:
            self.current_player = GameToken.RED

if __name__ == "__main__":
    game_engine = GameEngine()
    print("Captains Mistress")
    print("[0] - 2 Players ")
    print("[1] - Play against computer ")
    print("Press any other button to quit")
    selection = input("Your choice: ")
    if selection == '0':
        #game_engine.play_two_players()
        pass
    elif selection == '1':
        #game_engine.play_against_computer()
        pass
    print("Goodbye!")
    pass