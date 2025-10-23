from turtle import Screen
from snake import Snake
from food import Food
import time

screenwidth = 600
screenheight = 600

# Snake Setup
snake = Snake(debug=True)
snake.create_snake()

# Food setup

food = Food(screenwidth, screenheight)

# Screen setup

screen = Screen()
screen.setup(screenwidth, screenheight)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
REFRESHRATE = 0.1
screen.listen()

# Game configs
def tickrate():
    screen.update()
    time.sleep(REFRESHRATE)

    if snake.segments[0].distance(food) < 15:
        print("nom nom nom ")
        food.refresh()


screen.onkeypress(fun=lambda: snake.turn(direction="Left"), key="a")

screen.onkeypress(fun=lambda: snake.turn(direction="right"), key="d")

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
