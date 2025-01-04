from turtle import Turtle, Screen
import random
import time
        

s = Screen()
s.setup(width=1280, height=720)
s.bgcolor("black")
s.tracer()

positions = [(0,0), (-20,0),(-40,0)]
snake = []
alive = True

for position in positions:
    new_block = Turtle("square")
    new_block.color("white")
    new_block.penup()
    new_block.goto(position)
    snake.append(new_block)

while alive:
    s.update()
    time.sleep(0.1)
    for seg in range(len(snake)-1, 0, -1):
        new_x = snake[seg - 1].xcor()
        new_y = snake[seg - 1].ycor()
        snake[seg].goto(new_x, new_y)
        
    snake[0].fd(20)
    snake[0].left(90)

s.exitonclick()