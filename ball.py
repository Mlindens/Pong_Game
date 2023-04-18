from turtle import Turtle


class Ball(Turtle):
    """
    A class that is responsible for creating a ball object,
    moving it, and providing methods for bouncing off walls and paddles, as well as resetting
    its position.

    This class inherits from the Turtle class.

    Attributes:
    x_move (int): The amount the ball moves in the x-direction.
    y_move (int): The amount the ball moves in the y-direction.
    move_speed (float): The speed at which the ball moves.
    """
    def __init__(self):
        """Initializes the Ball object with a shape of a circle,
        and sets up its color, motion, and position on the game screen."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball by the specified x_move and y_move amounts."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        """Resets the ball's position to the center of the screen, and bounces it in the x-direction."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def bounce_y(self):
        """Reverses the ball's direction in the y-axis."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverses the ball's direction in the x-axis and speeds it up by a factor of 0.9."""
        self.x_move *= -1
        self.move_speed *= 0.9
