"""
Задача 3.
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

# init number system base
p = 10
# init one-reduced sequence length
k = 2

# input a number
n = int(input('Введите целое число:'))

# find the number sign
if n >= 0:
    r = 1
else:
    r = -1

# find the number order
q = 0
while r * n // p ** (q + 1):
    q += 1

# find a sequence sum of sequence sums
s, i = 0, 0
while i <= k:
    s_i, j = 0, 0
    while j <= i:
        s_i += p ** ((q + 1) * j)
        j += 1
    s += s_i
    i += 1

# find a sum of numbers
# by scaling the sequence sum with the number
n_s = n * s

# output the sum of numbers
print(n_s)
