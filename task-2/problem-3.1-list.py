"""
GeekBrains. Курс основы языка Python. Урок 2. Задача 3.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# --- setting ---

month_min, month_max = 1, 12
season_list = [['зима', 12, 1, 2],
               ['весна', 3, 4, 5],
               ['лето', 6, 7, 8],
               ['осень', 9, 10, 11]]

# --- input ---

print('Введите месяц в виде целого числа от',
      f'{month_min:d} до {month_max:d}.')
month = int(input('Введите месяц: '))

# --- solution ---

if month_min <= month <= month_max:
    for season in season_list:
        if month in season:
            print(f'Время года: {season[0]}')
else:
    print('Неверно введен месяц.')
