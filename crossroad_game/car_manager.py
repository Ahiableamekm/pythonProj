from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.car_garage = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        """
        Creates a car
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1 or random_chance == 3:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(280, random.randint(-250, 250))
            self.car_garage.append(new_car)

    def move(self):
        """
        Move a car across the screen
        """
        for car in self.car_garage:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        