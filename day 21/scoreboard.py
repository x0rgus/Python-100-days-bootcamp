from turtle import Turtle

class ScoreTurtle(Turtle):
    def __init__(self, xrange: int, yrange: int) -> None:
        super().__init__()
        self.hideturtle()
        
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.xlocation = xrange / 4
        self.ylocation = yrange / 4 


        self.teleport(xrange , self.ylocation)
    def addscore(self):
        self.score = self.score + 1
    def update(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Verdana", 24, "normal"))
