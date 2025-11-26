# object Class:
# object class is the base class of classes, directly or indirectly inherited from it

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')

class Mammal(Animal):
    def walk(self):
        print('walk')

class Fish(Animal):
    def swim(self):
        print('walk')

m = Mammal()

print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

o = object()

print(issubclass(Mammal, object))
print(issubclass(Mammal, Animal))