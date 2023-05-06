from Models import Dimenssion2D


class Potencial:
    M = 0
    m = 0
    G = 1
    source = Dimenssion2D(0, 0)

    def __init__(self, M=0, m=0, G=1, source=Dimenssion2D(0, 0)):
        self.M = M
        self.m = m
        self.G = G
        self.source = source

    def calculate(self, point: Dimenssion2D):
        distance = point.distance(self.source)
        return -1 * (self.G * self.M) / (distance)**(1)