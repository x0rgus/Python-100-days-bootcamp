from turtle import Turtle, Screen
import random

colors = ["red", "blue", "green", "yellow", "purple", "black", "orange"]
t1 = Turtle()
t1.shape("classic")
DEFAULT_WALK = 25


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

for x in range(100):
    t1.color(random.choice(colors))
    random.choice(list_moves)()

screen = Screen()
screen.exitonclick()