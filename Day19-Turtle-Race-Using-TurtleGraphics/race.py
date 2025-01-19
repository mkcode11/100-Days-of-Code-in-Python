from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title='Make Your Bet',prompt='What Turtle will Win the Race? Enter Your Bet : ')
colors=['red','orange','yellow','green','blue','purple']
all_turtle=[]
n=-150
for turtle_index in range(0,6):

    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=n)
    n += 50
    all_turtle.append(new_turtle)

is_race_on=False

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()

            if user_bet==winning_color:
                screen.textinput(title='You\'ve Win!',prompt=f'You\'ve win! The {winning_color} is the Winner!')
            else:
                screen.textinput(title='You\'ve Lost!', prompt=f'You\'ve Lost! The {winning_color} is the Winner!')

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


