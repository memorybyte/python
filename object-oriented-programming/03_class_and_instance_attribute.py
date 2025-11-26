
# Class Attributes: 
# 1. Shared across all instances of class
# 2. Defined at class label
# 3. Can be accesses using class reference or object reference

# Instance Attributes:
# 0. Created in constructor
# 1. New attribute can be created after creating object as object creation is dynamic
# 2. Can be accessed using only object reference

class Point:
    # Class Attribute
    default_color = 'Red' 

    def __init__(self, x, y):
        # Instance Attributes: x and y
        self.x = x
        self.y = y


    def draw(self):
        print(f'Point ({self.x}, {self.y})')


p1 = Point(1, 2)
p1.z = 3
p1.draw()

p2 = Point(4, 5)
p2.default_color = 'Pink'
# print(p2.z) # z is not available in p2 

print(Point.default_color) # Class Attribute is not modified unless it is modified using class reference

Point.default_color = 'White'
print(Point.default_color)