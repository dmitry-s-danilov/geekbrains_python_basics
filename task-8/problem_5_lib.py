from problem_4_lib import Unit


class Counting:
    count = 0
    placement = dict()

    def __init__(self, departments):
        for department in departments:
            self.placement[department] = []

    def __str__(self):
        s = ''
        for department, equipment in self.placement.items():
            s += f'{department}:\n'
            for unit in equipment:
                s += f'{unit}\n'
        return s

    def take(self, device, department):
        self.count += 1
        self.placement[department]\
            .append(Unit(device.type,
                         device.brand, device.model, device.serial,
                         self.count))

    def move(self, number, department):
        operation = False
        for equipment in self.placement.values():
            for unit in equipment:
                if unit.number == number:
                    self.placement[department]\
                        .append(equipment.pop(equipment.index(unit)))
                    operation = True
                    break
            if operation:
                break

    def remove(self, number):
        operation = False
        for equipment in self.placement.values():
            for unit in equipment:
                if unit.number == number:
                    equipment.pop(equipment.index(unit))
                    operation = True
                    break
            if operation:
                break
