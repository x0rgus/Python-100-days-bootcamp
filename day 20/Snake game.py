from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
REFRESHRATE = 0.1

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
#game configs
#generate starting snake
for position in starting_positions:
     new_segment = Turtle("square")
     new_segment.penup()
     new_segment.color("white")
     new_segment.goto(position)
     segments.append(new_segment)
def tickrate():
    screen.update()
    time.sleep(REFRESHRATE)
def up():
    segments[0].seth(90)
def down():
    segments[0].seth(270)
def left():
    segments[0].left(90)
def right():
    segments[0].right(90)



game_is_on = True
screen.update()
while game_is_on:
    tickrate()

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    left()



screen.exitonclick()
