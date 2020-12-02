from problem_4_lib import Device
from problem_5_lib import Counting


devices = [{'type': 'printer',
            'brand': 'minimal_', 'model': 'print_one', 'serial': 'MIP1'},
           {'type': 'scanner',
            'brand': 'minimal_', 'model': 'scan_one', 'serial': 'MIS1'},
           {'type': 'copier',
            'brand': 'minimal_', 'model': 'copy_one', 'serial': 'MIC1'}]
devices = [Device(**_) for _ in devices]
print('get devices:')
for _ in enumerate(devices, 1):
    print(_[0], _[1], sep='. ')

departments = 'office', 'storage'
counting = Counting(departments)
print(f'\ninitiate counting:\n{counting}')

department = 'storage'
for device in devices:
    counting.take(device, department)
print(f'take all devices to {department}:\n{counting}')

department = 'office'
for _ in range(1, counting.count + 1):
    counting.move(_, department)
print(f'move all devices to {department}:\n{counting}')

for _ in range(1, counting.count + 1):
    counting.remove(_)
print(f'remove all devices:\n{counting}')
