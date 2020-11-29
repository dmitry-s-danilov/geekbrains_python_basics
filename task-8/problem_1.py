from problem_1_lib import Date

dates = ['23-10-1953', '20-03-1983', '25-12-2015',  # right
         # check extraction
         'dd-06-2020', '22-mm-2020', '22-06-yyyy',  # wrong
         '22-06-2020-', '22-06-', '22-06', '22-', '22', ''  # wrong
         # check validation
         '22-06-2020',  # right
         '31-06-2020', '22-13-2020', '22-06-0000',  # wrong
         '29-02-2020',  # right
         '29-02-2021', '29-02-2022', '29-02-2023']  # wrong

print(f'init {Date.__name__} objects:')
dates = {_: Date(_) for _ in dates}

print(f'\nprint {Date.__name__} objects:')
for _ in dates.items():
    print(f'{_[0]}: {_[1]}')
