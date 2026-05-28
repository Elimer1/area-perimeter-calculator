from calculator import Shape
from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle

r1 = Rectangle(5, 10)
s1 = Square(4)
t1 = Triangle(6, 4, 5, 5, 6)
c1 = Circle(3)
h1 = Hexagon(7)

shape_list = [r1, s1, t1, c1, h1]

for shape in shape_list:
    print(shape)
    print()
