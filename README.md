# Pacman Game

This project is a simple implementation of the classic Pacman game using Python and the Pygame library. The game features Pacman navigating a maze, collecting dots, and avoiding ghosts.

## Features

- Pacman moves through a maze collecting points.
- Ghosts chase Pacman in random directions.
- Game ends with a win when all dots are collected.
- Game ends with a loss if Pacman collides with a ghost.

## How to Run

### Prerequisites

- Python 3.x installed on your machine.
- Pygame library installed. You can install it using pip:
  ```
  pip install pygame
  ```

### Running the Game

1. Save the script into a Python file (e.g., `pacman.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script:
   ```
   python pacman.py
   ```

## Controls

- **Arrow Keys**: Move Pacman up, down, left, or right.

## Rules

- Collect all the dots (small white circles) to win the game.
- Avoid collisions with the ghosts, as it results in a loss.

## Code Structure

### Main Components

- **Pacman**: The player character, represented by a yellow circle.
- **Ghosts**: Enemy characters, represented by circles of various colors.
- **Maze**: Static grid layout with walls (`#`) and paths (`.`).
- **Game Logic**:
  - Collision detection for Pacman and ghosts.
  - Score tracking based on collected dots.
  - Game-over and victory conditions.

### Key Functions

- `is_wall(x, y)`: Checks if a given coordinate corresponds to a wall.
- `check_game_end()`: Verifies if all dots have been collected.
- `update()`: Updates the positions of Pacman and ghosts.
- `draw()`: Renders the maze, characters, and score on the screen.

## Customization

- **Maze Layout**: Modify the `LEVEL` variable to change the maze design.
- **Ghost Behavior**: Customize ghost movement logic in the `Ghost` class.
- **Pacman Speed**: Adjust the `speed` attribute of the `Pacman` class.

## Screenshots

<p><img align="center" alt="png" width="800" src="https://github.com/suleymanovdev/pypacman/blob/main/screenshot.png"/></p>

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Inspired by the classic Pacman game developed by Namco.
- Built with the Pygame library for Python.

