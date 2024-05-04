from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("white")
        self.goto(-230, 250)
        self.write(f"level:{self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-230, 250)
        self.write(f"level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"game over :p", align="center", font=("Courier", 50, "normal"))
