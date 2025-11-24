## LIST Comprehensions

# SYNTAX: [ expression for item in iterable if condition ]

menu = [
    'Masala Chai',
    'Iced Lemon Tea',
    'Iced Peach Tea',
    'Ginger Chai'
]

# iced_tea = [tea for tea in menu if 'Iced' in tea]
iced_tea = [tea for tea in menu if len(tea) > 14]
print(iced_tea)