import turtle
from turtle import Turtle, Screen
import colorgram, random
STEPSIZE = 50
DOTSROW = 10
t1 = Turtle()
t1.pensize(15)
turtle.colormode(255)
t1.speed("fastest")
t1.hideturtle()
#set initial pos
t1.penup()
t1.setheading(225)
t1.forward(350)
t1.setheading(0)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


def walk_pattern():
    for dot in range(DOTSROW):
        t1.penup()
        t1.color(random.choice(rgb_colors))
        t1.dot(20)
        t1.forward(STEPSIZE)

    t1.setheading(90)
    t1.forward(50)
    t1.setheading(180)
    t1.forward(500)
    t1.setheading(0)
rows = 10
while (rows > 0):
    walk_pattern()
    rows = rows - 1


screen = Screen()
screen.exitonclick()
print(random.choice(rgb_colors))