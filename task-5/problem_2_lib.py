errors = {'IOError': "IOError: wrong file name '{}'"}


def open_file(file_name, explore_file):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            explore_file(file_object)
        return file_name
    except IOError:
        print(errors.get('IOError').format(file_name))


def print_file_0(file_object):
    for line in file_object:
        print(line, end='')


def print_file_1(file_object):
    lines = file_object.readlines()
    field_length = len(str(len(lines)))
    for index, line in enumerate(lines, 1):
        print('{}: {}'.format(str(index).zfill(field_length), line), end='')


def print_file_2(file_object, word_filter):
    lines = file_object.readlines()
    words = [[filter_isalnum(word)
              for word in _.split()
              if len(word_filter(word))]
             for _ in lines]
    words_numbers = [len(_) for _ in words]
    field_lengths = [len(str(_)) for _ in [len(lines), max(*words_numbers)]]
    for index, line in enumerate(lines, 1):
        print('{} - {}: {}'
              .format(str(index).zfill(field_lengths[0]),
                      str(words_numbers[index - 1]).zfill(field_lengths[1]),
                      line),
              end='')


def filter_isalnum(string_arg):
    return ''.join([_ for _ in list(string_arg) if _.isalnum()])
