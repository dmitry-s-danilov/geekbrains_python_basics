from problem_2 import filter_1, filter_2
from problem_2_check import check

test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
test_list.extend(['a', 0])
check(test_list,
      filter_1,
      (lambda _: list(filter_2(_)) if filter_2(_) is not None else None))
