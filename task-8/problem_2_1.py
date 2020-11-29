from problem_2_lib import messages

z = None
try:
    print(messages.get('call'))
    x, y = map(float, input(messages.get('input')).split())
    z = x / y
except ValueError:
    print(messages.get('ValueError'))
except ZeroDivisionError:
    print(messages.get('ZeroDivisionError'))
else:
    z = round(z, 3)
finally:
    print(messages.get('result').format(z))
