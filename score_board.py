
from turtle import Turtle


class ScoreBored(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.score =0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.penup()
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        score = max(self.l_score, self.r_score)
        self.score = score
        self.hideturtle()

    def right_point(self):
        self.r_score += 1
        self.update_score_board()


    def left_point(self):
        self.l_score += 1
        self.update_score_board()

















