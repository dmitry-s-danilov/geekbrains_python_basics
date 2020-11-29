from functools import partial
from problem_2_lib import open_file, print_file_2, filter_isalnum

files = ['text_3.txt',
         'text_4.txt',
         'text_6.txt',
         'text_666.txt',
         'text_7.txt',
         'text_77.json']

print_file = partial(print_file_2, word_filter=filter_isalnum)
for file in files:
    print(f'file: {file}')
    open_file(file, print_file)
    print('\n')
