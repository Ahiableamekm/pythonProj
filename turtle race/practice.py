import turtle as t

tom = t.Turtle()
screen = t.Screen()



def move_forward():
    tom.forward(20)



screen.onkey(move_forward, 'space')
screen.listen()





















screen.exitonclick()