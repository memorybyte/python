# Dictionary in Python
from pprint import pprint

point = {
    'x': 1,
    'y': 2
}

point = dict(x=1, y=2) # cleaner syntax

print(point['x'], point['y'])


chai_order = dict(
    type='Masala Chai',
    size='Large',
    sugar=2
)

# pprint(chai_order)

chai_recipe = {}
chai_recipe['base'] = 'Black Tea'
chai_recipe['liquid'] = 'milk'

# print(f'Recipe Base: {chai_recipe['liquid']}')

# Delete one item
# del chai_recipe['base']
# pprint(chai_recipe)

# MEMBERSHIP
# print(f'Is sugar in the order ? {"sugar" in chai_recipe}')


chai_order = dict(
    type= 'Ginger Chai',
    size= 'Medium',
    sugar= 1
)

# pprint(f'Orer Details (KEYS): {chai_order.keys()}')
# pprint(f'Orer Details (VALUES: {chai_order.values()}')
# pprint(f'Orer Details (ITEMS): {chai_order.items()}')

# pprint(chai_order)
last_item = chai_order.popitem()
# print(f'Removed last item: {last_item}')

extra_spices = {
    'cardamom': 'crushed',
    'ginger': 'sliced'
}

# Update the existing dictionary with the new one
chai_recipe.update(extra_spices)
# pprint(chai_recipe)

# Safely extract information using get() method
customer_note = chai_order.get('note', 'No note available')
# print(f'Customer note is: {customer_note}')
