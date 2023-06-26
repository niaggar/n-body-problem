from .Dimension2D import Dimension2D


class Energy:
    def __init__(self, mass: float, velocity: Dimension2D):
        self.mass = mass
        self.velocity = velocity

    def kinetic(self):
        return 0.5 * self.mass * (self.velocity.magnitude() ** 2)
    
    def potential(self, body):
        return -1 * (self.mass * body.mass) / self.velocity.distance(body.position)
    
    def multiple_potential(self, other_bodies):
        potential = 0
        for body in other_bodies:
            potential += self.potential(body)
        return potential
    
    def total(self, distance):
        return self.kinetic() + self.potential(distance)
