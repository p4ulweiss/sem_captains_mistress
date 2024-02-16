# Project planing
Initial planing of the project. 

## Overall project structure
Structure the project into packages and modules with their purpose.
The central elements we think of would be: gamecomponents and gamelogic. 

## What classes do we need?
We focus to implement classes in each python package for a object-oriented approach.
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
It controls whether it is YELLOW, RED or EMPTY field in the board. 
Moreover, we decided to drop the player class and just use Yellow or Red to identify who has the next move.
Another difference to the initial planing is the UI class. Since everything is managed in GameEngine input is made here.
The display_board() function is now part of the board like a to_string function. 
Furthermore, we added a custom exception in case a column is full with tokens called columnfullerror.
For the computer opponent we implemented a module with methods to determine the best move. It takes the field and gametoken as parameters and returns the best column calculated with the algorithm.