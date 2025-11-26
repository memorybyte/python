## Operator Overloading
# use module operator
base_liquid = ['water', 'milk']
extra_flavor = ['ginger']

full_liquid_mix = base_liquid + extra_flavor
print(full_liquid_mix)

strong_brew = ['black_tea'] * 3
strong_brew = ['black_tea', 'tea'] * 3
print(strong_brew)

from operator import itemgetter

# bytearray
raw_spice = bytearray(b'CINNAMON')
# print(raw_spice[0])
raw_spice = raw_spice.replace(b'CINNA', b'CARD')
print(raw_spice)