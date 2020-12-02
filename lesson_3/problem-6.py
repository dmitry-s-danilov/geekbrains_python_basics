"""
GeekBrains. Курс основы языка Python. Урок 3. Задача 6.
Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.capitalize()


def my_filter(string_primary):
    symbol_sep = ' '
    code_range = set(range(ord('A'), ord('Z') + 1)) | \
        set(range(ord('a'), ord('z') + 1)) | \
        {ord(symbol_sep)}
    string_filtered = ''
    for symbol in string_primary:
        if ord(symbol) not in code_range:
            symbol = symbol_sep
        string_filtered += symbol
    return string_filtered


def my_capitalize(string_arg):
    """Capitalizes words in string."""
    symbol_sep = ' '
    words = []
    for word in my_filter(string_arg).split():
        words.append(int_func(word))
    return symbol_sep.join(words)


strings = ['text',
           '*tEXT*',
           'abra cad abra',
           '*aBRA_cAD_aBRA*',
           'abracadabra',
           'super cali fragilistic expiali docious',
           '*sUPER_cALI_fRAGILISTIC_eXPIALI_dOCIOUS*',
           'supercalifragilisticexpialidocious']

print(my_capitalize.__doc__)
for number, string in enumerate(strings, 1):
    print(f'{number}: {string}',
          f'-> {my_capitalize(string)}',
          sep='\n')
