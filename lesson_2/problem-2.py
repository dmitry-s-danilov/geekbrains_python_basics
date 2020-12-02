"""
GeekBrains. Курс основы языка Python. Урок 2. Задача 2.
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# --- setting ---

# rearrangement sublist length
p = 2

# --- input ---

print(f'Введите список, длинной не менее, чем {p:d}, одной строкой,',
      'предварительно указав разделитель.')
s = input('Введите разделитель: ')
xs = input('Введите список: ')
x = xs.split(s)

# --- solution ---

# find list length
n = len(x)

if 0 < p <= n:
    # --- solution 1: initial ---
    # make a new list of rearranged slices

    # make an empty list
    # y = []
    # find a number of slices for rearrangement
    # k = n // p
    # find an index of changeless rest
    # q = n % p
    # extend the list by reversed slices
    # for i in range(k):
    #   y.extend(x[p * i:p * (i + 1)][::-1])
    # extend the list by unchangeable rest
    # y.extend(x[p * (i + 1): p * (i + 1) + q])

    # --- solution 2: simplified ---
    # rearrange a list itself

    # make a copy of the list
    y = x[:]
    # find a number of slices for rearrangement
    k = n // p
    # change slices by reversed ones
    for i in range(k):
        y[p * i:p * (i + 1)] = y[p * i:p * (i + 1)][::-1]

    # --- output ---

    # set a table format
    table_header = ('индекс', 'элемент', 'обмен')
    row_number = len(x)
    column_number = len(table_header)
    column_width_list = list()
    for column_header in table_header:
        column_width_list.append(len(column_header))

    # generate a table whose row contains
    # index and items of original and exchanged list
    data_table = [table_header]
    for row_index in range(row_number):
        # append a row to the table
        data_table.append((repr(row_index),
                           x[row_index],
                           y[row_index]))
        # update the column width list
        for column_index in range(column_number):
            maximum_column_width = column_width_list[column_index]
            column_width = len(data_table[row_index][column_index])
            if column_width > maximum_column_width:
                column_width_list[column_index] = column_width

    # print the table
    for row_index in range(row_number + 1):
        for column_index in range(column_number):
            table_item = data_table[row_index][column_index]
            print(table_item
                  .rjust(column_width_list[column_index]),
                  end=' ')
        print()
else:
    print('Некорректные данные')
