# Snake.py

from turtle import Turtle

# Define constants for directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg_num - 1].xcor()
            y_new = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_new, y_new)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def collided_with_body(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def collided_with_wall(self):
        if (
                self.head.xcor() > 280 or self.head.xcor() < -280 or
                self.head.ycor() > 280 or self.head.ycor() < -280
        ):
            return True
        return False
