name = input('input your name: ')
age = int(input('input your age in whole years: '))
# print('Hello, %s of %d years old!' % (name, age))
print('Hello, {:s} of {:d} years old!'.format(name, age))
