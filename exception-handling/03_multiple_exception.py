# Multiple Exception

def process_order(item, quantity):
    
    try:
        price = {'masala': 20}[item]
        cost = price * int(quantity)
        print(f'Total cost is {cost}')
    except KeyError:
        print(f'Sorry that chai is not on menu.')
    except (TypeError, ValueError):
        print(f'Quantity must be in number.')

process_order('masala', 'two')