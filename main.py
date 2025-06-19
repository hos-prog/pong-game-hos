from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game with hos")
screen.tracer(0)


paddle_a = Paddle(350,0)
paddle_b = Paddle(-350,0)
ball=Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_a.go_up,"o")
screen.onkey(paddle_a.go_down,"k")
screen.onkey(paddle_b.go_up,"w")
screen.onkey(paddle_b.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detcting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with a_paddle
    if ball.distance(paddle_a) < 50 and ball.xcor() < 340 or ball.distance(paddle_b) < 50 and ball.xcor() < -340 :
        ball.bounce_x()

    #detect the paddle_a misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.a_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.b_point()

screen.exitonclick()
