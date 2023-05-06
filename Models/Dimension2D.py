import math


class Dimension2D:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other_dimenssion):
        return math.sqrt((self.x - other_dimenssion.x)**2 + (self.y - other_dimenssion.y)**2)
    
    def scale(self, value):
        return Dimension2D(self.x * value, self.y * value)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        return Dimension2D(self.x / self.magnitude(), self.y / self.magnitude())
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, other_dimenssion):
        return Dimension2D(self.x + other_dimenssion.x, self.y + other_dimenssion.y)
    
    def __sub__(self, other_dimenssion):
        return Dimension2D(self.x - other_dimenssion.x, self.y - other_dimenssion.y)
    
    def __mul__(self, value):
        if value == int or value == float:
            return Dimension2D(self.x * value, self.y * value)
        elif isinstance(value, Dimension2D):
            return self.x * value.x + self.y * value.y
        else:
            raise Exception("Invalid operation")
    
    def __eq__(self, other):
        if isinstance(other, Dimension2D):
            return self.x == other.x and self.y == other.y
        return False
