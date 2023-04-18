from turtle import Turtle


class Paddle(Turtle):
    """
    A class that is responsible for creating a paddle object
    and providing methods for moving it up and down on the screen.

    This class inherits from the Turtle class.

    Attributes:
    position (tuple): The initial x and y coordinates of the paddle as a tuple (x, y).
    """
    def __init__(self, position):
        """Initializes the Paddle object with a shapesize of 5 squares,
        and sets up its color and position on the game screen."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddle up by 20 units."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down by 20 units."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
