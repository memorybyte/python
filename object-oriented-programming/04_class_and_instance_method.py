class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        # cls is reference to class itself
        # To make this method a class method, we have to decorate it with @classmethod 
        # It is a way if extending behavior of a function
        return cls(0, 0) # This is exactly like calling Point(0, 0)        

    def draw(self):
        print(f'Point ({self.x}, {self.y})')

point = Point.zero()
point.draw()

