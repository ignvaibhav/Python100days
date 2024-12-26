from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0),(-40,0)]
DISTANCE = 20

class Snake:
    def __init__(self):
          self.snake = []
          self.create_snake()
          self.head = self.snake[0]
          self.current_direction = "right"
          
    def create_snake(self):
        for position in STARTING_POSITION:
            self.addSnake(position)
            
    def addSnake(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.snake.append(new_block)
        
    def extend(self):
        self.addSnake(self.snake[-1].position())
            
    def move(self):
        for seg in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        
        self.head.fd(DISTANCE)
        
    
        
            
    def up(self):
        if self.current_direction != "down":
            self.head.setheading(90)
            self.current_direction = "up"

    def down(self):
        if self.current_direction != "up":
            self.head.setheading(270)
            self.current_direction = "down"

    def left(self):
        if self.current_direction != "right":
            self.head.setheading(180)
            self.current_direction = "left"

    def right(self):
        if self.current_direction != "left":
            self.head.setheading(0)
            self.current_direction = "right"