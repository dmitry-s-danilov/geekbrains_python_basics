class Transport:
    transport_attribute = 'transport attribute'

    def transport_method(self):
        print('transport method')


class Auto(Transport):
    auto_attribute = 'auto attribute'

    def auto_method(self):
        print('auto method')


class Bus(Transport):
    bus_attribute = 'bus attribute'

    def bus_method(self):
        print('bus method')


# create class item
auto = Auto()
print(auto, type(auto), sep='\n')

# get attributes
print(auto.transport_attribute,
      auto.auto_attribute,
      sep='\n')

# apply methods
auto.transport_method()
auto.auto_method()

print()

# create class item
bus = Bus()
print(bus, type(bus), sep='\n')

# get attributes
print(bus.transport_attribute,
      bus.bus_attribute,
      sep='\n')

# apply methods
bus.transport_method()
bus.bus_method()
