class Figure:
    area = None

    def __init__(self, color, base, height):
        self.color = color
        self.base = base
        self.height = height

    def info(self):
        print(f'color: {self.color}',
              f'base: {self.base}',
              f'height: {self.height}',
              f'area: {self.area}',
              sep='\n')


class Triangle(Figure):
    def __init__(self, color, base, height):
        super().__init__(color, base, height)
        self.area = .5 * self.base * self.height


class Rectangle(Figure):
    def __init__(self, color, base, height):
        super().__init__(color, base, height)
        self.area = base * height


b, h = 2., 1.

triangle = Triangle('red', b, h)
print(type(triangle))
triangle.info()

print()

rectangle = Rectangle('blue', b, h)
print(type(rectangle))
rectangle.info()
