class MyClass:
    """call overload"""
    def __init__(self, param):
        self.param = param

    def __call__(self, param):
        self.param = param

    def __str__(self):
        return self.param


my_object = MyClass('one')
print(my_object)
my_object('two')
print(my_object)
