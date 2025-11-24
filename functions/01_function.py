## Example 01
def print_order(name, chai_type):
    print(f'{name} ordered {chai_type} chai !!!')

# print_order('John Doe', 'Masala')
# print_order('Jane Doe', 'Ginger')
# print_order('Jia', 'Tulsi')


## Example 02
# Splitting complex task

def fetch_sales():
    print(f'Fetching the sales data...')

def filter_valid_orders():
    print(f'Filtering valid sales data...')

def summarize_data():
    print(f'Summarizing sales data...')

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()

generate_report()