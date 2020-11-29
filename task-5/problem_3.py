from problem_3_lib import open_file, read_salaries,\
    print_salaries, salary_average, person_filter

file_name = 'text_3.txt'
salaries = open_file(file_name, read_salaries)
if salaries is not None:
    print(f'файл: {file_name}\n')

    print_salaries(salaries)

    print(f'\nсреднее: {salary_average(salaries)}\n')

    salary_threshold = 20000
    print(f'не менее {salary_threshold}:')
    for _ in person_filter(salaries, lambda _: _ >= salary_threshold):
        print(_)
