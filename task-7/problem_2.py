from problem_2_lib import Coat, Suit


coats = [Coat(_) for _ in range(1, 10 + 1)]
print('- coats -', 'size consum', sep='\n')
for coat in coats:
    print(f'{coat.size:>4d} {coat.consum:>6.2f}')

print()

suits = [Suit(_) for _ in range(1, 10 + 1)]
print('- suits -', 'height consum', sep='\n')
for suit in suits:
    print(f'{suit.height:>6d} {suit.consum:>6.1f}')
