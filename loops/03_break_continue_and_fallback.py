flavours = ['Ginger', 'Out of Stock', 'Lemon', 'Discontinued', 'Tulsi']

for flavour in flavours:
    if flavour == 'Out of Stock':
        continue
    
    if flavour == 'Discontinued':
        print(f'{flavour} item found')
        break
    print(f'{flavour} item found')

print(f'Outside of loop')

# for...else

staff = [
    ('Amit', 16),
    ('Zara', 17),
    ('Raj', 15)
]

for name, age in staff:
    if age >= 18:
        print(f'{name} is eligible to manage the staff')
        break
else:
    print(f'No one is eligible to manage the staff')