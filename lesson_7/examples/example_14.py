class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def method_1(self):
        return self.param_1, self.param_2

    @property
    def method_2(self):
        return self.param_1, self.param_2


my_object = MyClass('one', 'two')
print(my_object.param_1,
      my_object.param_2,
      my_object.method_1(),
      my_object.method_2,
      sep='\n')
