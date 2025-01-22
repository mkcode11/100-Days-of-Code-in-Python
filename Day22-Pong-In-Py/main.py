import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
ball=Ball()


screen.bgcolor('black')
screen.setup(height=600,width=800)
screen.title('PONG IN PY')
screen.tracer(0)

r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.up,'Prior')
screen.onkeypress(r_paddle.up,'Prior')
screen.onkeypress(r_paddle.down,'End')
screen.onkeypress(l_paddle.up,'w')
screen.onkeypress(l_paddle.down,'z')


def play():
    is_game_on = True
    while is_game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor()>280 or ball.ycor()<-280:
            ball.bounce_y()

        if ball.distance(r_paddle)<60 and ball.xcor()>350 or ball.distance(l_paddle)<60 and ball.xcor()<-350 :
            ball.bounce_x()

        if ball.xcor()>400:
            ball.reset_ball()
            scoreboard.r_point()

        if ball.xcor()<-400:
            ball.reset_ball()
            scoreboard.l_point()

        if scoreboard.l_score==10 or scoreboard.r_score==10:
            scoreboard.game_over()

            is_game_on=False

play()






screen.exitonclick()