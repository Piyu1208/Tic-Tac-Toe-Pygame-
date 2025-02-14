# Tic-Tac-Toe Game

This project is a simple implementation of the classic Tic-Tac-Toe game using Python and the Pygame library. The game features a 3x3 grid where two players take turns marking their moves until one wins or the game ends in a draw.

## Features
- Interactive 3x3 grid.
- Two-player mode with alternating turns.
- Reset functionality to restart the game.
- Win detection for rows, columns, and diagonals.
- Draw detection when all cells are filled.

## How to Play
1. Run the program to start the game.
2. Players take turns clicking on the grid cells to make their moves.
   - Player 1 uses `X`.
   - Player 2 uses `O`.
3. The game will automatically detect if a player wins or if the game ends in a draw.
4. Press `Enter` to reset the game and start over.

## Requirements
- Python 3.7 or later
- Pygame library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Code Overview

### Key Components
- **Grid Initialization**
  The grid is represented as a 2D list where numbers correspond to each cell. The `positions` dictionary maps cell numbers to their respective coordinates on the screen.

- **Game Logic**
  - `assign_values_to(grid, moves1, moves2)`: Updates the grid based on the players' moves.
  - `winner(grid, count)`: Checks if a player has won based on the current state of the grid.
  - `draw(grid)`: Checks if the game ends in a draw.

- **Reset Functionality**
  The `reset_game` function resets all variables to their initial state, allowing players to restart the game by pressing `Enter`.

- **Event Handling**
  Handles player inputs for mouse clicks and key presses.

### Rendering
The `draw_window` function is used to render the game window, including the grid, player moves, and game status.

## File Structure
```
.
├── main.py          # Main script to run the game
├── README.md        # Project documentation
```



## Acknowledgments
- Developed using the [Pygame](https://www.pygame.org/) library.



---
Enjoy the game and happy coding!


