def filter_0(x):
    try:
        y = []
        for i in range(1, len(x)):
            if x[i] > x[i - 1]:
                y.append(x[i])
        return y
    except TypeError:
        print("Type Error: '>' not supported between instances.")


def filter_1(x):
    """Finds the greater than the previous one elements of the list."""
    try:
        return [x[_] for _ in range(1, len(x)) if x[_] > x[_ - 1]]
    except TypeError:
        print("Type Error: '>' not supported between instances.")


def filter_2(x):
    try:
        y = list(filter(lambda _: _[0] < _[1], zip(x[:-1], x[1:])))
        if len(y):
            return list(zip(*y))[1]
        else:
            return y
    except TypeError:
        print("Type Error: '>' not supported between instances.")
