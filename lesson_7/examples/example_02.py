class MyClass:
    """destructor overload"""
    def __init__(self, param):
        self.param = param
        print('object created')

    def __del__(self):
        print('object deleted')


my_object = MyClass('Hello!')
print(my_object.param)
