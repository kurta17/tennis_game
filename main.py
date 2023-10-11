import turtle as t
from ball import Ball
import time

screen= t.Screen()
screen.setup(800,600)
screen.bgcolor("black")

ball = Ball()

while True:
    time.sleep(0.2)
    ball.move_ball()

screen.exitonclick()