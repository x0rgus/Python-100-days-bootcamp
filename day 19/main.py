from turtle import Turtle, Screen
print("CONTROLS:\nW = Forward\nA = left\nD = right\nS = back\n+ = Change color (numpad)\n")
tim = Turtle()
tim.shape("turtle")
colors = ["black","red","green","blue","yellow","purple","orange"]
chosen_color = 0

def color_set():
    global chosen_color
    if chosen_color < (len(colors)-1):
        chosen_color += 1
    else:
        chosen_color = 0

    tim.color(colors[chosen_color])



def move_forward():
    tim.forward(10)
def turn_left():
    tim.left(5)
def turn_right():
    tim.right(5)
def move_backward():
    tim.backward(10)






screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="plus", fun=color_set)
screen.exitonclick()