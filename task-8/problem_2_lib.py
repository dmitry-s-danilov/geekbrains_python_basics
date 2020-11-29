class MyException(Exception):
    def __init__(self, message):
        self.message = message


messages = {'call': 'for division input two numbers separated by whitespaces',
            'input': 'input: ',
            'result': 'result: {}',
            'ValueError': 'ValueError',
            'ZeroDivisionError': 'ZeroDivisionError'}
