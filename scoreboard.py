from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-280,y=270)
        self.Level = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Level:{self.Level}",align='left',font=('Arial',17,'normal'))

    def increase_level(self):
        self.Level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(arg= f"GAME OVER",align='center',font=('Arial',17,'normal'))

