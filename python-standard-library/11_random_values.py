"""Generating random values"""

import random

# print(random.random()) # Generates a random value between 0 and 1
# print(int(random.random() * 100)) # Get a random number between 0 to 100

# random.randint(): Generate a random number between two integers
# print(random.randint(1, 100))

# random.choice(): Randomly pick item from the array
# print(random.choice(tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))

# random.choices(): Randomly pick items from the array, specify the k value
# print(random.choices(tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), k=5))

# random.shuffle(): randomly reorders (shuffles) the elements of a list in place.
# It modifies the original list and returns None.
# It only works with mutable sequences like lists (not strings or tuples).
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)


# Generate random password
import string

password = ''.join(
    random.choices(
        string.ascii_letters + '@#!$' + string.digits,
        k=6 # password length = 6
    )
)
print(f'Password: {password}')