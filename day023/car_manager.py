from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_pool(self, count):
        for _ in range(count):
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randrange(300, 1000, random.randint(60, 150)), random.randrange(-250, 250, 30))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            if new_x < -350:
                new_x = random.randrange(300, 1000, random.randint(60, 150))
            car.goto(new_x, car.ycor())

    def up_difficulty(self):
        self.move_speed += MOVE_INCREMENT

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     pass
