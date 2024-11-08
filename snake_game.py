from turtle import Turtle, Screen
from snake import Snake
from snake_food import Food
from snake_scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()

    # collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.game_over()
        game_is_on = False

    # collision with own tail
    for segment in snake.segment_list[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
