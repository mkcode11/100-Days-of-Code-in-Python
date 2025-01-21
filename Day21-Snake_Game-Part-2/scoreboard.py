from turtle import Turtle
ALIGNMENT= 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):

        self.home()
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
