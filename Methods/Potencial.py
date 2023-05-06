from Models import Dimension2D
import math


class Potencial:
    M = 0
    m = 0
    G = 1
    source = Dimension2D(0, 0)

    def __init__(self, M=0, m=0, G=1, source=Dimension2D(0, 0)):
        self.M = M
        self.m = m
        self.G = G
        self.source = source

    def calculate(self, point: Dimension2D):
        distance = point.distance(self.source)

        # morse_potencial = self.morse_potencial(distance)
        # return morse_potencial
        return -1 * (self.G * self.M) / (distance)**(1)
    
    def morse_potencial(self, distance):
        return -1 * (self.G * self.M * (1 - math.pow(math.e, -1/(self.G * self.M) * (distance - (self.G * self.M))))**2 - self.G * self.M)
