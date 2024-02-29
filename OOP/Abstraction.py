#abstraction Examples
#
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
    
    def parameter(self):
        return self.__side * 4
    

square = Square(10)

print(f"Square area is {square.area()}")