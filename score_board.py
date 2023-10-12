import turtle
import time

class Score(turtle.Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.x_position = x_position  # Set x_position here
        self.goto(x_position, 260)
        self.print_score()

    def print_score(self):
        self.goto(self.x_position, 260)
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self, update):
        
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 40, "normal"))
        time.sleep(1)
        self.print_score()
        update()
        self.clear()

class Score_Left(Score):
    def __init__(self):
        super().__init__(x_position=-200)

class Score_Right(Score):
    def __init__(self):
        super().__init__(x_position=200)

