class MyClass:
    """attribute set overload"""
    def __init__(self):
        print('MyClass object created')

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(f'MyClass object attribute set: {key} = {value}')

    def __str__(self):
        string = 'MyClass object attributes:'
        for key, value in self.__dict__.items():
            string += f'\n{key} = {value}'
        return string

    def __del__(self):
        print('MyClass object deleted')


my_object = MyClass()
my_object.zero = False
my_object.one = 'one'
my_object.two = 2
my_object.three = [False, 'one', 2]
print(my_object)
