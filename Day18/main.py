from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(100)
def draw_spriograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spriograph(5)

screen = Screen()
screen.exitonclick()


# colours = ['red', 'yellow', 'violet', 'green', 'blue', 'black']
# direction = [0,90,180,270]
# tim.pensize(10)
# tim.speed(10)
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         steps = int(100)
#         angle = int(angle)
#         tim.right(angle)
#         tim.forward(steps)
#         tim.fillcolor()
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

