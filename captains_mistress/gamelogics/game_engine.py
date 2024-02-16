import random

from captains_mistress.gamecomponents import computer_opponent
from captains_mistress.gamecomponents.gametoken import GameToken
from captains_mistress.gamecomponents.gameboard import GameBoard
from captains_mistress.exceptions.columnfullerror import ColumnFullError


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

    def play_two_players(self) -> None:
        """
        Starts a two-player game.

        Returns
        -------
        None
            This method does not return anything.
        """
        print("------------------------------")
        print("Game Start 1vs1: ")
        print("------------------------------")
        max_moves = self.game_board.cols * self.game_board.rows
        number_of_moves = 0
        while number_of_moves < max_moves:
            input_column = input(f"Player {str(self.current_player)} enter column: ")
            is_valid_game_move = self.game_move(input_column)
            if is_valid_game_move:
                self.game_board.print_board()
                if self.game_board.check_winner():
                    print(f"Winner is {str(self.current_player)}")
                    return
                self.switch_player()
                number_of_moves += 1
        print("Game is a draw!")

    def game_move(self, input_column: str) -> bool:
        """
        Processes a game move.

        Parameters
        ----------
        input_column : str
            The column where the current player wants to drop a token.

        Returns
        -------
        bool
            True if the move is valid, False otherwise.
        """
        try:
            self.game_board.drop_token(int(input_column), self.current_player)
            return True
        except ValueError:
            print("Please enter a valid column number!")
        except IndexError:
            print("Please enter a valid column number!")
        except ColumnFullError:
            print("Column is full of tokens")
        return False

    def play_against_computer(self):
        """
        Starts a game against the computer.

        Returns
        -------
        None
            This method does not return anything.
        """
        print("------------------------------")
        print("Game Start against Computer: ")
        print("------------------------------")
        max_moves = self.game_board.cols * self.game_board.rows
        number_of_moves = 0
        computer_player = random.choice([GameToken.RED, GameToken.YELLOW])
        while number_of_moves < max_moves:
            if self.current_player == computer_player:
                col = computer_opponent.find_best_move(self.game_board, computer_player)
                is_valid_game_move = self.game_move(col)
            else:
                input_column = input(f"Player {str(self.current_player)} enter column: ")
                is_valid_game_move = self.game_move(input_column)

            if is_valid_game_move:
                self.game_board.print_board()
                if self.game_board.check_winner():
                    if computer_player == self.current_player:
                        print(f"Computer won! Better luck next time!")
                    else:
                        print(f"Congratulations, you won!")
                    return
                self.switch_player()
                number_of_moves += 1
        print("Game is a draw!")


if __name__ == "__main__":
    game_engine = GameEngine()
    print("Captains Mistress")
    print("[0] - 2 Players ")
    print("[1] - Play against computer ")
    print("Press any other button to quit")
    selection = input("Your choice: ")
    if selection == '0':
        game_engine.play_two_players()
        pass
    elif selection == '1':
        game_engine.play_against_computer()
        pass
    print("Goodbye!")
    pass