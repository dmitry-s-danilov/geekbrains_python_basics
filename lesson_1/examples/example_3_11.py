x = 1, 2, 3
y = 'one', 'two', 'three'
print('three: {2:d}, two: {1:d}, one: {0:d}'.format(*x))
print('three: {2:s}, two: {1:s}, one: {0:s}'.format(*y))
