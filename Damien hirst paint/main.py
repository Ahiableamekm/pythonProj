# import colorgram
import turtle as t
import random

t.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('Damien hirst paint\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
hirst = t.Turtle()
x_loc = hirst.xcor() - 250
y_loc = hirst.ycor() - 250
hirst.pensize(10)
hirst.speed('fastest')
hirst.hideturtle()

distance_between= 50
for h in range(10):
    y_loc += distance_between
    hirst.penup()
    hirst.goto(x_loc, y_loc)
    hirst.dot()
    for r in range(10):
        hirst.color(random.choice(color_list))
        hirst.dot()
        hirst.penup()
        hirst.forward(50)
        hirst.pendown()
    



















screen = t.Screen()
screen.exitonclick()
