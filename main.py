from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))
ball = Ball()
l_score = Scoreboard((-20,260))
r_score = Scoreboard((20,260))

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #detecting collisions with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detecting collisions with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()
    #resetting state of ball
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.reset()
screen.exitonclick()