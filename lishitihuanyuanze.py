from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Test:
    def area_test(self, shape):
        print("Area is: ", shape.get_area())

r = Rectangle(3, 4)
s = Square(3)

t = Test()
t.area_test(r) # 输出：Area is: 12
t.area_test(s) # 输出：Area is: 9
