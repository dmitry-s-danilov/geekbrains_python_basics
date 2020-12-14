class Iterator:
    def __init__(self, start, stop, step):
        self.index = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self.index += self.step
        if self.index <= self.stop:
            return self.index
        else:
            raise StopIteration


class IteratingObject:
    def __init__(self, start, stop, step):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return Iterator(self.start, self.stop, self.step)


my_object = IteratingObject(start=0, stop=10, step=1)

for _ in my_object:
    print(_)

print()

for _ in my_object:
    print(_)
