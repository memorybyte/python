from fractions import Fraction
from decimal import Decimal

## Numbers:
#   1. Integers
#   2. Boolean
#   3. Real (Floating)
#   4. Complex Numbers

# 1. Numbers
black_tea_grams = 14
ginger_grams = 3

total_grams  = black_tea_grams + ginger_grams
print(f'Total grams of base tea is {total_grams}')

remaining_tea = black_tea_grams - ginger_grams
print(f'Total grams of remaining tea is {remaining_tea}')


# 2. Boolean
is_boiling = True
stri_count = 5
# False: 0, True: 1
total_actions = stri_count + is_boiling # type casting
print(f'Total actions: {total_actions}')

milk_present = 0 # no milk
print(f'Is there milk? {bool(milk_present)}')   


# Logical operators: and, or, not

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f'Can serve chai ? {can_serve}')

# 3. Real Numbers: float
ideal_temp = 95.5
current_temp = 95.4999999999
print(f'Ideal temperature: {ideal_temp}')
print(f'Current temperature: {current_temp}')
print(f'Difference temperature: {ideal_temp - current_temp}')