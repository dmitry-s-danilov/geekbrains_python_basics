from random import randint
from problem_2 import filter_1, filter_2
from problem_2_check import check

check([randint(1, 10) for _ in range(10)],
      filter_1,
      (lambda _: list(filter_2(_)) if filter_2(_) is not None else None))
