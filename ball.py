from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(3)
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.new_direction = self .xcor() * -1
        self.bounce_x()
        self.ball_speed = 0.1

    def move_ball(self):
        new_y_pos=self.ycor() + self.y_move
        new_x_pos = self.xcor() + self.x_move
        self.goto(new_x_pos, new_y_pos)

    def bounce_y(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def change_direction(self):
        self.goto(0, 0)
        self.bounce_x()















