n = int(input('input number: '))

if n > 1:
    s = 1
elif n < -1:
    s = -1
else:
    s = 0

print('number:', n)
print('step:', s)

k = 0
if s:
    print('dividers:')
    i = 2
    while i < s * n:
        if n % i == 0:
            k += 1
            print(i)
        i += 1

print('total:', k)
