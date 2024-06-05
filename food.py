from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.x_random = random.randint(-280, 280)
        self.y_random = random.randint(-280, 280)
        self.goto(x=self.x_random, y=self.y_random)
        self.food_score = 0
        self.refresh()

    def refresh(self):
        self.x_random = random.randint(-280, 300)
        self.y_random = random.randint(-280, 300)
        self.goto(x=self.x_random, y=self.y_random)





