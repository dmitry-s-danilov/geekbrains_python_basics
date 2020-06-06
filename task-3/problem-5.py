"""
GeekBrains. Курс основы языка Python. Урок 3. Задача 5.
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ,
выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""


def ext_func():
    com_sum = 0

    def int_func(arg_string):
        """Adds the sum of the entered numbers to the calculated one."""
        nonlocal com_sum
        if len(arg_string):
            arg_list = []
            for _ in arg_string.split():
                if _.isnumeric():
                    arg_list.append(float(_))
                else:
                    break
            com_sum += sum(arg_list)
        return com_sum
    return int_func


exit_symbol = '.'
my_func = ext_func()
print(my_func.__doc__,
      f"Enter the symbol '{exit_symbol}' to exit.",
      sep="\n")
while True:
    string = input('input numbers: ')
    if exit_symbol not in string:
        print(f'total sum: {my_func(string)}')
    else:
        string = string[:string.index(exit_symbol)]
        print(f'total sum: {my_func(string)}')
        break
