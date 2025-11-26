
# Declaring lists:
letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters # Combine two lists
numbers = list(range(20))
chars = list('Hello World')
# print(len(chars))
# print(numbers)


## Accessing items
# print(letters[0])
# print(letters[-1]) # First letter from the end of the list

# letters[0] = 'A' # Access and modify
# print(letters[0:3])
# print(letters[:3])
# print(letters[0:])
# print(letters[:]) # Copy of the list

# print(letters[::])

# print(numbers[::2]) # Shows every 2nd numbers in the list
# print(numbers[::-1]) # Returns the reverse of the list


# Unpacking lists
numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# Cleaner way: list unpacking
# But, the number of variables in the left side should be equal to number of items in the list
first, second, third = numbers 

numbers = [1, 2, 3, 5, 5, 5, 5, 5, 10]
first, second, *rest = numbers
# print(rest)
frist, *rest, last = numbers
# print(last)

# Looping over lists
letters = ['a', 'b', 'c']

for letter in letters:
    pass
    # print(letter)

# To get the index and value: enumerate()
# enumerate() returns a tuple
# we are unpacking tuple as index and value
for index, value in enumerate(letters):
    pass
    # print(f'At: {index}, value: {value}')

## Adding elements
# 1. adding: append(), insert()
letters = ['a', 'b', 'c']

# append()
letters.append('e') # inserts at the end

# insert(index, value) # inserts at a specific index
letters.insert(3, 'd')
# print(letters)

## Removing elements: pop(), pop(index), remove(value), del lst[index], del lst[1: 4]

# removing from the end
letters.pop() # removes the last element

letters.pop(0)
# print(letters)

# remove(value): if value does not exists, generate exception
# letters.remove('a')
# print(letters)

# Using del keyword: one or sequence of items can be deleted
del letters[0]
del letters[1:]
# print(letters)

# Remove all elements at once
letters.clear() # empty list
# print(letters)

# Finding items: index(item)
letters = ['a', 'b', 'c']

# print(letters.index('a'))
# print(letters.index('d')) # Generates error

# First check if element is in the list, then find the index
if 'd' in letters:
    print(letters.index('d'))

# count('d'): number of occurrences of the item 'd'
# print(letters.count('d'))


# Sorting Lists
numbers = [3, 51, 2, 8, 6]
# numbers.sort() # inplace sorting in ascending order
# numbers.sort(reverse=True)
# print(numbers)

# using built-in function: sorted() -> returns a new list, does not modify the original list
sorted_numbers = sorted(numbers, reverse=False)
sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)

# Sorting complex list/objects
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

# define a function which takes one item as argument
# return the value which will be used for sorting

def sort_item(item):
    return item[1]

items.sort(key=sort_item, reverse=False)
items.sort(key=sort_item, reverse=True)
# print(items)

# There is a cleaner way of doing above thing: using Lambda Function

# Lambda Functions
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
    ('Product4', 4)
]

items.sort(key=lambda item: item[1], reverse=False)
# print(items)


# map() function:
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
    ('Product4', 4)
]

prices = []
for item in items:
    prices.append(items[1])

prices = map(lambda item: item[1], items)
# print(list(prices))

# filter() function:
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
    ('Product4', 4)
]

prices = filter(lambda item: item[1] >= 10, items)
# print(list(prices))

# List Comprehension
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
    ('Product4', 4)
]

# map()
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

# filter()
prices = list(filter(lambda item: item[1] >= 10, items))
prices = [item for item in items if item[1] >= 10]
# print(prices)

# zip() function:
list1 = [1, 2, 3]
list2 = [10, 20, 30]

zipped = list(zip(list1, list2))
# print(zipped)

# Stack:
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
# print(browsing_session)
last = browsing_session.pop()
# print(browsing_session)

# print(browsing_session[-1]) # top of the stack

# Queue:
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(f'Queue: {queue}')
queue.popleft()
queue.popleft()
queue.popleft()
print(f'Queue: {queue}')

if not queue:
    print('Empty')



ingredients = ['water', 'milk', 'black tea']
ingredients.append('sugar')
# print(f'Ingredients: {ingredients}')
ingredients.remove('water') # Removes the first occurence of 'water'
# print(f'Ingredients: {ingredients}')

spice_options = ['Ginger', 'Cardamom']
chai_ingredients = ['Water', 'Milk']

chai_ingredients.extend(spice_options)
# print(chai_ingredients)

chai_ingredients.insert(2, 'Black Tea')
# print(chai_ingredients)

last_added = chai_ingredients.pop()
# print(f'Last Added: {last_added}')

# Reverse the list
chai_ingredients.reverse()
# print(chai_ingredients)

# Sort the list
chai_ingredients.sort()
# print(chai_ingredients)

sugar_levels = [1, 2, 3, 4, 5]
# print(f'Maximum sugar level:{max(sugar_levels)}')
# print(f'Minimum sugar level:{min(sugar_levels)}')



# Unpacking Operator

numbers = [1, 3, 2]
# print(numbers)
# print(*numbers)


values = list(range(5))
values = [*range(5), *'Hello']
# print(values)

first = [1, 2, 3]
second = [3]
values = [*first, *'HI', *second]
# print(values)

first = {'x': 1}
second = {'x': 10, 'y': 11}
combined = {**first, **second, 'z': 1} # last value of x will be used which is 10
print(combined)