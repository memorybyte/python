class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y 

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(1, 3)

print(point1 == point2)
print(point1 < point2)
print(point1 > point2)
print(point1 == point3)