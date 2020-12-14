input_color = input('input color: ')
palette = 'red', 'green', 'blue'

color = 'unknown'
for c in palette:
    if c == input_color:
        color = c
        break

print('color:', color)
