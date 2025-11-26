class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
point.draw()
# While calling the draw() method no need to pass any value for self
# Python interpreter does it for us
# It is optional


# Point.draw(Point(3, 4)) # Intentionally passing another object