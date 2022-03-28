from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ubuntu", 24, "normal")

class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score1 = 0  
        self.score1()
    
    
    def score1(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(150, 200)
        self.write(f"P1: {self.player_score1}", move=True, align=ALIGNMENT, font=FONT)
    
    
    def change_score_1(self):
        self.player_score1 += 1

    def game_over1_wins(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 0)
        self.write(f"Game Over! Player 1 Wins!", move= True, align= ALIGNMENT, font=FONT)    



class Score2(Score1):
    def __init__(self):
        super().__init__()
        self.player_score2 = 0
        self.score2()


    def score2(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(-150, 200)
        self.write(f"P2: {self.player_score2}", move=True, align=ALIGNMENT, font=FONT)    


    def change_score_2(self):
        self.player_score2 += 1


    def game_over2_wins(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 0)
        self.write(f"Game Over! Player 2 Wins!", move= True, align= ALIGNMENT, font=FONT)    
