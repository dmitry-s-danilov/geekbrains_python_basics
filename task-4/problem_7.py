def fact(n):
    """Returns factorial generator."""
    f = 1  # factorial of the zero
    try:
        for _ in range(1, n + 1):
            f *= _
            yield f
    except TypeError:
        print('TypeError: argument should be integer number')


def print_fact(n):
    for _ in enumerate(fact(n), 1):
        print('{}! = {}'.format(*_))

# implementation with next
# def print_fact(n):
#     f = fact(n)
#     k = 1
#     while k <= n:
#         print(f'{k}! = {next(f)}')
#         k += 1


print(fact.__doc__)
while True:
    try:
        print_fact(int(input('input integer number: ')))
        break
    except ValueError:
        print('ValueError: argument should be integer number')
        continue
