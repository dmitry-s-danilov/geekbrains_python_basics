def filter_0_nonduplicate(x):
    y = []
    for i in range(len(x)):
        u = True
        for j in range(i):
            if x[i] == x[j]:
                u = False
                break
        if u:
            for j in range(i + 1, len(x)):
                if x[i] == x[j]:
                    u = False
                    break
            if u:
                y.append(x[i])
    return y


def filter_0_duplicate(x):
    y = []
    for i in range(len(x)):
        u = True
        for j in range(i):
            if x[i] == x[j]:
                u = False
                break
        if u:
            for j in range(i + 1, len(x)):
                if x[i] == x[j]:
                    u = False
                    break
            if not u:
                y.append(x[i])
    return y


def filter_1_nonduplicate(x):
    y = []
    for i in range(len(x)):
        u = True
        for j in range(len(x)):
            if x[i] == x[j] and not i == j:
                u = False
                break
        if u:
            y.append(x[i])
    return y


def filter_1_duplicate(x):
    y = []
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j]:
                if j < i:
                    break
                elif j == i:
                    continue
                else:
                    y.append(x[i])
                    break
    return y


def filter_2_nonduplicate(x):
    y = []
    for i in range(len(x)):
        if x[i] not in x[:i] and x[i] not in x[i + 1:]:
            y.append(x[i])
    return y


def filter_2_duplicate(x):
    y = []
    for i in range(len(x)):
        if x[i] not in x[:i] and x[i] in x[i + 1:]:
            y.append(x[i])
    return y


def filter_3_nonduplicate(x):
    return [x[_]
            for _ in range(len(x))
            if x[_] not in x[:_] and x[_] not in x[_ + 1:]]


def filter_3_duplicate(x):
    return [x[_]
            for _ in range(len(x))
            if x[_] not in x[:_] and x[_] in x[_ + 1:]]


def filter_4_nonduplicate(x):
    """Defines non-duplicate list items."""
    return [_ for _ in x if x.count(_) == 1]


def filter_4_duplicate(x):
    """Defines duplicate list items."""
    return [x[_]
            for _ in range(len(x))
            if x.count(x[_]) > 1 and x.index(x[_]) == _]
