# import colorgram
#
# rgb_colors=[]
# colors=colorgram.extract('spots.jpg',10)
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

timmy = Turtle()
screen = Screen()
colors = [(20, 28, 16), (236, 21, 144), (212, 13, 9), (199, 12, 36), (130, 228, 6), (196, 70, 20), (32, 90, 188), (235, 148, 38)]
timmy.hideturtle()
timmy.shape('turtle')
timmy.penup()
timmy.speed('fastest')

timmy.teleport(-300,-200)


def draw_dots(color):
        timmy.color(color)
        timmy.dot(20)
        timmy.forward(50)
n=-200
for _ in range(10):

    for _ in range(10):
        draw_dots(random.choice(colors))
    n+=50
    timmy.teleport(-300,n)


screen.exitonclick()
