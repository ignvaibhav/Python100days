from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
    
    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.color("red")
        self.write(f"Game Over", align="center", font=("Arial", 50, "bold"))