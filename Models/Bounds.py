from .Dimension2D import Dimension2D


class Bounds:
    p1: Dimension2D = None
    p2: Dimension2D = None
    aparent_mass: float = 1
    normal_vector = {
        "left": Dimension2D(1, 0),
        "right": Dimension2D(-1, 0),
        "top": Dimension2D(0, -1),
        "bottom": Dimension2D(0, 1)
    }

    def __init__(self, p1: Dimension2D, p2: Dimension2D, aparent_mass: float = 1):
        self.p1 = p1
        self.p2 = p2
        self.aparent_mass = aparent_mass

    def contains(self, point: Dimension2D):
        return self.p1.x <= point.x <= self.p2.x and self.p1.y <= point.y <= self.p2.y
    
    def get_height(self):
        return self.p2.y - self.p1.y
    
    def get_width(self):
        return self.p2.x - self.p1.x

    def get_apparent_velocity(self, position: Dimension2D, velocity: Dimension2D):
        if self.contains(position):
            return Dimension2D(0, 0)
        else:
            apparent_velocity = Dimension2D(0, 0)

            if position.x < self.p1.x:
                apparent_velocity.x = -1 * velocity.x
            elif position.x > self.p2.x:
                apparent_velocity.x = -1 * velocity.x
            else:
                apparent_velocity.x = velocity.x

            if position.y < self.p1.y:
                apparent_velocity.y = -1 * velocity.y
            elif position.y > self.p2.y:
                apparent_velocity.y = -1 * velocity.y
            else:
                apparent_velocity.y = velocity.y

            return apparent_velocity

    def __str__(self) -> str:
        return f"({self.p1}, {self.p2})"
