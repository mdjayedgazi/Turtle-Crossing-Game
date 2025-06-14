from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2 , stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.forward(random.randint(10,50))
            random_Y = random.randint(-250,250)
            new_car.goto(x=300,y=random_Y)
            new_car.forward(10)
            new_car.speed(5)
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5


