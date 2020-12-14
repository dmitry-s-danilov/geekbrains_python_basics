class MyClass:
    def __init__(self, value):
        self.value = value

    # def __setattr__(self, key, value):
    #     if key == 'value':
    #         self.__dict__[key] = value

    def __call__(self, value=None):
        if value is not None:
            self.value = value
        return self.value

    def __str__(self):
        return str(self.value)

    def __iadd__(self, other):
        self.value += other.value
        return self

    def __isub__(self, other):
        self.value -= other.value
        return self


my_object_1 = MyClass(1)
my_object_2 = MyClass(my_object_1())

my_object_1 += my_object_2
print(my_object_1)

my_object_1 -= my_object_2
print(my_object_1)
