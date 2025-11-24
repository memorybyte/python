# Walrus Operator
value = 13
remainder = value % 5

# if remainder:
#     print(f'Not divisible, remainder is {remainder}')

# Using walrus operator: calculate and compare simultaneously
if (remainder := value % 5):
    print(f'Not divisible, remainder is {remainder}')

available_sizes = ['small', 'medium', 'large']
if (requested_size := input('Enter your chai cup size: ')) in available_sizes:
    print(f'Serving {requested_size} chai.')
else:
    print(f'Size is unavailable - {requested_size}')


# 
flavours = ['masala', 'ginger', 'lemon', 'mint']
print(f'Available flavours: {flavours}')
while (flavour := input('Choose your flavour: ')) not in flavours:
    print(f'Sorry, {flavour} is not available')

print(f'You choose {flavour} chai')



# Example: 

users = [
    {'id': 1, 'total': 100, 'coupon': 'P20'},
    {'id': 2, 'total': 150, 'coupon': 'F10'},
    {'id': 3, 'total': 80, 'coupon': 'P50'},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10), # Flat 10 rupee off
}

for user in users:
    percent, fixed = discounts.get(user['coupon'], (0, 0))
    discount = user['total'] * percent + fixed
    print(f'{user['id']} paid {user['total']} and got discount of next visit of rupees {discount}')