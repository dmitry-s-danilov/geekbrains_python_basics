name = input('input your name: ')
age = int(input('input your age in whole years: '))
# print('Hello, %s of %d years old!' % (name, age))
# print('Hello, {} of {} years old!'.format(name, age))
# print('Hello, {:s} of {:d} years old!'.format(name, age))
# print(f'Hello, {name} of {age} years old!')
print(f'Hello, {name:s} of {age:d} years old!')