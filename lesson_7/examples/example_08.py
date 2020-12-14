class MyClass:
    """equal operator overload"""
    def __init__(self, param):
        self.param = param

    def __call__(self, param=None):
        if param is not None:
            self.param = param
        return self.param

    def __eq__(self, other):
        return self.param == other.param

    def __str__(self):
        return str(self.param)


my_object_1, my_object_2 = MyClass(1), MyClass(2)
print(f'{my_object_1} == {my_object_2}' \
          if my_object_1 == my_object_2 \
          else f'{my_object_1} != {my_object_2}')

my_object_2(my_object_1())
print(f'{my_object_1} == {my_object_2}' \
          if my_object_1 == my_object_2 \
          else f'{my_object_1} != {my_object_2}')
