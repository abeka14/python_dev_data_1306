import math
from abc import ABC, abstractmethod
from geometry.utils import is_right_triangle


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if min(a, b, c) <= 0:
            raise ValueError("All sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        return is_right_triangle(self.a, self.b, self.c)
