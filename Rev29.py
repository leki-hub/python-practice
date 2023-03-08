class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
"""Objects creation , calling then printing"""
circle1 = Circle(0, 0, 5)
rectangle1 = Rectangle(0, 0, 10, 5)
circle2 = Circle(1, 2, 6)
rectangle2 = Rectangle(1, 2, 15, 5)

print("Circle areas for circle 1  :", circle1.area())
print("Rectangle areas are :", rectangle1.area() )
print("for circle 2 is " ,circle2.area())
print("for rectangle 2 is " ,rectangle2.area())