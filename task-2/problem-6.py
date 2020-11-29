"""
GeekBrains. Курс основы языка Python. Урок 2. Задача 6.
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
 (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
 (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{“название”: [“компьютер”, “принтер”, “сканер”],
 “цена”: [20000, 6000, 2000],
 “количество”: [5, 2, 7],
 “ед”: [“шт.”]}
"""

# --- settings ---

actions = {'н': 'вывести номенклатуру',
           'с': 'вывести статистику',
           'т': 'добавить товар'}

good_keys = ('название', 'цена', 'количество', 'eд')

goods = []
# goods = [(1, {'название': 'компьютер',
#               'цена': 20000,
#               'количество': 5,
#               'eд': 'шт.'}),
#          (2, {'название': 'принтер',
#               'цена': 6000,
#               'количество': 2,
#               'eд': 'шт.'}),
#          (3, {'название': 'сканер',
#               'цена': 2000,
#               'количество': 7,
#               'eд': 'шт.'})]

# --- solution ---

while True:
    for key, value in actions.items():
        print(f'{key}: {value}')

    action_key = input('\nвведите символ: ')

    if action_key == 'н':
        print(f'\nпозиций: {len(goods)}')

        for number, good in goods:
            print(f'\nномер: {number:d}')
            for good_key in good.keys():
                print(f'{good_key}: {good[good_key]}')

        print()
    elif action_key == 'с':
        print(f'\nпозиций: {len(goods)}')

        statistics = dict()
        for good_key in good_keys:
            statistics.update({good_key: list()})

        for number, good in goods:
            for good_key in good.keys():
                if good[good_key] not in statistics[good_key]:
                    statistics[good_key].append(good[good_key])

        for key, value in statistics.items():
            print(f'{key}: {repr(value)[1:-1]}')

        print()
    elif action_key == 'т':
        good = dict()

        good_key = good_keys[0]
        good_value = input(f'\nвведите {good_key}: ')
        if good_value.isalnum():
            good.update({good_key: good_value})
        else:
            print('товар не добавлен', end='\n\n')
            continue

        good_key = good_keys[1]
        good_value = input(f'введите {good_key}: ')
        if good_value.isnumeric():
            good.update({good_key: int(good_value)})
        else:
            print('товар не добавлен', end='\n\n')
            continue

        good_key = good_keys[2]
        good_value = input(f'введите {good_key}: ')
        if good_value.isnumeric():
            good.update({good_key: int(good_value)})
        else:
            print('товар не добавлен', end='\n\n')
            continue

        good_key = good_keys[3]
        good_value = input(f'введите {good_key}: ')
        if good_value.isalpha():
            good.update({good_key: good_value})
        else:
            print('товар не добавлен', end='\n\n')
            continue

        good_number = len(goods) + 1
        goods.append((good_number, good))
        print(f'товар добавлен под номером {good_number:d}', end='\n\n')
    else:
        break
