"""
GeekBrains. Курс основы языка Python. Урок 3. Задача 3.
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    """Calculate the sum of the largest two arguments."""
    n = 3
    c = (len(args) == n)
    if c:
        for i in range(n):
            c = c and (type(args[i]) == int or type(args[i]) == float)
        if c:
            largs = list(args)
            largs.remove(min(largs))
            return sum(largs)


tests = {0: [(0, 0, 0), (-2, -1, 1)],
         1: [(0, 0, 1), (-2, -1, 2)],
         2: [(0, 0, 2), (-2, -1, 3)]}

print(my_func.__doc__)
checks = []
for key in tests.keys():
    for test in tests[key]:
        checks.append(my_func(*test) == key)
        print('{}: {}, {}, {} -> {} {}'.
              format(key, *test, my_func(*test), checks[-1]))
print(f'all: {all(checks)}')
