from turtle import Screen, Turtle
from snake import Snake
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

segments = []

snake = Snake()

game_is_on = True
# Move Snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
