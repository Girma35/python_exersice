import random
from turtle import Turtle,Screen
jimmy = Turtle()
screen = Screen()
screen.colormode(255)
jimmy.penup()
jimmy.speed("fastest")
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241),
              (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183),
              (178, 198, 202), (112, 139, 141), (254, 194, 0)]


def dot(number_of_dot):
    number_of_line = int(number_of_dot / 10)
    for _ in range(2*number_of_line):
        color = random.choice(color_list)
        jimmy.dot(20, color)
        jimmy.forward(50)
        jimmy.dot(20, color)


def right():
    jimmy.setheading(90)
    jimmy.forward(50)
    jimmy.setheading(0)


def left():
    jimmy.setheading(90)
    jimmy.forward(50)
    jimmy.setheading(180)


def all_in_one(number_of_dot):
    dots = int(number_of_dot/2)
    jimmy.setheading(225)
    jimmy.forward(310)
    jimmy.setheading(0)
    jimmy.hideturtle()
    for _ in range(5):
        dot(dots)
        left()
        dot(dots)
        right()


all_in_one(100)

screen.exitonclick()
