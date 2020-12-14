class MyClass:
    """addition operator overload"""
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
        # print('MyClass object created')

    def __str__(self):
        return 'MyClass object with parameters ' + \
               f'({self.param_1}, {self.param_2})'

    def __add__(self, other):
        return MyClass(self.param_1 + other.param_1,
                       self.param_2 + other.param_2)

    # def __del__(self):
    #     print('MyClass object deleted')


my_object_1 = MyClass(1, 2)
my_object_2 = MyClass(3, 4)

print(my_object_1)
print(my_object_2)
print(my_object_1 + my_object_2)
