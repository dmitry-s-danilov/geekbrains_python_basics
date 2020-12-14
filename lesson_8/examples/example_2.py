class MyClass:
    @staticmethod
    def method_1_1(param_1, param_2):
        return param_1 + param_2

    def method_1_2(self, param_1, param_2):
        return MyClass.method_1_1(param_1, param_2)  # static method call

    def method_1_3(self, param_1, param_2):
        return self.method_1_1(param_1, param_2)  # static method call

    def method_2_1(self, param_1, param_2):
        return param_1 + param_2

    def method_2_2(self, param_1, param_2):
        return self.method_2_1(param_1, param_2)  # regular method call


param = 1, 2
print(MyClass.method_1_1(*param))
mc = MyClass()
print(mc.method_1_2(*param))
print(mc.method_1_3(*param))
print(mc.method_2_1(*param))
print(mc.method_2_2(*param))
