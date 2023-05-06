from Models import Body, Dimenssion2D, Bounds
from Methods import Verlet

import logging
import pyglet
from pyglet.window import key
from pyglet import shapes
from random import randint


logging.basicConfig(filename='.\\logs\\main.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

def create_random_bodies(num) -> list[Body]:
    bodies: list[Body] = []
    for i in range(num):
        name = f"Body {i}"
        mass = randint(1, 100)
        radius = randint(10, 20)
        position = Dimenssion2D(randint(0, 1280), randint(0, 720))
        velocity = Dimenssion2D(randint(-100, 100), randint(-100, 100))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))

        body = Body(name, mass, radius, position, velocity, color)     
        bodies.append(body)

        logger.info(f"Created body: {body}")
    logger.info(f"Created {num} bodies")
    logger.info(f"\n")
    return bodies

NUMBER_OF_BODIES = 5
bodies = create_random_bodies(NUMBER_OF_BODIES)
bounds = Bounds(Dimenssion2D(0, 0), Dimenssion2D(1280, 720), 10)
verlete = Verlet(bodies, 1/60., bounds)
window = pyglet.window.Window()
window.set_size(1280, 720)

@window.event
def on_draw():
    global bodies
    window.clear()

    for body in bodies:
        main_bathc = shapes.Batch()
        color = body.color
        
        body_circle = shapes.Circle(x=body.position.x, y=body.position.y, radius=body.radius, color=color, batch=main_bathc)

        force = body.aceleration.scale(0.2)
        if force.magnitude() > 200:
            force = force.normalize().scale(200)
        force_line = shapes.Line(x=body.position.x, y=body.position.y, x2=body.position.x + force.x, y2=body.position.y + force.y, width=1, color=color, batch=main_bathc)
        force_point = shapes.Circle(x=body.position.x + force.x, y=body.position.y + force.y, radius=3, color=(255, 0, 0), batch=main_bathc)

        path_lines = []
        for i in range(len(body.path) - 1):
            point = body.path[i]
            next_point = body.path[i + 1]
            path_line = shapes.Line(x=point[0], y=point[1], x2=next_point[0], y2=next_point[1], width=3, color=color, batch=main_bathc)
            path_line.opacity = 100
            path_lines.append(path_line)

        main_bathc.draw()

@window.event
def on_key_press(symbol, modifiers):
    global bodies, verlete, NUMBER_OF_BODIES

    if symbol == key.ENTER:
        pyglet.clock.schedule_interval(update, 1/60.)
    elif symbol == key.SPACE:
        pyglet.clock.unschedule(update)
    elif symbol == key.R:
        bodies = create_random_bodies(NUMBER_OF_BODIES)
        verlete = Verlet(bodies, 1/60., bounds)

def update(dt):
    global bodies
    bodies = verlete.update()

pyglet.app.run()
