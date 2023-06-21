from turtle import Turtle

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def create(self,x_cor,y_cor,name):
        self.goto(x_cor,y_cor)
        self.write(f"{name}",align="center", font=("Arial",10,"normal"))