# Multilevel inheritance should be avoided
# Should be limited to 1 or 2 level, not more than that

# Below, Chicken is a Bird, but it can not fly

class Animal:
    def eat(self):
        print('eat')
    
class Bird(Animal):
    def fly(self):
        print('fly')

class Chicken(Bird):
    pass