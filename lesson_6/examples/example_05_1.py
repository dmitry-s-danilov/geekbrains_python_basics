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

    def change_model(self, model):
        self._model = model

    def change_year(self, year):
        self.__year = year


# create class item
auto = Auto()
auto.print_info()
print()

# change class item attributes
auto.name = 'Lada'
auto.change_model(2110)
auto.change_year(2000)
auto.print_info()
