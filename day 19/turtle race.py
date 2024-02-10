import random, time
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
race = False
turtles = []

y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red","orange","yellow","green","blue","purple"]
for turtle_index in range(6):
    turt = Turtle()
    turt.shape("turtle")
    turt.penup()
    turt.color(colors[turtle_index])
    turt.speed("fastest")
    turt.teleport(x=-220, y= y_pos[turtle_index])
    turtles.append(turt)

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will the race? Enter a color:").lower()
if user_bet:
    race = True
while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! the {win_color} turtle is the winner!")

                time.sleep(2)

                exit(0)
            else:
                print(f"You've lose! the {win_color} turtle is the winner!")
                time.sleep(2)

                exit(0)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
race = False



screen.exitonclick()