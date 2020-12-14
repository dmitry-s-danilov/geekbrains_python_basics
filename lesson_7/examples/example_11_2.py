class ParentClass:
    def __init__(self, param_1):
        self.param_1 = param_1

    def __str__(self):
        return str(self.param_1)

    def __iadd__(self, other):
        self.param_1 += other
        return self

    def method_1(self, other):
        self.param_1 += other
        # return self


class ChildClass(ParentClass):
    def __init__(self, param_1, param_2):
        super().__init__(param_1)
        self.param_2 = param_2

    def __str__(self):
        return str(f'{self.param_1}, {self.param_2}')

    def __iadd__(self, other):
        super().__iadd__(other.param_1)
        self.param_2 += other.param_2
        return self

    def method_1(self, other):
        super().method_1(other.param_1)
        self.param_2 += other.param_2
        # return self


my_object = ParentClass(0)
print(my_object)

my_object += 1
print(my_object)

my_object.method_1(1)
print(my_object)

print()

my_object = ChildClass(0, 1)
print(my_object)

my_object += ChildClass(1, 1)
print(my_object)

my_object.method_1(ChildClass(1, 1))
print(my_object)
