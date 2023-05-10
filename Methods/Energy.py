
class Energy:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    def kinetic(self):
        return 0.5 * self.mass * self.velocity**2
    
    def potential(self, distance):
        return -1 * self.mass / distance
    
    def total(self, distance):
        return self.kinetic() + self.potential(distance)
