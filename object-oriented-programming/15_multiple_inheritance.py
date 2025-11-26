class Employee:
    def greet(self):
        print('Employee Greet')

class Person:
    def greet(self):
        print('Person Greet')

# Multiple Inheritance
class Manager(Employee, Person):
    pass

m = Manager()
m.greet()
print(Manager.__mro__)


# A good example

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

# A fish that can swim and fly
class FlyingFish(Flyer, Swimmer):
    pass