# Task allocations for project captain's mistress
Project contributors: Stefan Ebner, Paul Weiss

### Setup project / Organisation
- [X] Create git repository - Paul Weiss
  - Create git repository for the project captains mistress on https://github.com/p4ulweiss/sem_captains_mistress/tree/main/docs
  - Commit: 166289e
- [X] Add .gitignore File - Stefan Ebner
  - Generate a .gitignore file
  - Commits: 79ad816, 5b8a704 
- [X] Create task allocations - Paul Weiss
  - Create a markdown file task allocations
  - Commits: 5b8a704, 7524605, 525067f
- [X] Planing of project - Paul Weiss
  - Write about what classes we need to implement captains mistress
  - Include a diagram for class description (not UML standard)
  - Commit: aa1e3f4, 0a83213
- [X] Create project structure - Paul Weiss
  - Create python packages to store code and documentation
  - Commits: d485d0d

### Basic game
- [X] Create game token class - Paul Weiss
  - Enum containing three states (RED, YELLOW, EMPTY)
  - Commits: 3facacb
- [X] Create game board class - Paul Weiss
  - Constructor which creates gameboard with empty tokens
  - Implement method to reset a gameboard
  - Commits: 3facacb
- [X] Create game engine class - Stefan Ebner
  - With attributes _current_player_ and _gameboard_
  - Method to switch between players
  - Start menu to choose playing mode
  - Commits: 026da25
- [X] Create drop token method - Paul Weiss
  - Method to make a game move
  - Validating move with exceptions
  - Custom exception ColumnFull
  - Commits: 4e86f54
- [X] Show gameboard - Paul Weiss
  - Drawing method in gameboard
  - With colors using color codes
  - Commits: 48051c0
- [X] Check winner method - Paul Weiss
  - Check winner method in gameboard class
  - Analyzing all directions to check if 4 in a row
  - Commits: 48051c0
- [X] 1 vs 1 mode - Stefan Ebner
  - Implement method for playing
  - Use make_move method to catch invalid game moves
  - Commits: c5698bc


### Testing
- [X] Test gameengine class - Stefan Ebner
  - Unit test for switchplayer
  - Commits: 0811df3 (Wrong commit message)
- [X] Test gameboard class - Paul Weiss
  - Unit test for check_winner()
  - Unit test for drop_token()
  - Commits: 5b43e76

### Creating computer opponent
- [X] Create module for calculating best move - Paul Weiss
  - Implement minimax algorithm
  - Adding description on how the best move is found
  - Commits: dbd7cd5
- [X] Integrate computer opponent into game engine - Paul Weiss
  - Writing method for playing vs computer in game engine
  - Commits: f3a1d26

#### Design Pattern Explanations
- [X] Add a design pattern explanation - Stefan Ebner
  - Describe singleton pattern
  - Commit: 94496bf
- [X] Add a second design pattern explanation - Paul Weiss
  - Describe Observer pattern
  - Commit: 89698a5

#### Software Design Theory Question
- [X] Add the answer to the software design theory question - Stefan Ebner
  - Commit: 533eabb

### Readme.md
- [X] Create instructions on how to play - Stefan Ebner
  - Commit: 38a5266