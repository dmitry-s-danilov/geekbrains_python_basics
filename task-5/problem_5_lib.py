def open_for_read(file_name, read_file):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            return read_file(file_object)
    except IOError:
        print(f"IOError: wrong file name '{file_name}'")


def open_for_write(file_name, write_file):
    try:
        with open(file_name, 'w', encoding='utf-8') as file_object:
            return write_file(file_object)
    except IOError:
        print(f"IOError: wrong file name '{file_name}'")


def read_file_1(file_object):
    numbers = []
    while True:
        number = file_object.readline()
        if number:
            numbers.append(float(number.strip()))
        else:
            break
    return numbers


def write_file_1(file_object, numbers):
    for number in numbers:
        file_object.write(str(number) + '\n')
    return len(numbers)
