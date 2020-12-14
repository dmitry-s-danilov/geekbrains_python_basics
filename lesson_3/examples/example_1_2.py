def ext_func(a):
    def int_func(b):
        return b + a
    return int_func


x, y = 1, 2
obj_func = ext_func(x)
z = obj_func(y)
print(f'{type(z)}: {y} + {x} = {z}')

x, y = '1', '2'
obj_func = ext_func(x)
z = obj_func(y)
print(f'{type(z)}: {y} + {x} = {z}')
