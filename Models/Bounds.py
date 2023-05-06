from .Dimenssion2D import Dimenssion2D


class Bounds:
    p1: Dimenssion2D = None
    p2: Dimenssion2D = None
    aparent_mass: float = 1
    normal_vector = {
        "left": Dimenssion2D(1, 0),
        "right": Dimenssion2D(-1, 0),
        "top": Dimenssion2D(0, -1),
        "bottom": Dimenssion2D(0, 1)
    }

    def __init__(self, p1: Dimenssion2D, p2: Dimenssion2D, aparent_mass: float = 1):
        self.p1 = p1
        self.p2 = p2
        self.aparent_mass = aparent_mass

    def contains(self, point: Dimenssion2D):
        return self.p1.x <= point.x <= self.p2.x and self.p1.y <= point.y <= self.p2.y
    
    def get_apparent_velocity(self, position: Dimenssion2D):
        if self.contains(position):
            return Dimenssion2D(0, 0)
        else:
            apparent_velocity = Dimenssion2D(0, 0)

            if position.x < self.p1.x:
                apparent_velocity += self.normal_vector["left"]
            elif position.x > self.p2.x:
                apparent_velocity += self.normal_vector["right"]
            
            if position.y < self.p1.y:
                apparent_velocity += self.normal_vector["bottom"]
            elif position.y > self.p2.y:
                apparent_velocity += self.normal_vector["top"]
            
            apparent_velocity.x *= 100
            apparent_velocity.y *= 100
            return apparent_velocity

    def __str__(self) -> str:
        return f"({self.p1}, {self.p2})"
