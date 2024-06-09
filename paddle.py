from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize( stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=position[0], y=position[1])

    def go_up(self):
        x_cor = self.xcor()
        self.goto(x=x_cor, y=self.ycor()+20)
    def go_down(self):
        x_cor = self.xcor()
        self.goto(x=x_cor, y=self.ycor()-20)







