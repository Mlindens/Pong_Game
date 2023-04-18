# Pong Game

This is a simple implementation of the classic Pong game using the Python Turtle Graphics library.

## Game Overview
Pong is a two-player arcade game in which the players control paddles to hit a moving ball back and forth across the screen. The goal is to make the ball pass the opponent's paddle to score a point. The player with the highest score wins.


![screenshot](https://user-images.githubusercontent.com/83295029/232910393-68f92776-2e72-403e-b3b2-040f1da11992.PNG)

## Getting Started!
These instructions will help you get the game up and running on your local machine.

## Dependencies
To run this game, you will need:

* Python 3.x or higher.

## Installation
Clone the repository to your local machine:
```
git clone https://github.com/mlindens/Pong_Game.git
```
Navigate to the folder containing the source files in your terminal or command prompt.
```
cd Pong_Game
```
Run the following command:
```
python main.py
```
The game window will open, and you can start playing.

## How to Play
Right paddle:
* Up: Up arrow key
* Down: Down arrow key
Left paddle:
* Up: 'w' key
* Down: 's' key

## Game Components
This implementation of Pong consists of the following components:

* Paddle: A class representing the paddles that the players control. Each paddle can move up and down using the specified controls.
* Ball: A class representing the ball that moves across the screen and bounces off the paddles and walls.
* Scoreboard: A class representing the scoreboard that keeps track of each player's score and displays it on the screen.
* These components are imported into the main.py script, which sets up the game window, initializes the game objects, and manages the main game loop.

### Built With
* [Python](http://www.python.org)
* [Turtle graphics library](https://docs.python.org/3/library/turtle.html)


### Acknowledgments
* The original Pong game, which inspired this implementation.
* The Python and Turtle documentation for providing valuable resources and examples.
