from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def method_1(self):
        pass

    @abstractmethod
    def method_2(self):
        pass


class MyClass(MyAbstractClass):
    def method_1(self):
        pass

    def method_2(self):
        pass


my_object = MyClass()
print(my_object, type(my_object))
