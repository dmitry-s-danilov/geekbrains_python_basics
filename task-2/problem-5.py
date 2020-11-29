"""
GeekBrains. Курс основы языка Python. Урок 2. Задача 5.
Реализовать структуру «Рейтинг»,
представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

# --- settings ---

# output strings
call_string = 'Для продолжения введите натуральное число: '
report_string = 'Пользователь ввел число: {}.'
rating_start = 'Результат: '
rating_end = '.'
rating_empty = 'пустой'

# initial rating list
rating_list = []
# rating_list = [7]
# rating_list = [7, 5]
# rating_list = [7, 5, 3]
# rating_list = [7, 5, 3, 3, 2]

# --- solution ---

# print rating list
print(rating_start,
      repr(rating_list)[1:-1] if len(rating_list) else rating_empty,
      sep='', end=(rating_end + '\n'))

# run rating update
while True:
    # input a rating item
    input_item = input(call_string)
    # check an input string to be a numeric
    if input_item.isnumeric():
        # receive an integer number from string
        rating_item = int(input_item)
        # check an integer number to be positive
        if rating_item > 0:
            # print report
            print(report_string.format(rating_item), end=' ')

            # update rating list
            item_index = 0
            while item_index < len(rating_list):
                if rating_item > rating_list[item_index]:
                    break
                item_index += 1
            rating_list.insert(item_index, rating_item)

            # print rating list
            print(rating_start, repr(rating_list)[1:-1],
                  sep='', end=(rating_end + '\n'))
        else:
            break
    else:
        break
