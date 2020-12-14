class Figure:
    def __init__(self, color=None, base=None, height=None):
        self.color = color
        self.base = base
        self.height = height

    def info(self):
        print(f'color: {self.color}',
              f'base: {self.base}',
              f'height: {self.height}',
              sep='\n')


class Triangle(Figure):
    def __init__(self, color=None, base=None, height=None):
        super().__init__(color, base, height)

        self.area = .5 * self.base * self.height \
            if base is not None and height is not None \
            else None

    def info(self):
        print(f'color: {self.color}',
              f'base: {self.base}',
              f'height: {self.height}',
              f'area: {self.area}',
              sep='\n')


class Rectangle(Figure):
    def __init__(self, color=None, base=None, height=None):
        super().__init__(color, base, height)

        self.area = self.base * self.height \
            if base is not None and height is not None \
            else None

    def info(self):
        print(f'color: {self.color}',
              f'base: {self.base}',
              f'height: {self.height}',
              f'area: {self.area}',
              sep='\n')


b, h = 2., 1.

triangle_1 = Triangle('red', b)
print(type(triangle_1))
triangle_1.info()

print()

triangle_2 = Triangle(base=b, height=h)
print(type(triangle_2))
triangle_2.info()

print()

rectangle_1 = Rectangle('blue', height=h)
print(type(rectangle_1))
rectangle_1.info()

print()

rectangle_2 = Rectangle(base=b, height=h)
print(type(rectangle_2))
rectangle_2.info()
