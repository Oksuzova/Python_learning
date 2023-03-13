from turtle import Turtle, Screen
import random

tim = Turtle()

tim.penup()
tim.goto(-100, 300)
tim.pendown()

color = ["silver", "royal blue", "sea green", "tan", "hot pink", "indigo", "slate blue"]


def draw(angle):
    for _ in range(angle):
        tim.forward(100)
        tim.right(360 / angle)


for side in range(3, 11):
    tim.color(random.choice(color))
    draw(side)

screen = Screen()
screen.exitonclick()
