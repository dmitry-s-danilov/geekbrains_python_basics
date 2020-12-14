from random import randint
from problem_3_lib import Cell

x, y = [Cell(randint(1, 100)) for _ in range(2)]
print(f'x: {x}',
      f'y: {y}',
      f'x + y: {x + y}',
      f'x - y: {x - y}',
      f'y - x: {y - x}',
      f'x * y: {x * y}',
      f'x / y: {x / y}',
      f'y / x: {y / x}',
      f'x by y:\n{x.make_order(y())}',
      f'y by x:\n{y.make_order(x())}',
      sep='\n')
