class Auto:
    auto_count = 0

    def __init__(self, speed=None):
        Auto.auto_count += 1
        self.number = Auto.auto_count
        self.speed = speed if speed is not None else 0

    def info(self):
        print(f'number: {self.number}',
              f'speed: {self.speed}',
              sep='\n')


auto_1 = Auto()
print(type(auto_1))
auto_1.info()

print()

auto_2 = Auto(10)
print(type(auto_2))
auto_2.info()
