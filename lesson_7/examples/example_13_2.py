class IteratingObject:
    def __init__(self, start, stop, step):
        self.index = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.step
        if self.index <= self.stop:
            return self.index
        else:
            raise StopIteration


my_object = IteratingObject(start=0, stop=10, step=1)

for _ in my_object:
    print(_)

for _ in my_object:
    print(_)
