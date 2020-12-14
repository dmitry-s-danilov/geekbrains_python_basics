from itertools import count


def my_count(start, step=1):
    value = start
    while True:
        yield value
        value += step


def print_count(count_arg, stop):
    index, value = 1, next(count_arg)
    while value <= stop:
        print(f'{index}: {value}')
        index += 1
        value = next(count_arg)


my_start, my_stop = 3, 10
print_count(count(my_start), my_stop)

# implementation with my count
# print_count(my_count(my_start), my_stop)
