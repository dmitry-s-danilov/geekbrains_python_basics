class MyException(Exception):
    def __init__(self, message):
        self.message = message


class MyList:
    __messages = {'create': 'list created',
                  'append': 'item appended',
                  'length': 'list length: {}',
                  'IsNotNumeric': "IsNotNumeric: item didn't append",
                  'call': 'append integers one by one' \
                          + "\nto exit type '{}'",
                  'input': 'input: ',
                  'stop': 'input stopped'}
    __input_stop = 'stop'
    __str_sep = ' '
    __str_end = ''

    def __init__(self):
        self.data = []
        print(self.__messages.get('create'))

    def __str__(self):
        return self.__str_sep.join([str(_) for _ in self.data]) \
               + self.__str_end

    @property
    def len(self):
        return len(self.data)

    def append(self, string):
        try:
            if string.isnumeric():
                item = int(string)
            else:
                raise MyException(self.__messages.get('IsNotNumeric'))
        except MyException as exception:
            print(exception, end='. ')
        else:
            self.data.append(item)
            print(self.__messages.get('append'), end='. ')
        finally:
            print(self.__messages.get('length').format(self.len))

    def input(self):
        print(self.__messages.get('call').format(self.__input_stop))
        while True:
            string = input(self.__messages.get('input')).strip()
            if string == self.__input_stop:
                break
            self.append(string)
        print(self.__messages.get('stop'))
