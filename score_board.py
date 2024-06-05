from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score  {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.color("white")
        self.write(f"GAME OVER !! score {self.score}", align=ALIGNMENT, font=FONT)

