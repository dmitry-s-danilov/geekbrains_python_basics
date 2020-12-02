from problem_5_lib import Pen, Pencil, Handle


stationaries = [Pen('just a pen', 'red'),
                Pencil('just a pencil', 'green'),
                Handle('just a handle', 'blue')]

for index, stationary in enumerate(stationaries, 1):
    print(f'- {index} - ', stationary.title, sep='\n')
    stationary.draw()
    print()
