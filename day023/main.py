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
car = CarManager()

screen.onkey(player.go_up, key="Up")

game_is_on = True
gen = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() == 280:
        player.next_level()

    if gen == 6:
        car.new_car()
        gen = 0

    car.move()
    gen += 1

screen.exitonclick()