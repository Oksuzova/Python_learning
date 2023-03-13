import turtle
from turtle import Turtle, Screen
import random

color_list = [(213, 169, 105), (78, 92, 124), (199, 240, 245), (252, 235, 236), (122, 166, 204), (137, 168, 154),
              (122, 97, 85), (187, 134, 149), (252, 237, 57), (89, 70, 77), (216, 64, 78), (88, 118, 101),
              (155, 128, 79), (168, 201, 191), (96, 131, 163), (221, 100, 81), (223, 173, 180)]

y_coord = -220

timmy = Turtle()
timmy.speed(50)
turtle.colormode(255)

timmy.penup()
timmy.goto(-250, y_coord)
timmy.pendown()
timmy.hideturtle()


def points():
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)


for _ in range(10):
    for _ in range(10):
        points()
    y_coord += 50
    timmy.goto(-250, y_coord)

screen = Screen()
screen.exitonclick()

# import colorgram
#
# c = colorgram.extract('image.jpg', 20)
# colors = []
#
# for _ in range(20):
#     rgb = (c[_].rgb.r, c[_].rgb.g, c[_].rgb.b)
#     colors.append(rgb)
#
# print(colors)
