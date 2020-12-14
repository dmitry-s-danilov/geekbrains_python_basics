class MyClass:
    """constructor overload"""
    def __init__(self, param):
        self.param = param


my_object = MyClass('Hello!')
print(my_object.param)
