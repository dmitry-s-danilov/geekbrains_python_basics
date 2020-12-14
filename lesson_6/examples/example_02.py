class Auto:
    # set class attribute
    auto_count = 0

    # set class methods
    def on_auto_start(self, auto_name, auto_model, auto_year):
        # set class item attributes
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year

        # increment class attribute
        Auto.auto_count += 1

        # get class item attributes
        print(f'{self.auto_name} {self.auto_model} start.')

    def on_auto_stop(self):
        print(f'{self.auto_name} {self.auto_model} stop.')


auto = []
for _ in range(3):
    # create object
    auto.append(Auto())

    # apply class methods
    auto[-1].on_auto_start('Rocket', _, 2020)
    auto[-1].on_auto_stop()

    # get class attribute
    print(f'count: {Auto.auto_count}')

for _ in range(len(auto)):
    # get class item attributes
    print(_ + 1, auto[_].auto_name, auto[_].auto_model, auto[_].auto_year)
