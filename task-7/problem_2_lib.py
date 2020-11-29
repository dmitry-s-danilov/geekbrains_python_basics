from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consum(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consum(self):
        return self.size / 6.5 + .5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consum(self):
        return 2 * self.height + .3
