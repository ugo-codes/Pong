from turtle import Turtle
import random


class Ball:

    def __init__(self):
        self.ball = None
        self.create_ball()
        self.directions = ["-", "+"]
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()

    def set_ball_heading(self):
        self.ball.setheading(random.randint(45, 270))

    def move(self):
        x_cor = self.ball.xcor()
        y_cor = self.ball.ycor()
        self.ball.goto(x_cor + self.x_direction, y_cor + self.y_direction)

    def change_x_direction(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def change_y_direction(self):
        self.y_direction *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.ball.goto(0, 0)
        self.move_speed = 0.1
