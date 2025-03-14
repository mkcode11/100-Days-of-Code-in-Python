import time
from turtle import Screen



from food import Food
from snake import Snake
from scoreboard import Scoreboard



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()







screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with walls
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        scoreboard.game_over()
        is_game_on=False

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            is_game_on = False




screen.exitonclick()