import turtle as t
from ball import Ball
from line import Lines
from paddle import Paddle
from score_board import Score_Left
import time

ball = Ball()
line = Lines()
paddle_left = Paddle(-350,0)
paddle_right = Paddle(350,0)
score_l = Score_Left()

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
    time.sleep(0.05)
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor()< - 280:
        ball.bounce_wall()
    
    
    

screen.exitonclick()