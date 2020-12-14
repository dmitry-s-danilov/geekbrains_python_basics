d = '---'
for x in range(2 * 16 + 1):
    print(f'{x:3d}|{x:3o}|{x:3x}')
    if x % 8 == 0:
        print(f'{d:s}|{d:s}|{d:s}')
