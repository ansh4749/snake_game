from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.write(f"score: {self.score} ", align="center", font=("Ariel",20,"bold"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score} ", align="center", font=("Ariel", 20, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(" GAME OVER! ", align="center", font=("Ariel", 20, "bold"))