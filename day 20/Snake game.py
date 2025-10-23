from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
REFRESHRATE = 0.4

#game configs
def tickrate():
    screen.update()
    time.sleep(REFRESHRATE)


snake = Snake()
snake.create_snake()

game_is_on = True

while game_is_on:
    
    snake.move()
    tickrate()
    
    





screen.exitonclick()
