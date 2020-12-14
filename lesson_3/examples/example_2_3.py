def my_func():
    """Calculates cylinder area from radius and height."""
    pi_number = 3.14
    radius = float(input('input radius: '))
    height = float(input('input height: '))
    area_base = pi_number * radius ** 2
    area_side = 2 * pi_number * radius * height
    area_total = 2 * area_base + area_side
    return area_base, area_side, area_total


print(f'{my_func.__name__}: {my_func.__doc__}')
print('base area: {0}\nside area:{1}\ntotal area: {2}'.format(*my_func()))
