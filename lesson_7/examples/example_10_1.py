class MyClass:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if key == 'value':
            self.__dict__[key] = value

    def __call__(self, value=None):
        if value is not None:
            self.value = value

    def __str__(self):
        return str(self.value)

    def __iadd__(self, other):
        self.value += other
        return self

    def __isub__(self, other):
        self.value -= other
        return self


my_object = MyClass(1)
print(f'create with init: value = {my_object}')

my_object.value = 2
print(f'change with setattr: value = {my_object}')

my_object(3)
print(f'change with call: value = {my_object}')

my_object += 1
print(f'increment with iadd: value = {my_object}')

my_object -= 1
print(f'decrement with isub: value = {my_object}')
