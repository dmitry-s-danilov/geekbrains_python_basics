from functools import partial
from problem_4_lib import open_for_read, read_file_1,\
    open_for_write, write_file_1,\
    translate_1, eng_to_rus

in_file = 'text_4.txt'
lines = open_for_read(in_file, read_file_1)
if lines is not None:
    print(f'input: {in_file}')
    for line in lines:
        print(line, end='')

    translate = partial(translate_1, dictionary=eng_to_rus)
    lines = [[translate(word.lower()) for word in line.split()]
             for line in lines]
    lines = [' '.join(line) + '\n' for line in lines]

out_file = 'text_4_translated.txt'
write_file = partial(write_file_1, lines=lines)
open_for_write(out_file, write_file)

lines = open_for_read(out_file, read_file_1)
if lines is not None:
    print(f'\noutput: {out_file}')
    for line in lines:
        print(line, end='')
