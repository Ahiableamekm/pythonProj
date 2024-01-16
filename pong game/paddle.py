from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(coords)


    def up(self):
        x_position = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x=x_position, y=new_y)


    def down(self):
        x_position = self.xcor()
        new_y = self.ycor() - 20
        self.goto(x=x_position, y=new_y)
