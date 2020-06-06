"""
Задача 6.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
"""

# set training factor
d = 1.1

# input a first day result
a = float(input('Введите начальный результат: '))
# input a goal result
b = float(input('Введите общий результат: '))

if 0 < a and 0 < b:
    # let's train
    # init a day number equal to one
    n = 1
    # init a day result equal to the first day result
    x = a
    while True:
        # compare the day result with the goal result
        if x >= b:
            # output the day number
            print(n)
            break
        # increase a day
        n += 1
        # increase a result
        x *= d
else:
    print('Некорректная постановка задачи.')
