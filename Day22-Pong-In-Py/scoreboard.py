from turtle import Turtle
ALIGNMENT= 'center'
FONT = ('Courier', 60, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.color('white')
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(f'{self.l_score}', align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(f'{self.r_score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.home()
        if self.l_score>self.r_score:
            self.write(f'Game Over\nLeft Win', align=ALIGNMENT, font=FONT)
        else:
            self.write(f'Game Over\nRight Win', align=ALIGNMENT, font=FONT)


    def l_point(self):
        self.l_score+=1
        self.update_score()
    def r_point(self):
        self.r_score+=1
        self.update_score()
