"""
GeekBrains. Курс основы языка Python. Урок 2. Задача 4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

# --- settings ---

word_separator = ' '
word_width = 10

# --- test strings ---

# word_string = ''
# word_string = ' '
# word_string = 'one'
# word_string = ' one'
# word_string = 'one '
# word_string = ' one '
# word_string = 'one two three four five six seven eight nine ten ' +\
#               'supercalifragilisticexpialidocious'

# --- input ---

print("Введите строку из нескольких слов,",
      f"длинной не более {word_width:d},",
      f"разделенных символом '{word_separator:s}'.")
word_string = input('Введите строку:')

# --- solution ---

if len(word_string) > 0:
    print('Список слов:')
    for index, word in enumerate(word_string.split(word_separator), 1):
        print(index, word if len(word) <= word_width else word[:word_width])
else:
    print('Введена строка нулевой длины.')
