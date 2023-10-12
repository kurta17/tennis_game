import turtle as t

class Paddle(t.Turtle):
    def __init__(self, x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(self.x_cor, self.y_cor)
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.speed(0)
        
        
    
    def move_up(self):
        
        if self.ycor() < 250:
            self.goto(self.x_cor, self.ycor() + 40)
            
        
        
    def move_down(self):
        
        if self.ycor() > -250:
            self.goto(self.x_cor, self.ycor() - 40)
            
