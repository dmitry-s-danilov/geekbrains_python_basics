class Transport:
    transport_attribute = 'transport attribute'

    def transport_method(self):
        print('transport method')


class Auto(Transport):
    auto_attribute = 'auto attribute'

    def auto_method(self):
        print('auto method')


# create class item
auto = Auto()

# get attributes
print(auto.transport_attribute,
      auto.auto_attribute,
      sep='\n')

# apply methods
auto.transport_method()
auto.auto_method()
