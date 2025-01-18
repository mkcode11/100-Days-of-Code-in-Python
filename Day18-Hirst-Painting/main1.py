# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# timmy=Turtle()
# screen=Screen()
#
# direction = [ 0, 90, 180 , 270]
# timmy.shape('turtle')
# timmy.color('red','green')
#
#
# # def random_walk(color_e,direction):
# #     timmy.color(color_e)
# #     timmy.speed(100)
# #     timmy.setheading(direction)
# #     timmy.speed(50)
# #     timmy.forward(30)
#
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return r,g,b
# timmy.speed(100)
#
#
# def draw(size_of_gap):
#
#     for _ in range(int(360/size_of_gap)):
#
#          timmy.color(random_color())
#          timmy.circle(100)
#          timmy.setheading(timmy.heading()+size_of_gap)
#
# draw(10)
#
#
# screen.exitonclick()