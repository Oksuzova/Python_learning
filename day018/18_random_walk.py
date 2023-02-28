import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed(10)
degrees = [0, 90, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk():
    turn = random.choice(degrees)
    timmy.right(turn)
    timmy.forward(20)


for _ in range(1000):
    timmy.pensize(10)
    timmy.color(random_color())
    random_walk()

screen = Screen()
screen.exitonclick()