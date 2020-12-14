class WinDoor:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    @property
    def square(self):
        return self.length * self.height


class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.windoors = []

    def add_windoor(self, length, height):
        self.windoors.append(WinDoor(length, height))

    @property
    def square(self):
        return 2 * (self.length + self.width) * self.height

    @property
    def total_square(self):
        total_square = self.square
        for windoor in self.windoors:
            total_square -= windoor.square
        return total_square


room_size = 7, 4, 3.7
windoor_sizes = [(2, 2), (2, 2), (2, 2)]

room = Room(*room_size)
for _ in windoor_sizes:
    room.add_windoor(*_)

print(f'square: {room.square}')
print(f'total square: {room.total_square}')
