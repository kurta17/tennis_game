import turtle as t

class Lines(t.Turtle):
    def __init__(self):
        super().__init__()
        self.line = t.Turtle()
        self.line.color("white")
        
        self.line.speed(0)
        self.line.penup()
        self.line.goto(0,-300)
        self.line.width(5)
        self.line.setheading(90)

    def drow_line(self):
        while self.line.ycor() < 320:
            self.line.pendown()
            self.line.forward(10)
            self.line.penup()
            self.line.forward(10)
        self.line.pendown()
        
