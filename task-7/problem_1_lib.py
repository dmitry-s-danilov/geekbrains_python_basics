class Matrix:
    def __init__(self, a):
        self.__m = len(a)  # number of rows
        self.__n = len(a[0])  # number of columns
        self.__a = a  # matrix itself

    def __str__(self):
        f = [[len(str(self.__a[i][j]))
              for j in range(self.__n)]
             for i in range(self.__m)]

        f_max = f[0]
        for i in range(1, self.__m):
            for j in range(self.__n):
                if f[i][j] > f_max[j]:
                    f_max[j] = f[i][j]

        s = ''
        for i in range(self.__m):
            for j in range(self.__n):
                s += str(self.__a[i][j]).rjust(f_max[j])
                if j < self.__n - 1:
                    s += ' '
            if i < self.__m - 1:
                s += '\n'
        return s

    def __add__(self, other):
        return Matrix([[self.__a[i][j] + other.__a[i][j]
                        for j in range(self.__n)]
                       for i in range(self.__m)])

    @property
    def size(self):
        return self.__m, self.__n
