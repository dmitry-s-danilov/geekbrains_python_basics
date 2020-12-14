class MyClass:
    # set class attributes
    _attr_1 = 'class protected attribute'
    __attr_2 = 'class private attribute'

    # set item constructor
    def __init__(self):
        self._attr_3 = 'item protected attribute'
        self.__attr_4 = 'item private attribute'

    # set class methods
    def _meth_1(self):
        print('class protected method')

    def __meth_2(self):
        print('class private method')


# create class item
my_object = MyClass()

# get item attributes
print(my_object._attr_1,
      # MyClass._attr_1,
      my_object._MyClass__attr_2,
      my_object._attr_3,
      my_object._MyClass__attr_4,
      sep='\n')

# apply class methods
my_object._meth_1()
my_object._MyClass__meth_2()
