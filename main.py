import turtle as t
from ball import Ball
from line import Lines
from paddle import Paddle
from score_board import Score_Left
from score_board import Score_Right
from score_board import Score
import time

ball = Ball()
line = Lines()
paddle_left = Paddle(-350,0)
paddle_right = Paddle(350,0)
score_l = Score_Left()
score_r = Score_Right()


screen= t.Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")

def quit_game():
    print("goodbye")
    screen.bye()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(quit_game, key= "q")

line.drow_line()

        
def move_left_paddle(): 
    if ball.ycor() > paddle_left.ycor():
        paddle_left.move_up() 
    elif ball.ycor() < paddle_left.ycor():
        paddle_left.move_down()

while True:
    screen.tracer(0)
    screen.update()
    time.sleep(0.05)

    if ball.distance(paddle_right) < 62 and ball.xcor() > 330 and paddle_right.xcor() > ball.xcor() or ball.distance(paddle_left) < 62 and ball.xcor() < -330 and paddle_left.xcor() < ball.xcor():
        ball.bounce_paddle()

    ball.move_ball()
    
    if ball.ycor() > 280 or ball.ycor()< - 280:
        ball.bounce_wall()
        
    elif ball.xcor() > 400:
        screen.tracer(1)
        score_l.game_over(screen.update)
        ball.goto(0,0)
        score_l.score +=1
        score_l.print_score()
        score_r.print_score()
        screen.tracer(0)
        screen.update()
    elif ball.xcor() < -400:
        screen.tracer(1)
        score_l.game_over(screen.update)
        ball.goto(0,0)
        score_r.score += 1
        score_r.print_score()
        score_l.print_score()
        screen.tracer(0)
        screen.update()
    move_left_paddle()


    

        

    
    
    

screen.exitonclick()