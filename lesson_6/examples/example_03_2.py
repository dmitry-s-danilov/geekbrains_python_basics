class Auto:
    # set class attribute
    auto_count = 0

    # set constructor
    def __init__(self, auto_name, auto_model, auto_year):
        # set class item attributes
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year

        # increment class attribute
        Auto.auto_count += 1

    # set class methods
    def print_info(self):
        # get class item attributes
        print(f'name: {self.auto_name}',
              f'model: {self.auto_model}',
              f'year: {self.auto_year}',
              sep='\n')


def print_auto_count():
    # get class attribute
    print(f'count: {Auto.auto_count}')


# create object
auto = Auto('Lexus', 'RX 350T', 2020)

# get class attribute
print_auto_count()

# apply class method
auto.print_info()
