import turtle as t
import time
class Ball(t.Turtle):
    def __init__(self, ball_speed):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.xspeed = 1
        self.yspeed = 1
        self.ball_speed = ball_speed
        
        

    def move_ball(self):
        time.sleep(self.ball_speed)
        x = self.xcor()
        y = self.ycor()
        self.goto(x+10 * self.xspeed ,y+10 * self.yspeed)
        

    def bounce_wall(self):
        self.yspeed = self.yspeed * -1
    
    def bounce_paddle(self):
        self.xspeed = self.xspeed * -1

    def speed_ball(self):
        if self.ball_speed > 0.05:
            self.ball_speed -= 0.05
        
    def reset_speed(self):
        self.ball_speed = 0.2
        
