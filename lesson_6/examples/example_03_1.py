class Auto:
    # set class attribute
    auto_count = 0

    # set constructor
    def __init__(self):
        # increment class attribute
        Auto.auto_count += 1


auto = []
for _ in range(3):
    # create object
    auto.append(Auto())

    # get class attribute
    print(Auto.auto_count, auto[-1], type(auto[-1]))
