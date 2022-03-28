from turtle import Turtle
P1_START_POS = (350, 0)
P2_START_POS = (-350, 0)
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=None, stretch_len=5, outline=None)
        self.penup()
        self.setpos(P1_START_POS)
        self.setheading(UP)

    def up(self):
        if self.ycor() < 240:
            self.forward(50)


    def down(self):
        if self.ycor() > -240:
            self.forward(-50)

class Paddle2(Paddle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=None, stretch_len=5, outline=None)
        self.penup()
        self.setpos(P2_START_POS)
        self.setheading(UP)
    

    def up(self):
        if self.ycor() < 240:
            self.forward(50)


    def down(self):
        if self.ycor() > -240:
            self.forward(-50)
