from turtle import Turtle
import random

tim = Turtle()
colours = ['red', 'yellow', 'violet', 'green', 'blue']
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        steps = int(100)
        angle = int(angle)
        tim.right(angle)
        tim.forward(steps)
        tim.fillcolor()
for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
