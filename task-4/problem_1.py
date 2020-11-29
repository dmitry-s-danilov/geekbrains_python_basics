from sys import argv


def calculate_salary():
    """Calculates salary from production, rate and bonus."""
    try:
        return (lambda p, r, b: p * r + b)(*[float(_) for _ in argv[1:4]])
    except TypeError:
        print('TypeError: missing required positional argument.')
    except ValueError:
        print('ValueError: could not convert string to float.')


print(calculate_salary.__doc__)
print(f'Salary: {calculate_salary()}')
