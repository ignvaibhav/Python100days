from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

w = 1280
h = 720

screen = Screen()
screen.setup(w, h)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if scoreboard.score > 5:
        scoreboard.sir()
    
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        
        
    if snake.head.xcor() > (w/2)-20 or snake.head.xcor() < -(w/2)+20 or snake.head.ycor() > (h/2)-20 or snake.head.ycor() < -(h/2)+20:
        gameIsOn = False
        scoreboard.gameOver()
    
    
screen.exitonclick()