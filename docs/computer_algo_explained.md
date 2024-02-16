# Computer opponent explained

1. Method find_best_move() is called by game engine.
2. find_best_move() iterates over all columns and tries to drop the token in a duplicated gameboard.
3. Now the score for each move will be calculated with the minimax() algorithm.
4. Since the token for computer was already dropped in the first loop, we start with maximising=false (its the opponents turn).
5. In the first go through the best move against the computer is calculated and afterward again the move from the computer and so on.
This is creating a gametree until it is a winner or the desired depth is reached.
6. Now the score of the board is calculated with functions evaluate_board(). This function divides the field in its 'windows' group of four tokens in the board and calculates the score with evaluate_window().
7. Afterwards the score is returned to find_best_move() with the best score of all moves in the gametree.

Used this as inspiration for my minimax algorithm (without  alpha-beta pruning):
https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html

