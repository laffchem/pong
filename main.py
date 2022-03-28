from turtle import Screen
from paddles import P1_START_POS, P2_START_POS, Paddle, Paddle2
from ball import BALL_ORI, Ball
from score import Score1, Score2

import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle2()
ball = Ball()
score1 = Score1()
score2 = Score2()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_on = True
while game_on:
    ball.movement()
    screen.update()
    score1.score1()
    score2.score2()
    time.sleep(ball.move_speed)

    #Detect P1 Miss
    if ball.xcor() > 380:
        time.sleep(2)
        ball.reset_position()
        paddle1.setpos(P1_START_POS)
        paddle2.setpos(P2_START_POS)
        score2.change_score_2()

   
    #Detect P2 Miss
    elif ball.xcor() < -380:
        time.sleep(2)
        ball.reset_position()
        paddle1.setpos(P1_START_POS)
        paddle2.setpos(P2_START_POS)
        score1.change_score_1()
        

    #Top & Bottom Wall collision
    elif ball.ycor() <= -280:
        ball.bounce()
    elif ball.ycor() >= 280:
        ball.bounce()

    #Detect Collisions with Paddle
    if ball.distance(paddle1) < 65 and ball.xcor() > 320:
        ball.bounce_paddle()

    if ball.distance(paddle2) < 65 and ball.xcor() <-320:
        ball.bounce_paddle()
        


















screen.exitonclick()