from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.heading()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.left(90)
        self.color('black')

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)