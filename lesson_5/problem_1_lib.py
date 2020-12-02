from os import remove

actions = {'create': 'create file\nto exit enter blank string',
           'view': "view file '{}'",
           'saved': "file '{}' saved",
           'closed': "file '{}' closed",
           'removed': "file '{}' removed"}

inputs = {'name': 'input name: ',
          'line': 'input line: '}

errors = {'IOError': "IOError: wrong file name '{}'"}


def create_file(file_name, input_lines):
    try:
        with open(file_name, 'w', encoding='utf-8') as file_object:
            input_lines(file_object)
        print(actions.get('saved').format(file_name))
        return file_name
    except IOError:
        print(errors.get('IOError').format(file_name))


def view_file(file_name, print_lines):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            print_lines(file_object)
        print(actions.get('closed').format(file_name))
        return file_name
    except IOError:
        print(errors.get('IOError').format(file_name))


def remove_file(file_name):
    try:
        remove(file_name)
        print(actions.get('removed').format(file_name))
        return file_name
    except IOError:
        print(errors.get('IOError').format(file_name))


def input_lines_0(file_object):
    while True:
        line = input(inputs.get('line'))
        if line:
            file_object.write(line + '\n')
        else:
            break


def input_lines_1(file_object):
    lines = []
    while True:
        line = input(inputs.get('line'))
        if line:
            lines.append(line + '\n')
        else:
            break
    file_object.writelines(lines)


def input_lines_2(file_object):
    while True:
        line = input(inputs.get('line'))
        if line:
            print(line, file=file_object)
        else:
            break


def print_lines_0(file_object):
    print(file_object.read(), end='')


def print_lines_1(file_object):
    while True:
        line = file_object.readline()
        if line:
            print(line, end='')
        else:
            break


def print_lines_2(file_object):
    for line in file_object.readlines():
        print(line, end='')


def print_lines_3(file_object):
    for line in list(file_object):
        print(line, end='')


def print_lines_4(file_object):
    for line in file_object:
        print(line, end='')
