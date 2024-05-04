from turtle import Turtle
import random

COLORS = ["pink", "lightseagreen", "lightyellow", "skyblue", "palevioletred", "plum"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.new_cars = []
        self.a = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, y)
            self.new_cars.append(new_car)

    def move_car(self):
        for car in self.new_cars:
            car.backward(self.a)

    def level_up(self):
        self.a += MOVE_INCREMENT
