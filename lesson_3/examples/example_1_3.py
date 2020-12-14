def my_sum(a, b):
    return a, b, a + b


for x, y in ((1, 2), (1., 2.), (1 + 1j, 2 + 2j), ('1', '2')):
    print('{0}: {1} + {2} = {3}'.format(type(x), *my_sum(x, y)))
