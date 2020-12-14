from problem_2_lib import MyException, messages

z = None
try:
    print(messages.get('call'))
    x, y = map(float, input(messages.get('input')).split())
    if y:
        z = x / y
    else:
        raise MyException(messages.get('ZeroDivisionError'))
except ValueError:
    print(messages.get('ValueError'))
except MyException as exception:
    print(exception)
else:
    z = round(z, 3)
finally:
    print(messages.get('result').format(z))
