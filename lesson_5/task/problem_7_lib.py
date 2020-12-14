from functools import reduce


def open_for_read(file_name, read_file):
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            return read_file(file_object)
    except IOError:
        print(f"IOError: wrong file name '{file_name}'")


def read_file_1(file_object):
    incomes = [_.split() for _ in file_object.readlines()]
    incomes = {_[0]: [float(_[2]), float(_[3])] for _ in incomes}
    return incomes


# def salary_average(incomes):
#     return reduce(lambda x, y: x + y, incomes.values()) / len(incomes)

#
#
# def person_filter(salaries, salary_condition):
#     return [person
#             for person, salary in salaries.items()
#             if salary_condition(salary)]
