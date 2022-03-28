from turtle import Turtle
import random

BALL_ORI = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(BALL_ORI)
        self.x_move = 8
        self.y_move = 8
        self.move_speed = 0.04
        
    
    def movement(self):
        move_x = self.xcor() + self.x_move
        move_y = self.ycor() + self.y_move
        self.goto(move_x, move_y)
        

    
    def bounce(self):
        self.y_move *= -1
        

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setpos(BALL_ORI)
        self.move_speed = 0.04
        self.bounce_paddle()    
        
    
    
