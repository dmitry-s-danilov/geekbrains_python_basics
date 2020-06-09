def check(x, filter_nonduplicate, filter_duplicate):
    print(f'list: {x}')
    c = []
    for i in range(len(x) + 1):
        print(f'index: {i}')
        y = x[:i]
        print(f'slice: {y}')
        z = {'unique': set(y),
             'nonduplicate': filter_nonduplicate(y),
             'duplicate': filter_duplicate(y)}
        for _ in z.keys():
            print(f'{_}: {z[_]}')
        c.append(z['unique'] == set(z['nonduplicate']) | set(z['duplicate']))
        print(f'check: {c[-1]}')
    c = all(c)
    print(f'all: {c}')
    return c
