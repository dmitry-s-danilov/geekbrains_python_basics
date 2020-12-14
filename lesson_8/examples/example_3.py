class MyClass:
    @classmethod
    def my_method(cls, param):
        print(cls, param)

MyClass.my_method(1)
my_object = MyClass()
my_object.my_method(2)
