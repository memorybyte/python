
# Everything is object in Python.

# Every object has its own:
# 1. Identity
# 2. Type
# 3. Value

# Mutable: which is changable
# Immutable: which is not changable


## Immutable Example
sugar_amount = 2
print(f'Initial sugar: {sugar_amount}, ID: {id(sugar_amount)}')

sugar_amount = 12
print(f'Second Initial sugar: {sugar_amount}, ID: {id(sugar_amount)}')
# Both IDs are different


## Mutable
spice_mix = set()
print(f'Initial spice mix id: {id(spice_mix)}')
spice_mix.add('Ginger')
spice_mix.add('Cardamom')
print(f'After spice mix id: {id(spice_mix)}')