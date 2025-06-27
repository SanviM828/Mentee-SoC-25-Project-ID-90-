# Snake Game – Classic Arcade Style (SoC'25)

This is a simple Snake game I built as part of **SoC’25 (Summer of Code 2025)**. It’s a recreation of the classic arcade-style Snake game, developed using Python and `pygame`. The project helped me understand game loops, event handling, object movement, and collision detection in a fun and hands-on way.

## Objective:
The objective of this project was to recreate the classic Snake game using Python, as part of the SoC’25 learning journey. This involved learning about:
- Game loops  
- Event handling  
- Object movement  
- Collision detection

## Tools Used:
- **Programming Language**: Python  
- **Library**: `pygame`  
- **IDE**: VS Code  

## Game Description:
The Snake Game is a simple arcade-style game where the player controls a snake that moves around the screen, eating food to grow longer.  
The game ends when the snake collides with the walls or itself.

## Features Implemented:
- **Snake Movement**: Controlled using arrow keys. The snake continuously moves in the current direction and turns based on user input.  
- **Food Generation**: Food appears at random positions. Eating food increases the snake’s length.  
- **Score Tracking**: Score is displayed and increases each time food is eaten.  
- **Game Over Condition**: Game ends if the snake hits the wall or itself.  
- **Restart Option**: Press `R` to restart after Game Over.  
- **Exit Option**: Press `Esc` to quit after Game Over.

## Learning Outcomes:
- Learned **Python** basics and structure  
- Got hands-on experience with **pygame** and its event loop  
- Learned how to handle **user input**, **game logic**, and **collision detection**  
- Understood how to manage different **game states** (running, game over, restart)  
- Practiced debugging and improving real-time interactive programs

## Challenges Faced:
- Ensuring smooth movement without frame skips  
- Handling self-collision accurately  
- Managing snake growth and turn logic without bugs

## Conclusion:
This project helped reinforce the basics of Python programming while introducing me to game development concepts.  
It was fun to build and debug, and it definitely felt like a great starting point for more advanced graphical or interactive projects in the future.


## How to Run
1. Make sure Python 3 is installed.
2. Install `pygame` if not already installed:

```bash
pip install pygame
```
Run the game:
```bash
python snake.py
```
