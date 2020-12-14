class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    """overload retrieving an item by index"""
    def __init__(self, *args):
        self.my_list = []
        for _ in args:
            self.my_list.append(Class1(_))

    def __getitem__(self, item):
        return self.my_list[item]


my_object = Class2(False, 1, 'two')
for _ in range(len(my_object.my_list)):
    print(f'{_} {my_object[_]}')
