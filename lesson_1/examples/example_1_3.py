input_color = input('input color: ')

color = 'red'
if input_color == color:
    print('color:', color)
else:
    color = 'green'
    if input_color == color:
        print('color:', color)
    else:
        color = 'blue'
        if input_color == color:
            print('color:', color)
        else:
            color = 'unknown'
            print('color:', color)
