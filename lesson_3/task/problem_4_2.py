"""
GeekBrains. Курс основы языка Python. Урок 3. Задача 4.
Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""


def my_func(x, y):
    """Exponentiates."""
    if (type(x) == float or type(x) == int) and type(y) == int and \
            x > 0 and y < 0:
        z = 1
        for _ in range(-y):
            z /= x
        return z


def my_pow(x, y):
    try:
        z = pow(x, y)
    except ZeroDivisionError:
        return None
    return z


tests = [(0, -1), (0, -2), (0, -3), (0, -10),
         (1, -1), (1, -2), (1, -3), (1, -10),
         (2, -1), (2, -2), (2, -3), (2, -10)]

print(my_func.__doc__)
checks = []
for test in tests:
    checks.append(my_func(*test) == my_pow(*test))
    print('{} ^ {} = {} {}'.format(*test, my_func(*test), checks[-1]))
print(f'all: {all(checks)}')
