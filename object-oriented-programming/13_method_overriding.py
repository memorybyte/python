class Animal:
    def __init__(self):
        print('Animal Constructor')
        self.age = 1

    def eat(self):
        print('eat')

class Mammal(Animal):
    # __init__() is overridden here
    # super() has to be used to call base class constructor
    # It is not necessary to call base class constructor first in python
    def __init__(self):
        super().__init__()
        print('Mammal Constructor')
        self.weight = 1
        # super().__init__() # can be called later

    def walk(self):
        print('walk')

m = Mammal()
print(m.age)
print(m.weight)