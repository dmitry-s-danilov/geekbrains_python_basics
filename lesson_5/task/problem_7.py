from problem_7_lib import *

in_file = 'text_7.txt'
incomes = open_for_read(in_file, read_file_1)
if incomes is not None:
    print(f'файл: {in_file}\n')


    # print(f'\nсреднее: {salary_average(salaries)}\n')