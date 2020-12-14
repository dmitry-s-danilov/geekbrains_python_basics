from random import randint


class Auto:
    # class attribute
    amount = 0

    # class constructor
    def __init__(self, speed):
        self.speed = speed
        Auto.amount += 1
        # self.amount += 1
        print(f'created an auto # {Auto.amount} with speed {self.speed}')
        # print(f'created an auto # {self.amount} with speed {self.speed}')

    # class methods
    def change_speed(self, speed_change):
        speed_change_corrected = speed_change\
            if self.speed + speed_change > 0\
            else -self.speed
        self.speed += speed_change_corrected
        return speed_change_corrected


speed_initial = 10
speed_change_range = -speed_initial, speed_initial
auto = Auto(speed_initial)

for _ in range(10):
    print('{} > {}'
          .format(auto.change_speed(randint(*speed_change_range)),
                  auto.speed))
