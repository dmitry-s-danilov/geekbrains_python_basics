class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        try:
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {'wage': float(wage), 'bonus': float(bonus)}
        except ValueError:
            print('ValueError: wrong arguments')


class Position(Worker):
    total_income = 0

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        Position.total_income += sum(self._income.values())

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_income(self):
        return sum(self._income.values())
