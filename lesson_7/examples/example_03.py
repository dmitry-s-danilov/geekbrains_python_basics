class MyClass:
    """string overload"""
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
        print('MyClass object created')

    def __str__(self):
        return 'MyClass object with parameters ' + \
               f'({self.param_1}, {self.param_2})'

    def __del__(self):
        print('MyClass object deleted')


my_object = MyClass('one', 'two')
print(my_object)
