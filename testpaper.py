from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
r = Rectangle(5, 10)
c = Circle(7)   
s = Square(4)
print("Area of Rectangle:", r.area())  # Area of Rectangle: 50
print("Area of Circle:", c.area())     # Area of Circle: 153.86     
print("Area of Square:", s.area())     # Area of Square: 16