from turtle import Turtle


class Paddle:

    def __init__(self, position):
        self.paddle = None

        self.create_new_turtle(position)

    def create_new_turtle(self, position):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.goto(position)

    def up(self):
        self.paddle.forward(20)

    def down(self):
        self.paddle.backward(20)
