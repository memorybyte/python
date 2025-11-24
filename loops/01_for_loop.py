## Example 01
# A tea stall owner has a digital display.
# For every customer in line. a token number is printed and chai is served.
# Task: 
#     - Use a for loop to generate token numbers from 1 to 10 using range()
#     - Print: 'Serving chai to Token #[number]'

for token in range(1, 11):
    print(f'Serving chai to Token #{token}')

## Example 02
for batch in range(1, 5):
    print(f'Preparing chai for batch #{batch}')

## Example 03
# Loop through list
orders = [
    'name1', 'name2', 'name3', 'name4'
]

for name in orders:
    print(f'Order ready for {name}')


## Example 04
# enumerate()
menu = ['Green', 'Lemon', 'Spiced', 'Mint']
# for m in menu:
#     print(f'Menu item is {m}')

for index, m in enumerate(menu, start=1):
    print(f'Menu item @{index} is {m}')

## Example 05
# zip()
names = ['name1', 'name2', 'name3', 'name4']
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f'Bill for {name} is {amount}')