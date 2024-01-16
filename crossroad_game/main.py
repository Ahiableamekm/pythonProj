import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.6)
    screen.update()
    car_manager.make_car()
    car_manager.move()
    for car in car_manager.car_garage:
        if player.distance(car) < 20:
            game_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

















screen.exitonclick()