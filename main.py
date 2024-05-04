import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.bgcolor("black")
screen.listen()
screen.onkey(player.move, "Up")
cars = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.generate_cars()
    cars.move_car()
    # detecting collision with cars
    for car in cars.new_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
    # detecting if the turtle reached the top edge
    if player.ycor() > 300:
        player.goto((0, -280))
        cars.level_up()
        score.update_level()
screen.exitonclick()
