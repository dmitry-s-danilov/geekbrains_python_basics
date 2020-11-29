"""
GeekBrains. Курс основы языка Python. Урок 3. Задача 2.
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def my_func(name, surname,
            year=None, city=None, email=None, phone=None):
    """Displays user data."""
    print(f'name: {name}, surname: {surname},',
          f'year: {year}, city: {city}, email: {email}, phone: {phone}')


users = [{'name': 'John', 'surname': 'Smith',
          'year': 1977, 'city': 'Sheffield',
          'email': 'johnsmith@gmail.com'},
         {'name': 'Jane', 'surname': 'Smith',
          'year': 1991, 'city': 'Bristol',
          'phone': 3141592653},
         {'name': 'John', 'surname': 'Doe',
          'email': 'johdoe@gmail.com'},
         {'name': 'Jane', 'surname': 'Doe',
          'phone': 2718281828},
         {'name': 'Baby', 'surname': 'Doe'}]

print(my_func.__doc__)
for _, user in enumerate(users, 1):
    print(f'{_} >', end=' ')
    my_func(**user)
