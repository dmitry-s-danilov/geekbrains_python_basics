from problem_2_lib import Road


length = 5  # km
width = 20  # m
thickness = 5  # cm
density = 25  # kg m^-2 cm^-1

roads = [
    Road(),  # проселок
    Road(length),  # грунтовка
    Road(length, width),  # бетонка
    Road(length, width, thickness - 1, density),  # украли асфальт
    Road(length, width, thickness, density)]

print('- roads -')
for _ in roads:
    _.print_info()
    print()

print('- total -')
roads[0].print_total()
