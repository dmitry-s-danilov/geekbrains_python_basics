def check(x, filter_1, filter_2):
    print(f'list: {x}')
    c = []
    for _ in range(len(x) + 1):
        print(f'index: {_}')
        y = x[:_]
        print(f'slice: {y}')
        z = filter_1(y)
        print(f'filter: {z}')
        c.append(z == filter_2(y))
        print(f'check: {c[-1]}')
    c = all(c)
    print(f'all: {c}')
    return c
