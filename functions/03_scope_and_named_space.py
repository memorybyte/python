#

def serve_chai():
    chai_type = 'Masala'  # Local Scope
    print(f'Inside function: {chai_type}')

chai_type = 'Lemon'
# serve_chai()
# print(f'Outside function: {chai_type}')

def chai_counter():
    # chai_order = 'Lemon' # Enclosing scope
    def print_order():
        # chai_order = 'Ginger'
        print(f'INNER: {chai_order}')
    print_order()
    print(f'OUTER: {chai_order}')


chai_order = 'Tulsi'
# chai_counter()
# print(f'Global: {chai_order}')


