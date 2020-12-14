def my_sum(a, b):
    """returns a sum of two arguments"""
    return a + b


print(f'{my_sum.__name__}: {my_sum.__doc__}')

d = ((1, 2), (1., 2.), (1 + 1j,  2 + 2j), ('1', '2'))
for x, y in d:
    z = my_sum(x, y)
    print(f'{type(z)}: {x} + {y} = {z}')
