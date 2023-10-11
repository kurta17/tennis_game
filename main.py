import turtle as t
from ball import Ball
from line import Lines
from paddle import Paddle
import time

ball = Ball()
line = Lines()
paddle_left = Paddle(-370,0)
paddle_right = Paddle(370,0)


screen= t.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")




line.drow_line()

while True:
    screen.update()
    time.sleep(0.1)
    if ball.distance(paddle_left) < 20 or ball.distance(paddle_right) < 20:
        ball.bounce_wall()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor()< - 280:
        ball.bounce_wall()
    
    
    

screen.exitonclick()