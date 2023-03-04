from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.turtlesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(random.randint(300, 350), random.randrange(-250, 250, 30))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def up_difficulty(self):
        self.move_speed += MOVE_INCREMENT
