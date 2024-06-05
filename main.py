from turtle import Screen
from Snake import Snake
from food import Food
from score_board import ScoreBoard
import time

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
food = Food()
screen.listen()
screen.title("my snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Define level speeds and score thresholds
levels = {
    "level1": {"speed": 0.3, "threshold": 30},
    "level2": {"speed": 0.2, "threshold": 60},
    "level3": {"speed": 0.1, "threshold": 80}
}

game_is_on = True

level = "level1"  # Start with level 1
snake = Snake()
score_board = ScoreBoard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(levels[level]["speed"])  # Adjust speed based on the current level
    snake.move()

    # Check for collisions with the snake's own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Check for collision with walls
    if (
            snake.head.xcor() > 290 or
            snake.head.xcor() < -290 or
            snake.head.ycor() > 290 or
            snake.head.ycor() < -290
    ):
        game_is_on = False
        score_board.game_over()

    # Check score for level up
    if score_board.score >= levels[level]["threshold"]:
        # Check if there's a next level
        next_level = "level" + str(int(level[-1]) + 1)
        if next_level in levels:
            level = next_level

screen.exitonclick()
