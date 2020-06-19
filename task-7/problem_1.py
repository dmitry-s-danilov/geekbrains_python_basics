from problem_1_lib import Matrix


def my_print(x):
    print(f'size: {x.size}',
          f'matrix:\n{x}',
          f'twice:\n{x + x}',
          sep='\n', end='\n\n')


matrices = [[[31, 22]],
            [[31], [37], [51]],
            [[31, 22], [37, 43], [51, 86]],
            [[3, 5, 32], [2, 4, 6], [-1, 64, -8]],
            [[3, 5, 8, 3], [8, 3, 7, 1]]]
matrices = [Matrix(_) for _ in matrices]

for _ in matrices:
    my_print(_)
