class Equipment:
    def __init__(self, brand, model, serial):
        self.brand = brand
        self.model = model
        self.serial = serial


class Printer(Equipment):
    type = 'printer'

    def __init__(self, brand, model, serial, consumable):
        super().__init__(brand, model, serial)
        self.consumable = consumable


class Scanner(Equipment):
    type = 'scanner'


class Xerox(Equipment):
    type = 'xerox'

    def __init__(self, brand, model, serial, consumable):
        super().__init__(brand, model, serial)
        self.consumable = consumable
