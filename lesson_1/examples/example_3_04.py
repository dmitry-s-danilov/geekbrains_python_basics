x = 'one', 'two', 'three'
y = 1, 2, 3
z = 1.11, 2.22, 3.33

print('right alignment:')
for i in range(len(x)):
    print('%2d|%6s|%2d|%4.1f|' % (i, x[i], y[i], z[i]))

print('left alignment:')
for i in range(len(x)):
    print('%-2d|%-6s|%-2d|%-4.1f|' % (i, x[i], y[i], z[i]))
