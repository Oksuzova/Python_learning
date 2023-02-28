import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(50)
turtle.colormode(255)
turn = 5


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(155, 255)
    return r, g, b


def circle():
    timmy.circle(100)
    timmy.left(turn)


for _ in range(int(360 / turn)):
    timmy.color(random_color())
    circle()

screen = Screen()
screen.exitonclick()
