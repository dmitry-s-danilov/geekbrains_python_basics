class Car:
    __speed_max = 150

    def __init__(self):
        self.speed = 0

    def move(self, speed_change=None):
        if speed_change is not None:
            if 0 <= self.speed + speed_change <= Car.__speed_max:
                self.speed += speed_change
            elif Car.__speed_max < self.speed + speed_change:
                self.speed = Car.__speed_max
            else:
                self.speed = 0
        return self.speed


class TownCar(Car):
    speed_change_range = (1, 10)

    def __init__(self, name, color, is_police):
        super().__init__()
        self.name = name
        self.color = color
        self.is_police = bool(is_police)


class SportCar(Car):
    __speed_max = 200
    speed_change_range = (5, 20)

    def __init__(self, name, color, is_police):
        super().__init__()
        self.name = name
        self.color = color
        self.is_police = bool(is_police)


class WorkCar(Car):
    __speed_max = 100
    speed_change_range = (1, 5)

    def __init__(self, name, color, is_police):
        super().__init__()
        self.name = name
        self.color = color
        self.is_police = bool(is_police)


def speed_check(car, speed_limit):
    return car.is_police or car.speed <= speed_limit
