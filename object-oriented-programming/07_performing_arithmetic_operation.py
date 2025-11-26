class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f'Point ({self.x}, {self.y})')

point = Point(1, 2) + Point(3, 5)
point.draw()