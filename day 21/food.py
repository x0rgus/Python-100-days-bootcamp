from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self, xrange : int, yrange: int) -> None:
        self.maxrangex = xrange / 2 - 10
        self.maxrangey = yrange / 2 - 10
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x =  random.randint(-int(self.maxrangex), int(self.maxrangex))
        random_y =  random.randint(-int(self.maxrangey), int(self.maxrangey))
        self.goto(random_x, random_y)        


