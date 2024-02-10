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
def draw_spirograph(size):
    for x in range(int(360 / size)):
        t1.color(get_random_color())
        t1.left(size)
        t1.circle(150)

for x in reversed(range(1,360, 10)):
    draw_spirograph(x)



screen = Screen()
screen.exitonclick()