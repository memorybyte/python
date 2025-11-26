# set is an unordered set
# indexing is not possible

numbers = [1, 2, 1, 3, 4]
uniques = set(numbers)
# print(uniques)

second = {1, 4}
second.add(5)
# print(second)
second.remove(1)
# print(second)

essential_spices = {'cardamom', 'ginger', 'cinnamon'}
optional_spices = {'ginger', 'cloves', 'black pepper'}

first = set([1, 1, 2, 3, 4])
second = {1, 5, 4}

# SET UNION
all_spices = essential_spices | optional_spices
# print(all_spices)
# print(first | second)

# SET INTERSECTION
common_spices = essential_spices & optional_spices
# print(common_spices)
# print(first & second)


# SET DIFFERENCE
only_in_essential = essential_spices - optional_spices
# print(only_in_essential)
# print(first - second)

# Symmetric Difference
# either in A or in B, but not both
print(first ^ second)


# Membership in set
# print(f'Is "cloves" in optional spices ? {"cloves" in optional_spices}')

## FROZEN SET
