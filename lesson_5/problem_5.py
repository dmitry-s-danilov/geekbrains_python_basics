from functools import reduce, partial
from random import random
from problem_5_lib import *

file_name = 'text_5.txt'

n = 10
x = [random() for _ in range(n)]
x_sum = reduce(lambda a, b: a + b, x)

for _ in enumerate(x, 1):
    print('{}: {}'.format(*_))
print(f'sum: {x_sum}')

p = 3
x = [round(_, p) for _ in x]

write_file = partial(write_file_1, numbers=x)
if open_for_write(file_name, write_file) is not None:
    print(f'saved to file {file_name}')

y = open_for_read(file_name, read_file_1)
if y is not None:
    print(f'read from file {file_name}')
    y_sum = reduce(lambda a, b: a + b, y)
    sum_delta = x_sum - y_sum
    for _ in enumerate(y, 1):
        print('{}: {}'.format(*_))
    print(f'sum: {y_sum:.3f}')
    print(f'delta: {sum_delta:.5f}')
