from problem_4_lib import Device

devices = [{'type': 'printer',
            'brand': 'minimal_', 'model': 'print_one', 'serial': 'MIP1'},
           {'type': 'scanner',
            'brand': 'minimal_', 'model': 'scan_one', 'serial': 'MIS1'},
           {'type': 'copier',
            'brand': 'minimal_', 'model': 'copy_one', 'serial': 'MIC1'}]
devices = [Device(**_) for _ in devices]

print('devices:')
for _ in enumerate(devices, 1):
    print(_[0], _[1], sep='. ')
