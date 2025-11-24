## Example 01
chai = 'Ginger Tea'

def prepare_chai(order:  "str"):
    print(f'Preparing: {order}')

# prepare_chai(chai)


## Example 02
chai = [1, 2, 3]
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)

# print(chai)

## Example 03
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# make_chai('Darjeeling', 'Yes', 'Low') # Positional Arguments, 
# make_chai(tea='Green', sugar='Medium', milk='No') # Keyword


## Example 04
def special_chai(*ingredients, **extras):
    print(f'Ingredients: {ingredients}')
    print(f'Extras: {extras}')

# special_chai('Cinnamon', 'Cardamom', sweetner='Honey', foam='Yes')


## Example 05 (default values)
# def chai_order(order=[]):
#     order.append('Masala Chai')
#     print(order)

# chai_order()
# chai_order() # Bug

def chai_order(order=None):
    if order is None:
        order = []

    print(order)

chai_order()
chai_order()