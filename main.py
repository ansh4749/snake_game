from turtle import  Screen
from snake import Snake
from food import food
from Scoreboard import scoreboard

import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=600)
screen.title("Snake game")

screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food = food()
scoreboard = scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move() 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() > 280 or snake.head.xcor()  < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segment:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()


