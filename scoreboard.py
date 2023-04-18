from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class used to displaying and update the scoreboard of the game.

    This class inherits from the Turtle class.

    Attributes:
    l_score (int): The current score of the left player.
    r_score (int): The current score of the right player.
    """
    def __init__(self):
        """Initializes the Scoreboard object with a starting score of 0,
        and sets up its appearance and position on the game screen."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the current scoreboard and updates it with the current scores of both players."""
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        """Increments the left player's score and updates the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increments the right player's score and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()