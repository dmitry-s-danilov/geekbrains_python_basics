class Complex:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __add__(self, other):
        return Complex(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, other):
        return Complex(self.__x * other.__x - self.__y * other.__y,
                       self.__x * other.__y + self.__y * other.__x)

    def __abs__(self):
        return (self.__x ** 2 + self.__y ** 2) * .5

    def __str__(self):
        if self.__x and self.__y:
            z = f'{self.__x}+{self.__y}i' if self.__y > 0 \
                else f'{self.__x}{self.__y}i'
        elif self.__x and not self.__y:
            z = f'{self.__x}'
        elif not self.__x and self.__y:
            z = f'{self.__y}i'
        else:
            z = '0'
        return z

    @property
    def real(self):
        return self.__x

    @property
    def imag(self):
        return self.__y
