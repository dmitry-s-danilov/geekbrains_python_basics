class Device:
    def __init__(self, type, brand, model, serial):
        self.type = type
        self.brand = brand
        self.model = model
        self.serial = serial

    def __str__(self):
        s = ', '.join((f'type: {self.type}',
                       f'brand: {self.brand}',
                       f'model: {self.model}',
                       f'serial: {self.serial}'))
        return s


class Unit(Device):
    def __init__(self, type, brand, model, serial, number):
        super().__init__(type, brand, model, serial)
        self.number = number

    def __str__(self):
        s = ', '.join((f'number: {self.number}',
                       f'type: {self.type}',
                       f'brand: {self.brand}',
                       f'model: {self.model}',
                       f'serial: {self.serial}'))
        return s
