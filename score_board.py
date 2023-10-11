import turtle

class Score_Left(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.scorel = 0 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.print_score()
        
    def print_score(self):
        self.clear()  
        self.write(f"Score: {self.scorel}", align="center", font=("Arial", 24, "normal"))

class Score_Right(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.scorer = 0 
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(200, 260)
        self.print_score()
        
    def print_score(self):
        self.clear()  
        self.write(f"Score: {self.scorer}", align="center", font=("Arial", 24, "normal")) 
    
