from functools import reduce

errors = {'IOError': "IOError: wrong file name '{}'"}


def open_file(file_name, read_file):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            return read_file(file_object)
    except IOError:
        print(errors.get('IOError').format(file_name))


def read_salaries(file_object):
    salaries = [_.split() for _ in file_object.readlines()]
    salaries = {_[0]: float(_[1]) for _ in salaries}
    return salaries


def print_salaries(salaries):
    for _ in salaries.items():
        print('{}: {}'.format(*_))


def salary_average(salaries):
    return reduce(lambda x, y: x + y, salaries.values()) / len(salaries)


def person_filter(salaries, salary_condition):
    return [person
            for person, salary in salaries.items()
            if salary_condition(salary)]
