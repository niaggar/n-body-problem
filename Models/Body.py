import logging

# from Methods import Energy
from .Dimension2D import Dimension2D


class Body:
    logger = logging.getLogger("main")
    name: str = ""
    mass: float = 0
    radius: float = 0
    color: tuple[float] = (0, 0, 0)
    position: Dimension2D = Dimension2D(0, 0)
    velocity: Dimension2D = Dimension2D(0, 0)
    aceleration: Dimension2D = Dimension2D(0, 0)
    path: list = []
    # energy: Energy = None
    _distance: int = 0
    
    def __init__(self, name: str, mass: float, radius: float, position: Dimension2D, velocity: Dimension2D, color: tuple[float]=(0, 0, 0)):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.color = color
        self.path = []
        # self.energy = Energy(mass, velocity)

    def distance(self, other_body):
        return self.position.distance(other_body.position)
    
    def add_path(self, position: Dimension2D):
        if self._distance == 4:
            self._distance = 0
            self.path.append((position.x, position.y))
        else:
            self._distance += 1

        if len(self.path) > 50:
            self.path.pop(0)

    def calculate_kinetic_energy(self):
        return self.energy.kinetic()

    def calculate_potencial_energy(self, other_body):
        distance = self.distance(other_body)
        return self.energy.potencial(distance)

    def calculate_total_energy(self, other_body):
        distance = self.distance(other_body)
        return self.energy.total(distance)

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.name == other.name
        return False
    
    def __str__(self):
        return f"Body: {self.name} with mass {self.mass} and radius {self.radius} at position {self.position} with velocity {self.velocity}"
    

