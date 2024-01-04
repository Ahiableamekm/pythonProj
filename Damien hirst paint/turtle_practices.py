from turtle import Turtle, Screen, colormode

import random
tom_turtle = Turtle()
colormode(255)
# drawing a square with turtle
# tom_turtle.forward(100)
# tom_turtle.right(90)
# tom_turtle.forward(100)
# tom_turtle.right(90)
# tom_turtle.forward(100)
# tom_turtle.right(90)
# tom_turtle.forward(100)

# drawing a score with turtle
# for _ in range(4):
#     tom_turtle.forward(100)
#     tom_turtle.right(90)


# drawing a dashline
# for _ in range(15):
#     tom_turtle.forward(10)
#     tom_turtle.penup()
#     tom_turtle.forward(10)
#     tom_turtle.pendown()


# drawing multiple sided shapes
# colors = ['coral', 'cyan', 'green', 'khaki', 'purple', 'orange', 'blue', 'turquiose']
# for sides in range(3, 11):
#     tom_turtle.color(random.choice(colors))
#     for _ in range(sides):
#         tom_turtle.forward(100)
#         tom_turtle.right(360/sides)


# makeing random walks

# tom_turtle.pensize(5)
# movement = [tom_turtle.forward(15), tom_turtle.backward(15), ]
# for _ in range(100):
#     random.choice(movement)

# drawing a spiral
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         tom_turtle.color(c)
#         tom_turtle.forward(steps)
#         tom_turtle.right(30)






colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tom_turtle.pensize(5)
tom_turtle.speed('fastest')
directions = [0, 90, 180, 270]



# random walk 1
# for i in range(100):
#     steps = random.choice([-15, 15])
#     angles = random.choice([-90, 90])
#     tom_turtle.color(random.choice(colours))
#     tom_turtle.right(angles)
#     tom_turtle.forward(steps)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# random walk 2
# for _ in range(200):
#     tom_turtle.color(random_colors())
#     tom_turtle.forward(30)
#     tom_turtle.setheading(random.choice(directions))


for _ in range(73):
    tom_turtle.color(random_colors())
    tom_turtle.circle(100)
    tom_turtle.setheading(_*5)











screen = Screen()
screen.exitonclick()