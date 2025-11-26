class Point:
    def draw(self):
        print(f'Draw')


point = Point()
point.draw()
print(type(point)) # __main__.Point -> Here, __main__ is name our module

print(isinstance(point, Point))
print(isinstance(point, object))
print(isinstance(point, int))