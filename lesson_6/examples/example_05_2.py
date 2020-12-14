class Auto:
    # constructor
    def __init__(self):
        # set class item attributes
        # public
        self.name = 'Mazda'
        # protected
        self._model = 'CX5'
        # private
        self.__year = 2020

    # class methods
    def print_info(self):
        print(f'name: {self.name}',
              f'model: {self._model}',
              f'model: {self.__year}',
              sep='\n')


# create class item
auto = Auto()
auto.print_info()
print()

# change class item attributes
auto.name = 'Lada'
auto._model = 2110
auto._Auto__year = 2000
auto.print_info()
