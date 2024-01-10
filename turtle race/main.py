import turtle as t
import random

is_race_on = False

screen = t.Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'blue', 'green' , 'purple', 'yellow']
y_positions =[-70, -40, -10, 20, 50, 80]
all_turtle = []

user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if user_bet == winning_turtle_color:
                print(f"You've won. The {winning_turtle_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_turtle_color} turtle is the winner!")

        turtle_distance = random.randint(0, 10)
        turtle.forward(turtle_distance)













screen.exitonclick()