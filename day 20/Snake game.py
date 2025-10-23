from turtle import Turtle, Screen
from snake import Snake
import time

# Snake Setup
snake = Snake()
snake.create_snake()

# Screen setup
screen = Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
REFRESHRATE = 0.4

# Game configs
def tickrate():
    screen.update()
    time.sleep(REFRESHRATE)




game_is_on = True

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
