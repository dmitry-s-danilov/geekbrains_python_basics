from itertools import cycle

exit_symbol = 'q'
call_string = {'string': 'enter a string to cycle: ',
               'cycle': "input '{}' to exit: ".format(exit_symbol),
               'next': '{}: {}'}


def print_cycle(cycle_arg):
    index = 1
    while True:
        print(call_string.get('next').format(index, next(cycle_arg)))
        index += 1
        input_string = input(call_string.get('cycle'))
        if exit_symbol in input_string:
            break


try:
    print_cycle(cycle(input(call_string.get('string')).strip()))
except StopIteration:
    print('StopIteration: zero length string')
