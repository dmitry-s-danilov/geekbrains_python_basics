errors = {'IOError': "IOError: wrong file name '{}'"}

eng_to_rus = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре'}


def open_for_read(file_name, read_file):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            return read_file(file_object)
    except IOError:
        print(errors.get('IOError').format(file_name))


def open_for_write(file_name, write_file):
    try:
        with open(file_name, 'w', encoding='utf-8') as file_object:
            return write_file(file_object)
    except IOError:
        print(errors.get('IOError').format(file_name))


def read_file_1(file_object):
    return file_object.readlines()


def write_file_1(file_object, lines):
    return file_object.writelines(lines)


def translate_1(word, dictionary):
    if word in dictionary.keys():
        return dictionary.get(word)
    else:
        return word
