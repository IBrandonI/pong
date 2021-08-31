from turtle import Screen
from tab import Tab
from ball import Ball
import time
from score import Score
# Screen setup:
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("V I S I O N")
screen.tracer(0)


ball = Ball()
RightPaddle = Tab("right")
LeftPaddle = Tab("left")
score = Score()



screen.listen()
screen.onkey(RightPaddle.go_up, "Up")
screen.onkey(RightPaddle.go_down, "Down")
screen.onkey(LeftPaddle.go_up, "w")
screen.onkey(LeftPaddle.go_down, "s")

game_is_on = True
coordinate = -1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with top or bottom
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_fromTD()
    #Detect collision with either paddle
    if ball.xcor() == 330 and ball.distance(RightPaddle) < 50:
        #print(f"Ball distance from right paddle: {ball.distance(RightPaddle)}")
        ball.bounce_on_x()
    if ball.xcor() == -330 and ball.distance(LeftPaddle) < 50:
        #print(f"Ball distance from left paddle: {ball.distance(LeftPaddle)}")
        ball.bounce_on_x()
    #when right paddle misses system:
    if ball.xcor() > 400:
        score.add_point_left()
        print(f"Left player has score {score.l_player_score}")
        ball.reset_ball_pos()

    if ball.xcor() < -400:
        score.add_point_right()
        print(f"Right player has score {score.r_player_score}")
        ball.reset_ball_pos()
screen.exitonclick()
