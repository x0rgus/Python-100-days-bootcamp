import turtle
from turtle import Turtle, Screen
import random

t1 = Turtle()
t1.shape("classic")
DEFAULT_WALK = 25
turtle.colormode(255)
colors = []
t1.pensize(10)
t1.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_color_construct_list():
    for color in range(100):
        color = random_color()
        colors.append(color)


def x_up():
    t1.forward(DEFAULT_WALK)


def x_down():
    t1.back(DEFAULT_WALK)


def x_left():
    t1.left(90)
    t1.forward(DEFAULT_WALK)


def x_right():
    t1.right(90)
    t1.forward(DEFAULT_WALK)


list_moves = [x_up, x_down, x_left, x_right]

random_color_construct_list()

for x in range(1000):
    t1.color(random.choice(colors))
    random.choice(list_moves)()

screen = Screen()
screen.exitonclick()
