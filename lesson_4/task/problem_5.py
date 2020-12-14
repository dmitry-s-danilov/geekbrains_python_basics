from functools import reduce

my_range = 100, 1000 + 1, 1
my_divider = 2
my_condition = lambda _: _ % my_divider == 0
my_operation = lambda *_: _[0] + _[1]

my_object = (_ for _ in range(*my_range) if my_condition(_))
my_result = reduce(my_operation, my_object)
print(f'sum: {my_result}')

# implementation with validation
# my_object = [_ for _ in range(*my_range) if my_condition(_)]
# my_result = reduce(my_operation, my_object)
# my_check = my_result == (my_object[0] + my_object[-1]) / 2 * len(my_object)
# print(f'sum: {my_result}\ncheck: {my_check}')
