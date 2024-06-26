from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "X")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()