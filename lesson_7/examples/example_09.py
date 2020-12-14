class Salary:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print('salary equal method')
        return self.value == other.value

    def __lt__(self, other):
        print('salary less then method')
        return self.value < other.value

    def __gt__(self, other):
        print('salary greater then method')
        return self.value > other.value

    def __str__(self):
        return str(self.value)


class Bonus:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print('bonus equal method')
        return self.value == other.value

    def __lt__(self, other):
        print('bonus less then method')
        return self.value < other.value

    def __gt__(self, other):
        print('bonus greater then method')
        return self.value > other.value

    def __str__(self):
        return str(self.value)


s = Salary(10)
b = Bonus(1)
print(f'salary: {s}\nboubus: {b}')

print(s == b)
print(s < b)
print(s > b)

print(b == s)
print(b < s)
print(b > s)

