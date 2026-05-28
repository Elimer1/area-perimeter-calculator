class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return f"Shape: {self.__class__.__name__} \nArea:{self.get_area()} \nPerimeter: {self.get_perimeter()}"
