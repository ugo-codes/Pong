from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Favourite Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

x_direction = "+"
y_direction = "+"

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the wall
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.change_y_direction()

    # Detect collision with paddle
    if ball.ball.distance(r_paddle.paddle) < 50 and ball.ball.xcor() > 320\
            or ball.ball.distance(l_paddle.paddle) < 50 and ball.ball.xcor() < -320:
        ball.change_x_direction()

    # Detect right paddle miss
    if ball.ball.xcor() > 380:
        ball.reset_position()
        ball.change_x_direction()
        scoreboard.increase_l_point()

    # Detect left paddle miss
    if ball.ball.xcor() < -380:
        ball.reset_position()
        ball.change_x_direction()
        scoreboard.increase_r_point()

screen.exitonclick()
