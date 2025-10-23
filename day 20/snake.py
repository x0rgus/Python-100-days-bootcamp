from turtle import Turtle
import logging

# logging
logging.basicConfig(
                    filename="snake.log",
                    level= logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                    )
logger = logging.getLogger(__name__)
print(logger)
class Snake():
    """Snake class with methods to create and move a snake, starts unalive by default"""
    def __init__(self, debug: bool = False ) -> None:
        self.debug = debug
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_alive = False
        self.segments = []
    def log(self, message: str):
        """Logs messages while debug is on"""
        if self.debug == True:
            logger.info(message)
    def create_snake(self):
        """Creates a snake and sets it status to alive, creates the body and appends it to the segments"""
        self.log("Creating a snake")
        self.snake_alive = True
        
        self.log("Generating segments...")
        self.log(f"Starting positions: {self.starting_positions}")
        
        for position in self.starting_positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
            
            self.log(f"[{position}]New segment created:{new_segment}")
        self.log(f"Snake created: {self.segments}")
        
    def move(self):
        """Links the segments, the first segment moves forward constantly and the rest just follows, only if snake is alive"""
        self.log("Moving snake...")

        if self.snake_alive:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)
        self.log("Done")
    def die(self):
        """Kills the snake"""
        self.log("Killing snake...")

        self.snake_alive = False

        self.log("done")
       
    def turn(self, direction):
        # turns the head
        match direction:
            case "left":
                self.segments[0].left(90)
            case "right":
                self.segments[0].right(90)
                
    
    
