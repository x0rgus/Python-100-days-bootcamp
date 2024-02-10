from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

def startingsnake():
    for position in starting_positions:
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        segments.append(new_segment)


startingsnake()
game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)


screen.exitonclick()
