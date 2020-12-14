x = 'one', 'two', 'three'
y = 1, 2, 3
z = 1.11, 2.22, 3.33

print('right alignment:')
for i in range(len(x)):
    # print('%2d|%6s|%2d|%4.1f|' % (i, x[i], y[i], z[i]))
    # print('{:2d}|{:>6s}|{:2d}|{:4.1f}|'.format(i, x[i], y[i], z[i]))
    print(f'{i:2d}|{x[i]:>6s}|{y[i]:2d}|{z[i]:4.1f}|')

print('left alignment:')
for i in range(len(x)):
    # print('%-2d|%-6s|%-2d|%-4.1f|' % (i, x[i], y[i], z[i]))
    # print('{:<2d}|{:6s}|{:<2d}|{:<4.1f}|'.format(i, x[i], y[i], z[i]))
    print(f'{i:<2d}|{x[i]:6s}|{y[i]:<2d}|{z[i]:<4.1f}|')
