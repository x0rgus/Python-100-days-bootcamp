from turtle import Turtle

class ScoreTurtle(Turtle):
    def __init__(self, xrange: int, yrange: int) -> None:
        super().__init__()
        # self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.ylocation = yrange / 2 - 20

        self.teleport(xrange , self.ylocation)
    def addscore(self):
        self.score =+ 1
    def update(self):
        self.write(arg=self.score)
