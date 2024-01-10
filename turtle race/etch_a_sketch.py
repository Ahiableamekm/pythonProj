import turtle as t


tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_clockwise():
    tim.right(10)


def rotate_anticlockwise():
    tim.left(10)



def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkeypress(fun=move_forward, key='w')
screen.onkeypress(fun=move_backward, key='s')
screen.onkeypress(fun=rotate_anticlockwise, key='a')
screen.onkeypress(fun=rotate_clockwise, key='d')
screen.onkeypress(fun=clear, key='c')









screen.exitonclick()
