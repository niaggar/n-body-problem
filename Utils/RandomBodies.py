from Models import Body, Dimension2D, Bounds
from random import randint


def create_random_bodies(num: int, window_size: Bounds) -> list[Body]:
    bodies: list[Body] = []
    
    for i in range(num):
        name = f"Body {i}"
        radius = randint(5, 10)
        mass = radius * 1000
        velocity = Dimension2D(randint(-50, 50), randint(-50, 50))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        position = Dimension2D(randint(0, window_size.get_width()), randint(0, window_size.get_height()))

        body = Body(name, mass, radius, position, velocity, color)     
        bodies.append(body)
    
    return bodies
