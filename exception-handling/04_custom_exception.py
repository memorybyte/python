# Raise your own exception
def brew_chai(flavor):
    if flavor not in {'masala', 'ginger', 'elaichi'}:
        raise ValueError('Upsupported chai flavor...')
    print(f'Brewing {flavor} chai...')

# print(brew_chai('mint'))


# Create your own exception

class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError('Missing milk or sugar')
    print('Chai is ready')

make_chai(1, 1)
make_chai(1, 0)