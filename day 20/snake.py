from turtle import Turtle

class Snake():
    """Snake class with methods to create and move a snake, starts unalive by default"""
    def __init__(self) -> None:
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_alive = False
        self.segments = []
    def create_snake(self):
        """Creates a snake and sets it status to alive, creates the body and appends it to the segments"""
        self.snake_alive = True
        for position in self.starting_positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def move(self):
        """Links the segments, the first segment moves forward constantly and the rest just follows"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
       
    def turn(self, direction):
        # turns the head
        match direction:
            case "left":
                self.segments[0].left(90)
            case "right":
                self.segments[0].right(90)
                
    
    
