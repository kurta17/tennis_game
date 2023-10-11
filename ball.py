import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.color("white")

    def move_ball(self):
        self.forward(20)
