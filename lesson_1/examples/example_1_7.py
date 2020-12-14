number_1 = float(input('input first number: '))
number_2 = float(input('input second number: '))

if number_1 >= number_2:
    print("second number isn't greater")
    if number_1 > number_2:
        print('first number is greater')
    else:
        print('numbers are equal')
elif number_1 <= number_2:
    print("first number isn't greater")
    if number_1 < number_2:
        print('second number is greater')
    else:
        print('numbers are equal')
