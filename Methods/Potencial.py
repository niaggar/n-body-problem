from Models import Dimension2D
import math


class Potencial:
    M = 0
    m = 0
    G = 1
    source = Dimension2D(0, 0)
    pot_type = "newton"

    def __init__(self, pot_type="newton", M=0, m=0, G=1, source=Dimension2D(0, 0)):
        self.M = M
        self.m = m
        self.G = G
        self.source = source
        self.pot_type = pot_type

    def calculate(self, point: Dimension2D):
        distance = point.distance(self.source)

        if self.pot_type == "morse":
            return self.morse_potencial(distance)
        elif self.pot_type == "newton":
            return self.newton_potencial(distance)
    
    def morse_potencial(self, distance):
        return -1 * (self.G * self.M * (1 - math.pow(math.e, -1/(self.G * self.M) * (distance - (self.G * self.M))))**2 - self.G * self.M)
    
    def newton_potencial(self, distance):
        return -1 * (self.G * self.M) / (distance)**(1)
