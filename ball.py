import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.xspeed = 1
        self.yspeed = 1
        

    def move_ball(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x+10 * self.xspeed ,y+10 * self.yspeed)
        

    def bounce_wall(self):
        x = self.xcor()
        y = self.ycor()
        self.yspeed = self.yspeed * -1
