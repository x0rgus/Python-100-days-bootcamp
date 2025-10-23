from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

# Snake Setup
snake = Snake(debug=True)
snake.create_snake()

# Screen setup
screenwidth = 1920
screenheight = 1080
screen = Screen()
screen.setup(screenwidth, screenheight)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
REFRESHRATE = 0.4
screen.listen()

# Game configs
def tickrate():
    screen.update()
    time.sleep(REFRESHRATE)


screen.onkeypress(fun=lambda: snake.turn(direction="Left"), key="a")

screen.onkeypress(fun=lambda: snake.turn(direction="right"), key="d")

game_is_on = True
food = Food(screenwidth, screenheight)
while game_is_on:
    snake.move()
    tickrate()

""" test to see if die function works
for x in range(0,20):  
    snake.move()
    tickrate()
    if x > 10:
        snake.die()
"""
    
    





screen.exitonclick()
