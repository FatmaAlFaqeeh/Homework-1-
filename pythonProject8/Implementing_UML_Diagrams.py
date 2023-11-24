import abc

class Shape(abc.ABC):

    @abc.abstractmethod
    def calc_perimeter(self):
        """Method documentation"""
        pass

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Perimeter of Triangle:", perim)
        return perim

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Perimeter of Rectangle:", perim)
        return perim

class Square(Shape):

    def __init__(self, a):
        self.a = a

    def calc_perimeter(self):
        perim = 4 * self.a
        print("Perimeter of Square:", perim)
        return perim

rectangle = Rectangle(4, 6)
rectangle.calc_perimeter()

square = Square(5)
square.calc_perimeter()
