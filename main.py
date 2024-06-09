from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBored
import time

screen = Screen()
screen.tracer(0)
screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBored()

screen.bgcolor("black")
screen.title("BOUNCING BALL GAME ")
screen.setup(width=800, height=600)
game_is_on = True
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while game_is_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    ball.bounce_y()
    # detect the collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 40 and ball.xcor() > -360:
        ball.bounce_x()
        ball.ball_speed *= 0.9



    if ball.xcor() > 400:
        score_board.left_point()
        ball.change_direction()

    if ball.xcor() < -400:
        score_board.right_point()
        ball.change_direction()
        ball.ball_speed = 0.1


screen.exitonclick()
