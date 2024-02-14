# Project planing
Initial planing of the project. 

## What classes do we need?

- **Game board**
  - Contains the field itself and methods to manipulate and check for winners
  - Attributes:
    - rows, cols and the field[][]
  - Methods:
    - reset_board()
    - check_winner()
    - drop_token()
- **Player**
  - A player object which is created at the game start
  - Attributes:
    - name, token
- **Game engine**
    - Class which controlls the flow of the game
    - Attributes:
      - gameboard, players
    - Methods:
      - startgame()
      - switch_player()
- **UI**
  - Controlls all outputs and inputs
  - Methods:
    - display_board()
    - display_start_menu()
- **For computer opponent**: functions to determine best move
  - Takes a gameboard and calculates the best move for computer opponent

## What changed during developing?
First, we decided to use a enum gametoken to manage the state of each slot. 
It controlls whether it is YELLOW, RED or EMPTY. 
Moreover, we decided to drop the player class and just use Yellow or Red to identify who has the next move.
Another difference to the initial planing is the UI class. Since everything is managed in GameEngine input is made here.
The display_board() function is now part of the board like a to_string function. 
Furthermore, we added a custom exception in case a column is full with tokens. 







