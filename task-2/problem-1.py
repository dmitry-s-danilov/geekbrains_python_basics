"""
GeekBrains. Курс основы языка Python. Урок 2. Задача 1.
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

# --- setting ---

# samples of string and integer
s = 'сорок два'
n = 42

# a list of data samples
data_list = [
    s,  # string
    s.encode(),  # bytes
    bytearray(s.encode()),  # bytearray
    n,  # integer number
    # bin(n),  # in binary format
    # oct(n),  # in octal format
    # hex(n),  # in hexadecimal format
    float(n),  # real number
    complex(n, n),  # complex number
    list(s),  # list
    tuple(s),  # tuple
    set(s),  # set
    frozenset(s),  # frozenset
    {s: n},  # dict
    bool(n),  # bool
    None  # NoneType
]

# --- output ---

# set a table format
table_header = ('', 'элемент', 'тип')
row_number = len(data_list)
column_number = len(table_header)
column_width_list = list()
for column_header in table_header:
    column_width_list.append(len(column_header))

# make a table whose row contains
# sample index, data sample and sample type
data_table = [table_header]
for row_index, data_sample in enumerate(data_list, 1):
    # check a type of the data sample
    sample_type = type(data_sample)
    # append a row to the data table
    data_table.append((repr(row_index),
                       repr(data_sample),
                       repr(sample_type)))
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
              .ljust(column_width_list[column_index]),
              end=' ')
    print()
