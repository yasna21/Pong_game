from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import ScoreBord

# Create a screen object from Screen class
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("brown")
screen.tracer(0)


# Create paddle objects from Paddle class
r_paddle = Paddle((-360, 0))
l_paddle = Paddle((350, 0))
ball = Ball()
scorebord = ScoreBord()


# Create screen events from screen class
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


# Create awhile loop for game
is_game_on = True
while is_game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scorebord.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scorebord.r_point()




screen.exitonclick()
