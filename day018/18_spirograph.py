import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(30)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(155, 255)
    return r, g, b


def circle():
    timmy.circle(100)
    timmy.left(5)


for _ in range(int(360 / 5)):
    timmy.color(random_color())
    circle()

screen = Screen()
screen.exitonclick()
