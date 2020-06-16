from problem_3_lib import Position

workers = [{'name': 'John', 'surname': 'Doe', 'position': 'A',
            'wage': 1200, 'bonus': 300},
           {'name': 'Jane', 'surname': 'Doe', 'position': 'B',
            'wage': 800, 'bonus': 200},
           {'name': 'John', 'surname': 'Smith', 'position': 'C',
            'wage': 400, 'bonus': 100}]

workers = [Position(**_) for _ in workers]

print('- payroll -')
for _ in workers:
    print(_.get_full_name(), _.position, _.get_income())
print(f'total: {workers[0].total_income}')
