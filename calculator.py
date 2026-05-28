class Shape:
    def __init__(self, *args):
        for arg in args:
            self.input_validator(arg)

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return f"Shape: {self.__class__.__name__} \nArea:{self.get_area()} \nPerimeter: {self.get_perimeter()}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self.__dict__.values())}"

    @staticmethod
    def input_validator(num):
        if not isinstance(num, (int, float)):
            raise ValueError("Invalid Input: Input must be a number")
        if num <= 0:
            raise ValueError("Invalid Input: Number must be greater than 0")
        return True
    

