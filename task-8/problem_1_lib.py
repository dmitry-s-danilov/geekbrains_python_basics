class MyException(Exception):
    def __init__(self, message):
        self.message = message


class Date:
    __input_separator = '-'
    __input_keys = 'day', 'month', 'year'
    __messages = {'ValueError': 'ValueError',
                  'LengthError': 'LengthError'}

    @staticmethod
    def check_year_leap(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    @staticmethod
    def check_year(year):
        return year >= 1

    @staticmethod
    def check_month(month):
        return 1 <= month <= 12

    @staticmethod
    def check_day(day, month, year):
        days = {1: 31,
                2: {True: 29, False: 28},
                3: 31, 4: 30, 5: 31,
                6: 30, 7: 31, 8: 31,
                9: 30, 10: 31, 11: 30,
                12: 31}
        if month != 2:
            return day in range(1, days.get(month) + 1)
        else:
            return day in range(1, days.get(2)
                                .get(Date.check_year_leap(year)) + 1)

    @staticmethod
    def validate(year, month, day):
        if Date.check_year(year) and Date.check_month(month):
            return Date.check_day(day, month, year)
        else:
            return False

    @classmethod
    def extract(cls, input_string):
        try:
            input_values = [int(_) for _ in
                            input_string.split(cls.__input_separator)]
            if len(input_values) >= len(cls.__input_keys):
                input_values = input_values[:len(cls.__input_keys)]
            else:
                raise MyException(cls.__messages.get('LengthError'))
        except ValueError:
            print(cls.__messages.get('ValueError'))
        except MyException as exception:
            print(exception)
        else:
            return input_values

    def __init__(self, input_string):
        input_values = self.extract(input_string)
        if input_values is not None:
            self.date = {self.__input_keys[_]: input_values[_]
                         for _ in range(len(self.__input_keys))}
            if not self.validate(**self.date):
                self.date = None
        else:
            self.date = None

    def __str__(self):
        return repr(self.date)
