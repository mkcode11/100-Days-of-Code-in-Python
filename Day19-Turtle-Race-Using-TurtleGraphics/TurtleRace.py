from turtle import Turtle,Screen
import random

screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=500, height=400)

def choice(ch):
    global screen
    if ch=='y' or ch=="yes":
        play()
    else:
        screen.exitonclick()


def play():

    colors=['red','orange','yellow','green','blue','purple']
    user_bet = screen.textinput(title='Make Your Bet',prompt=f'What Turtle will Win the Race? \n{colors}\nEnter Your Color : ')
    screen.clear()
    all_turtle=[]
    n=-150
    for turtle_index in range(0,6):

        new_turtle=Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-220, y=n)
        n += 50
        all_turtle.append(new_turtle)



    is_race_on = False

    if user_bet in colors:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtle:

            if turtle.xcor()>230:
                is_race_on=False
                winning_color=turtle.pencolor()

                if user_bet==winning_color:
                    ch=screen.textinput(title='You\'ve Win!',prompt=f'You\'ve win! The {winning_color} is the Winner!\n'
                                                                    f'Enter \'y\' to Play again : Or\n'
                                                                    f'Enter \'n\' and click on screen to exit')

                    choice(ch)
                else:
                    ch=screen.textinput(title='You\'ve Lost!', prompt=f'You\'ve Lost! The {winning_color} is the Winner!\n'
                                                                      f'Enter \'y\' to Play again : Or\n'
                                                                      f'Enter \'n\' and click on screen to exit')

                    choice(ch)

            random_distance=random.randint(0,10)
            turtle.forward(random_distance)




play()

