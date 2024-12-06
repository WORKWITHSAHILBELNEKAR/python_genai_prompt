data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}
]


success_count = sum(item['success'] for item in data)
print("Count of `success` True values:", success_count)
