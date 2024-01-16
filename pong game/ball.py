from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        """
        Moves the ball on the screeen
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)



    def bounce_y(self):
        """
        Reverse the ball in opposite direction after collision with wall
        """
        self.y_move *= -1


    def bounce_x(self):
        """
        Reverse the ball in opposite direction after collision with Paddles
        """
        self.x_move *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        """
        Send the ball back to the starting point
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


        

        
        