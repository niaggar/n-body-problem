import logging
from Models import Body, Bounds, Dimension2D
from .Potencial import Potencial
from .Derivate import Derivate


class Verlet:
    logger = logging.getLogger("main")
    bounds: Bounds = None
    list_bodies: list[Body] = []
    
    actual_time: float = 0
    dt: float = 0
    
    potencial: Potencial = None
    derivate: Derivate = None
    
    kinetic_energy_data = []


    def __init__(self, list_bodies: list, dt: float, bounds: Bounds = None, potencial: Potencial = None):
        self.list_bodies = list_bodies
        self.dt = dt
        self.bounds = bounds
        self.potencial = potencial
        self.derivate = Derivate(self.potencial, 0.0001)

    def calculate_aceleration(self) -> list[Dimension2D]:
        acelerations: list[Dimension2D] = []
        for body in self.list_bodies:
            body_aceleration = Dimension2D(0, 0)
            
            for other_body in self.list_bodies:
                if body != other_body:
                    self.potencial.source = other_body.position
                    self.potencial.M = other_body.mass
                    self.potencial.m = body.mass

                    acel = Dimension2D(0, 0)
                    distance = body.position.distance(other_body.position)
                    if distance > (body.radius + other_body.radius):
                        acel = self.derivate.partial(body.position)
                    
                    body_aceleration.x += -1 * acel.x
                    body_aceleration.y += -1 * acel.y

            acelerations.append(body_aceleration)
        
        return acelerations
    
    def calculate_elastic_clash(self, aceleration_k) -> None:
        for body in self.list_bodies:
            body_aceleration_k = aceleration_k[self.list_bodies.index(body)]

            new_position = Dimension2D(0, 0)
            new_position.x = body.position.x + body.velocity.x * self.dt + (1/2) * body_aceleration_k.x * self.dt**2
            new_position.y = body.position.y + body.velocity.y * self.dt + (1/2) * body_aceleration_k.y * self.dt**2

            # Calculate the new velocity of the body after a clash with the bounds
            if self.bounds is not None:
                if not self.bounds.contains(new_position):
                    v1x = body.velocity.x
                    v1y = body.velocity.y

                    apparent_velocity = self.bounds.get_apparent_velocity(new_position, body.velocity)
                    v2x = apparent_velocity.x
                    v2y = apparent_velocity.y

                    m1 = body.mass
                    m2 = body.mass

                    u1 = Dimension2D(0, 0)
                    u1.x = (v1x * (m1 - m2) + v2x * (2 * m2)) / (m1 + m2)
                    u1.y = (v1y * (m1 - m2) + v2y * (2 * m2)) / (m1 + m2)
                    body.velocity = u1
                    continue

            # Calculate the new velocity of the body after a clash
            for other_body in self.list_bodies:
                if body != other_body:
                    distance = new_position.distance(other_body.position)
                    
                    if distance <= body.radius + other_body.radius:
                        self.logger.info(f"Clash between {body.name} and {other_body.name}")

                        v1x = body.velocity.x
                        v1y = body.velocity.y
                        m1 = body.mass
                        v2x = other_body.velocity.x
                        v2y = other_body.velocity.y
                        m2 = other_body.mass
                        
                        u1 = Dimension2D(0, 0)
                        u1.x = (v1x * (m1 - m2) + v2x * (2 * m2)) / (m1 + m2)
                        u1.y = (v1y * (m1 - m2) + v2y * (2 * m2)) / (m1 + m2)

                        u2 = Dimension2D(0, 0)
                        u2.x = (v2x * (m2 - m1) + v1x * (2 * m1)) / (m1 + m2)
                        u2.y = (v2y * (m2 - m1) + v1y * (2 * m1)) / (m1 + m2)

                        body.velocity = u1
                        other_body.velocity = u2

    def calculate_kinetic_energy(self, time) -> None:
        energy = 0
        for body in self.list_bodies:
            energy += body.calculate_kinetic_energy()
        
        self.kinetic_energy_data.append({ "x": time, "y": energy })

    def update(self) -> list[Body]:
        aceleration_k = self.calculate_aceleration()

        self.actual_time += self.dt
        self.calculate_elastic_clash(aceleration_k)
        self.calculate_kinetic_energy(self.actual_time)
        
        position_k1 = []
        for body in self.list_bodies:
            body_aceleartion_k = aceleration_k[self.list_bodies.index(body)]

            new_position = Dimension2D(0, 0)
            new_position.x = body.position.x + body.velocity.x * self.dt + (1/2) * body_aceleartion_k.x * self.dt**2
            new_position.y = body.position.y + body.velocity.y * self.dt + (1/2) * body_aceleartion_k.y * self.dt**2

            position_k1.append(new_position)
            body.add_path(new_position)

        aceleration_k1 = self.calculate_aceleration()

        for body in self.list_bodies:
            body_aceleration_k1 = aceleration_k1[self.list_bodies.index(body)]
            body_aceleration_k = aceleration_k1[self.list_bodies.index(body)]

            body.velocity.x += (1/2) * (body_aceleration_k.x + body_aceleration_k1.x) * self.dt
            body.velocity.y += (1/2) * (body_aceleration_k.y + body_aceleration_k1.y) * self.dt

        for body in self.list_bodies:
            body.aceleration = aceleration_k1[self.list_bodies.index(body)]
            body.position = position_k1[self.list_bodies.index(body)]


        return self.list_bodies
    