from turtle import Turtle
FONT = ("Courier", 24, "normal")
LOCATION = (-220, 250)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(LOCATION)
        self.update_level()


    def update_level(self):
        """
        Update the scorebaord
        """
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def increase_level(self):
        """
        Increase the game level
        """
        self.level += 1
        self.update_level()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)