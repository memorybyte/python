# Example 01
kettle_boiled = True
if kettle_boiled:
    print('Kettle Done !! Time to make chai!')

snack_input = input('Enter your preferred snack: ').strip().lower()
if snack_input == 'samosa' or snack_input == 'cookies':
    print(f'Great Choice! We"ll serve you {snack_input}')
else:
    print('Sorry, we only serve cookies and samosa with tea.')


# Example 02
cup = input('Choose your cup size (small/medium/large): ').strip().lower()

if cup == 'small':
    print('Price is 10 rupees')
elif cup == 'medium':
    print('Price is 15 rupees')
elif cup == 'large':
    print('Price is 20 rupees')
else:
    print('Unknown cup size')


# Example 03
device_status = 'active'
temperature = 38

if device_status == 'active':
    if temperature > 35:
        print('High Temperature')
    else:
        print('Normal Temperatue')
else:
    print('Device is offline')


# Example 04
order_amount = int(input('Enter the order amount: '))
delivery_fee = 0 if order_amount > 300 else 30
print(f'Total amout: {order_amount + delivery_fee}')


