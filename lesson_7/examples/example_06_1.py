class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for _ in args:
            self.my_list.append(Class1(_))


my_object = Class2(False, 1, 'two')
for _ in enumerate(my_object.my_list):
    print(f'{_[0]} {_[1]}')
