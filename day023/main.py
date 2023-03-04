import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.go_up, key="Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    gen_cars = random.randint(1, 6)
    if gen_cars == 1:
        car_manager.new_car()

    if player.ycor() == 280:
        player.next_level()
        car_manager.up_difficulty()
        score.next_level()

    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
