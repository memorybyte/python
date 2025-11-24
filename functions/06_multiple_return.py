## 
# If nothing is returned from function, then None is returned.
# one value can be returned
# multiple values can be returned
# early return

def make_chai():
    return 'Here is your masala chai.'
    print(f'Here is your masala chai')

returned_value = make_chai()

# print(make_chai())


def sold_cups():
    return 120

total = sold_cups()
print(total)

# Early return
def chai_status(cups_left):
    if cups_left == 0:
        return 'Sorry, chai over'
    return 'Chai is ready'

# print(chai_status(0))


# Returning multiple values

def chai_report():
    return 100, 20 # sold, remaining


sold, remaining = chai_report()

print(f'Sold: {sold}')
print(f'Remaining: {remaining}')
