# Pong Game

## Introduction
The provided Python script represents a classic Pong game created using the Pygame library. In the game, two players control paddles to bounce a ball back and forth. The script initializes the game, handles user input, manages game objects, and displays the game on the screen. This documentation will explain the features, Python concepts used, and the structure of the code.

## Features

### Game Setup
- The game window has a width of 1000 pixels and a height of 600 pixels, specified by `WIDTH` and `HEIGHT`.
- The ball and paddles have predefined dimensions and are loaded as images.

### Ball Class (`ball.py`)
- The `Ball` class is responsible for initializing and updating the ball's properties.
- It handles the ball's position, velocity, and rendering on the screen.
- The ball bounces off the top and bottom walls.

### Paddle Class (`paddle.py`)
- The `Paddle` class manages the paddles for two players.
- Paddles are initialized with a screen, position, and velocity.
- Paddle movement is controlled by player input.
- Paddle collision with the top and bottom walls is managed.

### Scoreboard Class (`scoreboard.py`)
- The `Scoreboard` class displays the scores for both players.
- It keeps track of each player's score.
- The scores are displayed on the screen.

### User Interaction
- Players control their paddles using the arrow keys (Player 1) and "W" and "S" keys (Player 2).
- The game detects key presses and releases to control paddle movement.
- The game window can be closed using the close button (X) in the corner.

### Game Logic
- The game loop (`while running`) controls the flow of the game.
- The ball bounces off the top and bottom walls and reverses direction when it hits a player's paddle.
- Scoring occurs when the ball goes past a paddle, and the ball is reset to the center.
- The game checks for a winning condition (e.g., one player reaching a score of 11), and a winning message is displayed.

## Python Concepts Used

- **Pygame Library:** The Pygame library is used to create the game, handle graphics, and user input.
- **Classes:** The code is structured using classes (`Ball`, `Paddle`, and `Scoreboard`) for encapsulating objects and their behavior.
- **Game Loop (`while`):** The main game loop allows continuous updates and rendering of game elements.
- **User Input Handling:** The code responds to keyboard input to control paddle movement and exit the game.
- **Image Loading:** Images for the ball and paddles are loaded and displayed.
- **Collision Detection:** The code detects collisions between the ball and paddles and handles scoring.
- **Text Rendering:** Text is rendered on the screen to display player scores and the winning message.

## Code Structure

The code is divided into three main parts:

1. **Game Setup and Initialization:** This section defines the game window, initializes game objects (ball, paddles, and scoreboards), and sets up the initial game state.

2. **Game Loop:** The core game logic is implemented within the game loop. It handles user input, updates the position and behavior of game objects, detects collisions, and manages scoring.

3. **Class Definitions:** The code is organized into three separate Python files (`ball.py`, `paddle.py`, and `scoreboard.py`) to define the classes for the ball, paddles, and scoreboards. Each class encapsulates its functionality.

## Conclusion

This Pong game is a simple yet engaging example of game development in Python using the Pygame library. It demonstrates key game development concepts such as game initialization, user input handling, object-oriented programming, collision detection, and game loop implementation. Players can enjoy a classic Pong experience with competitive scoring.
