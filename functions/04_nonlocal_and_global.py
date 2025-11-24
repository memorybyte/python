## nonlocal
def update_order():
    chai_type = 'Elaichi'
    def kitchen():
        # nonlocal chai_type
        chai_type = 'Kesar'
    kitchen()

    print(f'After kitched update: {chai_type}')


# update_order()


## global

chai_type = 'Plain'

def front_desk():
    chai_type = 'Elaichi'
    def kitchen():
        global chai_type
        # nonlocal chai_type
        chai_type = 'Irani'
    
    kitchen()

front_desk()
print(f'{chai_type}')