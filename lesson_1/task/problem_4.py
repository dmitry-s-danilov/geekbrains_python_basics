"""
Задача 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# set number system base
p = 10
# set minimum digit in positive number
d_min = 1
# set maximum digit in positive number
d_max = 9

# input a number
n = int(input('Введите положительное целое число: '))

if n > 0:
    # find the number order
    q = 0
    while n // p ** (q + 1):
        q += 1

    # init maximum digit
    # equal to minimum digit in positive number
    m = d_min
    # init a rest of the number
    # equal to the number
    r = n
    # init an order of the rest
    # equal to the number order
    i = q
    while i >=0:
        # find a digit corresponding to the order
        d = r // p ** i

        # output current state
        # print(i, d, m, r)

        # check the digit
        if d > m:
            # increase the maximum digit
            m = d
            if m == d_max:
                break

        # decrease the rest
        r -= d * p ** i
        # decrease the order
        i -= 1

    # output the maximum digit
    print(m)
else:
    print('Число не положительно.')
