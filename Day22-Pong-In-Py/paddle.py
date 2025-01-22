from turtle import Turtle






class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=5)


    def up(self):
        if self.ycor()>230:
            pass
        else:
            self.forward(20)


    def down(self):
        if self.ycor()<-230:
            pass
        else:
            self.backward(20)


