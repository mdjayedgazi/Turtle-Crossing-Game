import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_car()

    #Detect collision with cars
    for car in cars.all_cars:
        if car.distance(turtle) <20:
            game_is_on = False
            scoreboard.game_over()

    #Detec successful crossing
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        cars.level_up()
        scoreboard.increase_level()



screen.exitonclick()