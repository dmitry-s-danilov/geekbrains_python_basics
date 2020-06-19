class Cell:
    def __init__(self, n_arg):
        n = int(n_arg)
        if n > 0:
            self.__n = n
        else:
            print('init error: non-positive cell number')
            raise Exception

    def __call__(self, n=None):
        if n is not None:
            if n > 0:
                self.__n = int(n)
            else:
                print('call error: non-positive cell number')
                raise Exception
        return self.__n

    def __str__(self):
        return str(self.__n)

    def __add__(self, other):
        return Cell(self.__n + other.__n)

    def __sub__(self, other):
        if self.__n > other.__n:
            return Cell(self.__n - other.__n)
        else:
            print('subtract error: self cell number less then other one')

    def __mul__(self, other):
        return Cell(self.__n * other.__n)

    def __truediv__(self, other):
        if self.__n >= other.__n:
            return Cell(self.__n // other.__n)
        else:
            print('division error: self cell number less then other one')

    def make_order(self, m_arg):
        m = int(m_arg)
        if m > 0:
            s = ''
            for i in range(self.__n // m):
                s += m * '*' + '\n'
            if self.__n % m:
                s += (self.__n % m) * '*'
            else:
                s = s[:-1]
            return s
        else:
            print('make order error: non-positive order number')
