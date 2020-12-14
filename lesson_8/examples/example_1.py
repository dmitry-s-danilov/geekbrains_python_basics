class MyClass:
    __number = 0

    def __init__(self):
        MyClass.__number += 1

    def __del__(self):
        MyClass.__number -= 1

    @staticmethod
    def number():
        return MyClass.__number


print(MyClass.number())

mc = MyClass()
print(MyClass.number())  # call a static method through a class
print(mc.number())  # call a static method through an object

del mc
print(MyClass.number())
