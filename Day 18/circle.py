import turtle
from turtle import Turtle, Screen
import random

t1 = Turtle()
t1.shape("classic")
DEFAULT_WALK = 25
turtle.colormode(255)
colors = []
t1.pensize(1)
t1.speed("fastest")


def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

for x in range(360):
    t1.color(get_random_color())
    t1.left(1)
    t1.circle(150)


screen = Screen()
screen.exitonclick()