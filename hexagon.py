from calculator import Shape
from math import sqrt

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return ((sqrt(3) * 3) / 2) * self.side * self.side
    
    def get_perimeter(self):
        return self.side * 6