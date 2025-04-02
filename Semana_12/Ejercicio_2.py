import math
from abc import ABC, abstractmethod

class Shape (ABC):

    @abstractmethod
    def calculate_perimeter (self):
        pass

    @abstractmethod
    def calculate_area (self):
        pass

class Circle (Shape):

    def __init__ (self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    def calculate_area(self):
        return math.pi*self.radius*self.radius 

class Square(Shape):

    def __init__ (self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4*self.side
    def calculate_area(self):
        return self.side*self.side

class Rectangle (Shape):

    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2*(self.length + self.width)
    def calculate_area(self):
        return self.length * self.width   
    
rectangle = Rectangle (2,4)
print (f'Rectangle Perimeter: {rectangle.calculate_perimeter()}, Rectangle area: {rectangle.calculate_area()}')
square = Square (5)
print (f'Square Perimeter: {square.calculate_perimeter()}, Square area: {square.calculate_area()}')
circle = Circle (2)
print (f'Circle Perimeter: {circle.calculate_perimeter()}, Circle area: {circle.calculate_area()}')