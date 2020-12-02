from problem_2 import filter_1, filter_2
from problem_2_check import check

test_list = list('abracadabra')
test_list.extend([0, 'a'])
check(test_list,
      filter_1,
      (lambda _: list(filter_2(_)) if filter_2(_) is not None else None))
