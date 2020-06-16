from random import randint, choice
from problem_4_lib import TownCar, SportCar, WorkCar, speed_check

# set cars and speed limits
cars = [(TownCar('A', 'red', False), 60),
        (TownCar('B', 'blue', True), 60),
        (SportCar('C', 'red', False), 60),
        (WorkCar('D', 'green', False), 40)]

# move
r = 10  # acceleration section
d = 10  # drive section
for _ in range(1, r + d + 1):
    print(f'- {_} -')
    for car, speed_limit in cars:
        car.move((choice((-1, 1)) if _ > r else 1) \
                 * randint(*car.speed_change_range))
        print(car.name, car.speed,
              'over speed' if not speed_check(car, speed_limit) else '')
    print()
