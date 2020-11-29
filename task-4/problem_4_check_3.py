from random import randint
from problem_4 import filter_4_nonduplicate, filter_4_duplicate
from problem_4_check import check

check([randint(1, 10) for _ in range(10)],
      filter_4_nonduplicate, filter_4_duplicate)
