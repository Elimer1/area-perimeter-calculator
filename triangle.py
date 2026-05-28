from calculator import Shape

class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        super().__init__(base, height, side_a, side_b, side_c)
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b= side_b
        self.side_c = side_c

    def get_area(self):
        return (self.base * self.height) / 2
    
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c 