import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        

    def move_ball(self):
        x = self.xcor()
        y = self.ycor()
        
        self.goto(x-5,y+5)
        self.forward(20)
