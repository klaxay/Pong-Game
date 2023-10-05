from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(position)
        self.color("white")
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(self.score, align="center",font=("Courier",30,"normal"))