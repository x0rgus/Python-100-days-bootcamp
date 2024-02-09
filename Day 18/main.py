from turtle import Turtle, Screen
import random
colors = ["red","blue","green","yellow","purple"]
t1 = Turtle()
t1.shape("classic")
t1.color("red")

#square
for i in range(0,4):
    t1.forward(100), t1.right(90)

t1.reset()
#dotted lines
for i in range(0,100):
    t1.penup()
    t1.forward(1)
    if (i % 2) == 0:
        t1.pendown()
        t1.forward(1)

t1.reset()
# shape builder helper
def draw_shape(num_sides):
    angle = 360 / num_sides
    for x in range(num_sides):
        t1.forward(100)
        t1.right(angle)
# if less than 3 sides its just a line so range starts from there

for shape in range(3, 8):
    t1.color(random.choice(colors))
    draw_shape(shape)
    t1.reset()





screen = Screen()
screen.exitonclick()