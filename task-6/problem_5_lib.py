class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationary):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'start drawing with {self.color} pen')


class Pencil(Stationary):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'start drawing with {self.color} pencil')


class Handle(Stationary):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'start drawing with {self.color} handle')
