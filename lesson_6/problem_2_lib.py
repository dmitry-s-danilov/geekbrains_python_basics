class Road:
    index = 0
    total_length = 0  # km
    total_area = 0  # km2
    total_mass = 0  # tn

    def __init__(self, length=None, width=None, thickness=None, density=None):
        Road.index += 1
        self.number = Road.index

        self._length = length  # km
        self._width = width  # m
        self._thickness = thickness  # cm
        self._density = density  # kg m^-2 cm-1

        Road.total_length += self._length if self._length is not None else 0

        self.area = self._length * self._width * 10**-3 \
            if self._length is not None \
            and self._width is not None \
            else None
        Road.total_area += self.area if self.area is not None else 0

        self.mass = self.area * self._thickness * self._density * 10**3 \
            if self.area is not None \
            and self._thickness is not None \
            and self._density is not None \
            else None
        Road.total_mass += self.mass if self.mass is not None else 0

    def print_info(self):
        area = round(self.area, 1) if self.area is not None else None
        mass = int(self.mass) if self.mass is not None else None
        print(f'number: {self.number}',
              f'length [km]: {self._length}',
              # f'width [m]: {self._width}',
              # f'thickness [cm]: {self._thickness}',
              # f'density [kg m-2 cm-1]: {self._density}',
              f'area [km^2]: {area}',
              f'mass [tn]: {mass}',
              sep='\n')

    def print_total(self):
        total_area = round(Road.total_area, 1) \
            if Road.total_area is not None else None
        total_mass = int(Road.total_mass) \
            if Road.total_mass is not None else None
        print(f'number: {Road.index}',
              f'length [km]: {Road.total_length}',
              f'area [km2]: {total_area}',
              f'mass [tn]: {total_mass}',
              sep='\n')
