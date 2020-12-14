number_1 = float(input('input first number: '))
number_2 = float(input('input second number: '))

if number_1 != number_2:
    print("numbers aren't equal")
    if number_1 > number_2:
        print('first number is greater')
    else:
        print('second number is greater')
else:
    print('numbers are equal')
