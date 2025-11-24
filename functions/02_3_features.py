## Feature 01: Hiding Implementation Details

def get_input():
    print(f'Getting user input...')

def validate_input():
    print(f'Validating the user information...')

def save_to_db():
    print(f'Saving to Database...')

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print(f'User registration complete')

# register_user()



## Feature 02: Improving Redability

def calculate_bill(cups: int, price_per_cup: float) -> float:
    return cups * price_per_cup

bill = calculate_bill(3, 15)
# print(f'Tota Bill: {bill}')


## Feature 03: Improving Tracebility

def add_vat(price: float, vat_rate: float) -> float:
    return price * (100 + vat_rate) / 100

orders = [100, 150, 200]

for order in orders:
    final_amount = add_vat(order, 10)
    print(f'Original Value: {order}, Final with VAT: {final_amount}')

