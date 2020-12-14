"""
GeekBrains. Курс основы языка Python. Урок 3. Задача 1.
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def my_func(x, y):
    """Calculates quotient of division."""
    try:
        z = x / y
    except ZeroDivisionError:
        return
    return z


def my_input():
    try:
        x = float(input('input divisible: '))
        y = float(input('input divisor: '))
    except ValueError:
        return
    return x, y


print(my_func.__doc__)
my_args = my_input()
if my_args is not None:
    print(f'quotient: {my_func(*my_args)}')
